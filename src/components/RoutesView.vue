<template>
  <div id="container">
    <div id="map"></div>
    <div id="navbar">
      <div class="menu-bar">
        <button @click="emitSwitchView('routes')" :class="{ active: activeMenu === 'routes' }">Routes</button>
        <button @click="emitSwitchView('passengerFlow')" :class="{ active: activeMenu === 'passengerFlow' }">Passenger Flow</button>
      </div>
      <div class="switch-container" v-if="activeMenu === 'routes'">
        <div class="switch-row">
          <el-switch
            v-model="backgroundSwitch"
            size="medium"
            active-text="Color"
            inactive-text="Grey"
            @change="toggleBackground"
            class="switch-item"
          />
          <el-switch
            v-model="viewSwitch"
            size="medium"
            active-text="Stations"
            inactive-text="Routes"
            @change="toggleView"
            class="switch-item"
          />
        </div>
      </div>

      <div style="margin-top: 0px">
        <el-radio-group v-model="colorOption" @change="handleColorChange">
          <el-radio value="1" size="medium" border>Color 1</el-radio>
          <el-radio value="2" size="medium" border>Color 2</el-radio>
        </el-radio-group>
      </div>

      <div class="knob-radio-container" style="margin-top: 20px">
        <div class="knob-control-container">
          <knob-control
            v-model="angleRange"
            :min="0"
            :max="360"
            :step="1"
            size="100"
            stroke-width="5"
            @change="handleAngleChange"
          />
          <div class="angle-labels">
            <div class="angle-input">
              <label>Start Angle:</label>
              <el-input-number
                v-model.number="angleRange[0]"
                :min="0"
                :max="360"
                size="small"
                class="input-narrow"
                @change="validateAngle('start')"
              />
            </div>
            <div class="angle-input">
              <label>End Angle:</label>
              <el-input-number
                v-model.number="angleRange[1]"
                :min="0"
                :max="360"
                size="small"
                class="input-narrow"
                @change="validateAngle('end')"
              />
            </div>
          </div>
          <el-button @click="applyAngleRange" class="confirm-button">Submit</el-button>
        </div>
        <el-radio-group v-model="radio" class="radio-group" @change="handleRadioChange">
          <el-radio :value="'routes'">Routes</el-radio>
          <el-radio :value="'directions'">Directions</el-radio>
          <el-radio :value="'start'">Start</el-radio>
        </el-radio-group>
      </div>

      <div class="slider-container">
        <el-slider
          v-model="lineWeight"
          :min="3"
          :max="10"
          :show-stops="true"
          label="Line Weight"
          class="slider-short"
          @change="applyAngleRange"
        />
        <div class="slider-labels">
          <span>3</span>
          <span>10</span>
        </div>
      </div>

      <div v-if="activeMenu === 'routes'" class="category-menu">
        <button
          v-for="category in filteredCategories"
          :key="category.label"
          @click="selectCategory(category)"
          :class="{ active: selectedCategory === category.label }"
        >
          {{ category.label }}
        </button>
      </div>
      <div v-if="activeMenu === 'routes'" class="bus-list">
        <button
          v-for="bus in sortedBuses"
          :key="bus"
          @click="selectBus(bus)"
          :class="{ 'bus-active': selectedBus === bus }"
        >
          {{ bus }}
        </button>
      </div>
      <button @click="reset" class="reset-button">Reset</button>
    </div>
  </div>
</template>

<script>
import { onMounted, ref, onBeforeUnmount, watch, computed, toRaw } from 'vue';
import axios from 'axios';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { ElSwitch, ElSlider, ElRadio, ElRadioGroup, ElInputNumber, ElButton, ElMessage } from 'element-plus';
import 'element-plus/dist/index.css';
import KnobControl from './KnobControl.vue';
import tabsData from '@/data/tabs_data.json';

export default {
  name: 'RoutesView',
  components: {
    ElSwitch,
    ElSlider,
    ElRadio,
    ElRadioGroup,
    ElInputNumber,
    ElButton,
    KnobControl,
  },
  setup(props, { emit }) {
    const colorMap8 = ["rgb(245,201,70)", "rgb(231,135,60)", "rgb(218,55,62)", "rgb(111,48,140)", "rgb(50,71,153)", "rgb(78,155,195)", "rgb(120,186,87)", "rgb(225,231,121)"];
    const colorMap1 = ["#FF0D00", "#FF8900", "#FFB600", "#FFEE00", "#C9FF00", "#0DFF00", "#00FFF5", "#109CFF", "#186EFF", "#4B1FFF", "#9E10FF", "#FF0196"];
    const colorMap360 = Array.from({ length: 360 }, (_, i) => `hsl(${i}, 90%, 50%)`);

    const map = ref(null);
    const backgroundSwitch = ref(false);
    const viewSwitch = ref(false);
    const lineWeight = ref(3);
    const currentLayerGroup = ref(null);
    const mapInitialized = ref(false);
    const radio = ref('routes');
    const use360Colors = ref(false);
    const angleRange = ref([0, 360]);
    const colorOption = ref('1');
    const selectedBus = ref(null);
    const activeMenu = ref('routes');

    const categories = ref(tabsData.filter(category => category.numbers.length > 0));
    const selectedCategory = ref(categories.value[0]?.label || '');
    const selectedBuses = ref(categories.value[0]?.numbers || []);
    const filteredCategories = ref(categories.value);
    const isBusSelected = ref(false); // 用于标记当前是否有线路被选中
    const sortedBuses = computed(() => {
      return [...selectedBuses.value].sort((a, b) => a - b);
    });

    const initialState = {
      backgroundSwitch: false,
      viewSwitch: false,
      lineWeight: 3,
      selectedCategory: selectedCategory.value,
      selectedBuses: selectedBuses.value,
      center: [51.5074, -0.1278],
      zoom: 11,
    };

    const reset = () => {
      backgroundSwitch.value = initialState.backgroundSwitch;
      viewSwitch.value = initialState.viewSwitch;
      lineWeight.value = initialState.lineWeight;
      selectedCategory.value = initialState.selectedCategory;
      selectedBuses.value = initialState.selectedBuses;
      selectedBus.value = null;
      use360Colors.value = false;
      angleRange.value = [0,360];
      clearMap();
      fetchRoutes();
      if (map.value) {
        toRaw(map.value).setView(initialState.center, initialState.zoom);
      }
      console.log('State has been reset to initial values');
    };

    const selectCategory = (category) => {
      selectedCategory.value = category.label;
      selectedBuses.value = category.numbers;
      console.log('Category selected:', selectedCategory.value, 'Buses:', selectedBuses.value);
    };

    const getColorByAngle = (angle) => {
      if (use360Colors.value) {
        return colorMap360[Math.round(angle) % 360];
      } else if (colorOption.value === '1') {
        const index = Math.floor(angle / 45) % 8;
        return colorMap8[index];
      } else {
        const index = Math.floor(angle / 30) % 12;
        return colorMap1[index];
      }
    };

    const getRouteColor = (angle) => {
      if (isBusSelected.value){
        return getColorByAngle(angle);
      }
      if (angleRange.value[0] <= angleRange.value[1]) {
        return angle >= angleRange.value[0] && angle <= angleRange.value[1]
          ? getColorByAngle(angle)
          : 'lightgray';
      } else {
        return (angle >= angleRange.value[0] || angle <= angleRange.value[1])
          ? getColorByAngle(angle)
          : 'lightgray';
      }
    };

    const createArrowIcon = (angle, color) => {
      return L.divIcon({
        className: 'arrow-icon',
        html: `
          <div class="arrow-icon" style="transform: rotate(${angle}deg);">
            <svg class="arrow-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
              <polygon points="50,0 15,100 85,100" fill="${color}" />
            </svg>
          </div>
        `,
        iconSize: [20, 20],
        iconAnchor: [10, 10]
      });
    };

    const selectBus = async (bus) => {
      if (!map.value || !currentLayerGroup.value) return;

      console.log(`Selected bus: ${bus}`);
      selectedBus.value = bus;
      isBusSelected.value = true; // Marking the selected state

      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${bus}`);
        console.log('Route data fetched:', response.data);
        const routeData = response.data;
        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);
        clearMap();

        // 获取原始颜色或根据角度范围返回的颜色
        const originalColor = getRouteColor(routeData.angle, true);

        // Draw grey route
        L.polyline(points, { color: 'lightgray', weight: lineWeight.value, opacity: 0.5 }).addTo(toRaw(currentLayerGroup.value));

        // 绘制选中线路原始颜色
        L.polyline(points, { color: originalColor, weight: lineWeight.value, opacity: 0.8 }).addTo(toRaw(currentLayerGroup.value));

        // Draw colored route on top if within angle range
        const routeColor = getRouteColor(routeData.angle);
        const polyline = L.polyline(points, { color: routeColor, weight: lineWeight.value, opacity: 0.8 }).addTo(toRaw(currentLayerGroup.value));

        points.forEach((point, index) => {
          const marker = L.circleMarker(point, {
            radius: 5,
            color: 'white',
            weight: 1,
            fill: true,
            fillColor: routeColor,
            fillOpacity: 1
          });
          marker.bindTooltip(routeData.points[index].Stop_Name, { permanent: false, direction: 'top' });
          marker.on('mouseover', function () {
            this.openTooltip();
          });
          marker.on('mouseout', function () {
            this.closeTooltip();
          });
          marker.addTo(toRaw(currentLayerGroup.value));
        });

        const startPoint = routeData.points[0];
        const arrowIcon = createArrowIcon(routeData.angle, routeColor);
        L.marker([startPoint.Latitude, startPoint.Longitude], { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));

        // Add circle at the start point
        const startCircle = L.circleMarker([startPoint.Latitude, startPoint.Longitude], {
          radius: 6,
          color: 'white',
          weight: 2,
          fill: true,
          fillColor: routeColor,
          fillOpacity: 1
        });
        startCircle.addTo(toRaw(currentLayerGroup.value));

        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
        toRaw(map.value).fitBounds(polyline.getBounds());
        console.log('Route rendered successfully');

      } catch (error) {
        console.error(`Error fetching route data for ${bus}:`, error);
      } finally {
        isBusSelected.value = false;
      } // 清除选中状态
    };

    const fetchRoutes = async () => {
    if (!map.value || !currentLayerGroup.value) return;

    try {
      const response = await axios.get('http://127.0.0.1:5000/api/routes', {
        params: {
          min_angle: 0,
          max_angle: 360
        }
      });
      const routes = response.data;
      console.log('Fetched routes:', routes);  // 打印获取到的线路
      const routePromises = routes.map(route => fetchRouteData(route));
      const routeData = await Promise.all(routePromises);
      initializeMapWithRoutes(routeData.filter(route => route !== null));
    } catch (error) {
      console.error('Error fetching routes:', error);
    }
  };


    const fetchRouteData = async (route) => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);
        const routeData = response.data;
        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);
        return {
          routeId: routeData.route_id,
          points,
          angle: routeData.angle
        };
      } catch (error) {
        console.error(`Error fetching route data for ${route}:`, error);
        return null;
      }
    };


    const fetchStationData = async (routeId) => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
        const routeData = response.data;
        return routeData.points.map(point => ({
          Latitude: point.Latitude,
          Longitude: point.Longitude,
          Stop_Name: point.Stop_Name
        }));
      } catch (error) {
        console.error(`Error fetching station data for ${routeId}:`, error);
        return [];
      }
    };

    const initializeMapWithRoutes = (routes) => {
      clearMap();

      // First draw grey routes without Tooltip
      routes.forEach((route) => {
        if (currentLayerGroup.value) {
          L.polyline(route.points, {
            color: 'lightgray',
            weight: lineWeight.value,
            opacity: 0.5
          }).addTo(toRaw(currentLayerGroup.value));
        }
      });

      // Then draw colored routes with Tooltip
      routes.forEach((route) => {
        if (currentLayerGroup.value && (angleRange.value[0] <= angleRange.value[1]
            ? route.angle >= angleRange.value[0] && route.angle <= angleRange.value[1]
            : route.angle >= angleRange.value[0] || route.angle <= angleRange.value[1])) {
          const routeColor = getColorByAngle(route.angle);
          const polyline = L.polyline(route.points, {
            color: routeColor,
            weight: lineWeight.value,
            opacity: 0.7
          }).addTo(toRaw(currentLayerGroup.value));

          // 为彩色线路添加鼠标事件以显示 Tooltip
          polyline.on('mouseover', function (e) {
            const tooltip = L.tooltip({
              permanent: false,
              direction: 'top',
              className: 'route-tooltip'
            })
              .setContent(`Route: ${route.routeId}`)
              .setLatLng(e.latlng)
              .openOn(toRaw(map.value));

            this._currentTooltip = tooltip;
          });

          polyline.on('mousemove', function (e) {
            if (this._currentTooltip) {
              this._currentTooltip.setLatLng(e.latlng);
            }
          });

          polyline.on('mouseout', function () {
            if (this._currentTooltip) {
              toRaw(map.value).closeTooltip(this._currentTooltip);
              this._currentTooltip = null;
            }
          });

          // Add circle at the start point
          const startPoint = route.points[0];
          const startCircle = L.circleMarker(startPoint, {
            radius: 6,
            color: 'white',
            weight: 2,
            fill: true,
            fillColor: routeColor,
            fillOpacity: 1
          });
          startCircle.addTo(toRaw(currentLayerGroup.value));
        }
      });

      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
      }
    };


    const initializeMapWithStations = (stations) => {
      clearMap();
      stations.forEach(station => {
        if (currentLayerGroup.value) {
          const marker = L.circleMarker([station.Latitude, station.Longitude], {
            radius: 5,
            color: 'white',
            weight: 1,
            fill: true,
            fillColor: '#BC403A',
            fillOpacity: 1
          });

          marker.bindTooltip(station.Stop_Name, {permanent: false, direction: 'top'});
          marker.on('mouseover', function () {
            this.openTooltip();
          });
          marker.on('mouseout', function () {
            this.closeTooltip();
          });

          marker.addTo(toRaw(currentLayerGroup.value));
        }
      });
      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
      }
    };

    const clearMap = () => {
      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).clearLayers();
      }
    };

    const updateMapLayer = () => {
      if (map.value) {
        const tileLayerUrl = backgroundSwitch.value
            ? 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'
            : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';

        L.tileLayer(tileLayerUrl, {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          maxZoom: 19
        }).addTo(toRaw(map.value));
      }
    };

    const toggleBackground = () => {
      updateMapLayer();
    };

    const toggleView = () => {
      if (viewSwitch.value) {
        fetchStationsWithinAngleRange();
      } else {
        fetchRoutes();
      }
    };

    const handleRadioChange = async (value) => {
      if (value === 'directions') {
        use360Colors.value = true;
        await fetchDirections();
      } else if (value === 'start') {
        use360Colors.value = true;
        await fetchStartPoints();
      } else {
        use360Colors.value = false;
        fetchRoutes();
      }
    };

    const fetchDirections = async () => {
      if (!map.value || !currentLayerGroup.value) return;

      try {
        const response = await axios.get('http://127.0.0.1:5000/api/routes', {
          params: {
            min_angle: angleRange.value[0],
            max_angle: angleRange.value[1]
          }
        });
        const routes = response.data;

        clearMap();

        for (const route of routes) {
          const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);
          const routeData = routeResponse.data;

          const start = [routeData.points[0].Latitude, routeData.points[0].Longitude];
          const end = [routeData.points[routeData.points.length - 1].Latitude, routeData.points[routeData.points.length - 1].Longitude];
          const angle = routeData.angle;
          const routeColor = getColorByAngle(angle);

          L.polyline([start, end], {
            color: routeColor,
            weight: lineWeight.value,
            opacity: 0.6
          }).addTo(toRaw(currentLayerGroup.value));

          const arrowIcon = createArrowIcon(angle, routeColor);
          L.marker(start, {icon: arrowIcon}).addTo(toRaw(currentLayerGroup.value));
        }

        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
        console.log('Directions rendered successfully');

      } catch (error) {
        console.error('Error fetching directions:', error);
      }
    };

    const fetchStartPoints = async () => {
      if (!map.value || !currentLayerGroup.value) return;

      try {
        const response = await axios.get('http://127.0.0.1:5000/api/routes', {
          params: {
            min_angle: angleRange.value[0],
            max_angle: angleRange.value[1]
          }
        });
        const routes = response.data;

        clearMap();

        const routePromises = routes.map(route => fetchRouteData(route));
        const routeData = await Promise.all(routePromises);

        initializeMapWithStartPoints(routeData.filter(route => route !== null));

        console.log('Start points rendered successfully');
      } catch (error) {
        console.error('Error fetching start points:', error);
      }
    };

    const initializeMapWithStartPoints = (routes) => {
      clearMap();
      routes.forEach(route => {
        if (currentLayerGroup.value) {
          const routeColor = getColorByAngle(route.angle);
          const startPoint = route.points[0];
          const arrowIcon = createArrowIcon(route.angle, routeColor);
          L.marker(startPoint, {icon: arrowIcon}).addTo(toRaw(currentLayerGroup.value));
        }
      });
      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
      }
    };

    const fetchStationsWithinAngleRange = async () => {
      if (!map.value || !currentLayerGroup.value) return;

      try {
        const response = await axios.get('http://127.0.0.1:5000/api/routes', {
          params: {
            min_angle: angleRange.value[0],
            max_angle: angleRange.value[1]
          }
        });
        const routes = response.data;
        const stationPromises = routes.map(route => fetchStationData(route));
        const allStations = (await Promise.all(stationPromises)).flat();
        initializeMapWithStations(allStations);
      } catch (error) {
        console.error('Error fetching stations within angle range:', error);
      }
    };

    const handleAngleChange = () => {
      applyAngleRange();
    };

    const handleColorChange = () => {
      applyAngleRange();
    };

    const validateAngle = (type) => {
      if (type === 'start' && angleRange.value[0] > 360) {
        ElMessage.error('Start point cannot be greater than 360');
        angleRange.value[0] = 360;
      } else if (type === 'end' && angleRange.value[1] > 360) {
        ElMessage.error('End point cannot be greater than 360');
        angleRange.value[1] = 360;
      }
    };

    const applyAngleRange = () => {
      if (viewSwitch.value) {
        fetchStationsWithinAngleRange();
      } else if (radio.value === 'directions') {
        fetchDirections();
      } else if (radio.value === 'start') {
        fetchStartPoints();
      } else {
        fetchRoutes();
      }
    };

    const selectMenu = (menu) => {
      activeMenu.value = menu;
      console.log(`Selected menu: ${menu}`);
      applyAngleRange();
    };

    const emitSwitchView = (view) => {
      emit('switch-view', view);
    };

    watch(lineWeight, () => {
      applyAngleRange();
    });

    watch(backgroundSwitch, () => {
      updateMapLayer();
    });

    watch(viewSwitch, () => {
      toggleView();
    });

    onMounted(() => {
      L.Popup.prototype._animateZoom = function (e) {
        if (!this._map) {
          return;
        }
        var pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),
            anchor = this._getAnchor();
        L.DomUtil.setPosition(this._container, pos.add(anchor));
      };

      map.value = L.map('map').setView(initialState.center, initialState.zoom);
      currentLayerGroup.value = L.layerGroup().addTo(toRaw(map.value));
      mapInitialized.value = true;
      updateMapLayer();
      fetchRoutes();
    });

    onBeforeUnmount(() => {
      mapInitialized.value = false;
      if (map.value) {
        toRaw(map.value).remove();
        map.value = null;
      }
      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).clearLayers();
        currentLayerGroup.value = null;
      }
    });

    return {
      backgroundSwitch,
      viewSwitch,
      lineWeight,
      toggleBackground,
      toggleView,
      categories,
      filteredCategories,
      selectedCategory,
      selectedBuses,
      sortedBuses,
      selectCategory,
      selectBus,
      reset,
      radio,
      handleRadioChange,
      angleRange,
      handleAngleChange,
      colorOption,
      handleColorChange,
      validateAngle,
      applyAngleRange,
      selectedBus,
      activeMenu,
      selectMenu,
      emitSwitchView,
    };
  }
};
</script>

<style scoped>
#container {
  display: flex;
  height: 100vh;
  overflow: hidden;
}

#map {
  flex-grow: 1;
}

#navbar {
  width: 350px;
  background-color: white;
  border-left: 1px solid #ccc;
  padding: 10px;
  display: flex;
  flex-direction: column;
  justify-content: flex-start;
  align-items: center;
  overflow-y: auto;
}

.menu-bar {
  width: 100%;
  display: flex;
  justify-content: space-around;
  background-color: #ffffff;
  padding: 10px 0;
  margin-bottom: 10px;
}

.menu-bar button {
  width: 45%;
  border: none;
  background-color: #d9e6fc;
  cursor: pointer;
  text-align: center;
  padding: 10px 0;
  border-radius: 5px;
  font-size: 16px;
}

.menu-bar button.active {
  background-color: #5a9cf8;
  color: white;
}

.switch-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  margin-bottom: 10px;
  width: 100%;
}

.switch-row {
  display: flex;
  justify-content: space-between;
  width: 100%;
}

.switch-item {
  margin-bottom: 10px;
}

.knob-radio-container {
  border: 3px solid #5a9cf8;
  border-radius: 10px;
  padding: 10px;
  margin-bottom: 10px;
  width: 90%;
  display: flex;
  flex-direction: column;
  align-items: center;
}

.knob-control-container {
  display: flex;
  align-items: center;
  justify-content: center;
  margin-bottom: 10px;
  width: 100%;
}

.angle-labels {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  justify-content: center;
  margin-left: 20px;
}

.angle-labels span {
  font-size: 0.8em;
  margin-bottom: 5px;
}

.angle-input {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  font-size: 0.8em;
  margin-bottom: 5px;
}

.input-narrow .el-input-number {
  width: 80px;
}

.confirm-button {
  margin-top: 10px;
  margin-left: 10px;
  padding: 5px 10px;
  font-size: 12px;
  border-radius: 5px;
}

.el-input-number--small .el-input__inner {
  height: 22px;
  padding: 0 7px;
}

.radio-group {
  margin-bottom: 0px;
}

.slider-container {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 10px;
}

.slider-short {
  width: 150px;
}


.slider-labels {
  display: flex;
  justify-content: space-between;
  width: 100%;
  padding: 0 20px;
}

.slider-label {
  font-size: 0.8em;
}

.category-menu {
  display: grid;
  grid-template-columns: repeat(4, 1fr);
  gap: 8px;
  margin-top: 20px;
}

.category-menu button {
  padding: 5px;
  height: 30px;
  border: none;
  background-color: #eee;
  cursor: pointer;
  text-align: center;
  border-radius: 10px;
  font-size: 0.8em;
}

.category-menu button.active {
  background-color: #333;
  color: white;
}

.bus-list {
  display: grid;
  grid-template-columns: repeat(8, 1fr);
  gap: 5px;
  margin-top: 10px;
  width: 100%;
}

.bus-list button {
  height: 30px;
  border: none;
  background-color: #f0f8ff;
  color: #0000ee;
  cursor: pointer;
  text-align: center;
  line-height: 25px;
  border-radius: 3px;
  font-size: 0.8em;
  padding: 3px;
}

.bus-list button.bus-active {
  border: 2px solid blue;
  font-weight: bold;
}

.reset-button {
  margin-top: 20px;
  padding: 10px 20px;
  border: none;
  background-color: #ff6347;
  color: white;
  cursor: pointer;
  text-align: center;
  border-radius: 5px;
}

.arrow-icon {
  display: flex;
  justify-content: center;
  align-items: center;
  transform-origin: center;
}

.arrow-svg {
  width: 20px;
  height: 20px;
}
</style>

