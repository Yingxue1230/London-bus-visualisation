<!--<template>-->
<!--  <el-container style="height: 100vh; width: 100vw;">-->
<!--    <el-container>-->
<!--      <el-main style="padding: 0; height: 100%;">-->
<!--        <div id="map-container">-->
<!--          <iframe id="map-frame" :src="mapSrc" width="100%" height="100%" style="border: none;"></iframe>-->
<!--        </div>-->
<!--      </el-main>-->
<!--    </el-container>-->
<!--    <el-aside width="300px" style="height: 100vh; overflow: auto;">-->
<!--      <div class="sidebar-content">-->
<!--        <div class="switch-container">-->
<!--          <el-switch-->
<!--            v-model="showStations"-->
<!--            active-text="Stations"-->
<!--            inactive-text="Routes"-->
<!--            @change="updateMapSrc"-->
<!--          />-->
<!--        </div>-->
<!--        <div class="switch-container">-->
<!--          <el-switch-->
<!--            v-model="isGray"-->
<!--            active-text="Colour"-->
<!--            inactive-text="Gray"-->
<!--            @change="updateMapSrc"-->
<!--            class="ml-2"-->

<!--          />-->
<!--        </div>-->
<!--        <div class="bus-index">-->
<!--          <h2>Which bus are you looking for?</h2>-->
<!--          <div class="tab-container">-->
<!--            <div-->
<!--              v-for="(tab, index) in filteredTabs"-->
<!--              :key="index"-->
<!--              :class="['tab', { active: activeTab === index }]"-->
<!--              @click="setActiveTab(index)"-->
<!--            >-->
<!--              {{ tab.label }}-->
<!--            </div>-->
<!--          </div>-->
<!--          <div class="bus-numbers">-->
<!--            <div-->
<!--              v-for="number in filteredTabs[activeTab].sortedNumbers"-->
<!--              :key="number"-->
<!--              :class="['bus-number', { selected: selectedNumber === number }]"-->
<!--            >-->
<!--              <a href="#" @click.prevent="loadRoute(number)">{{ number }}</a>-->
<!--            </div>-->
<!--          </div>-->
<!--        </div>-->
<!--        <div class="reset-button">-->
<!--          <el-button type="primary" @click="reset">Reset</el-button>-->
<!--        </div>-->
<!--      </div>-->
<!--    </el-aside>-->
<!--  </el-container>-->
<!--</template>-->

<!--<script>-->
<!--import tabsData from '@/data/tabs_data.json'; // 导入本地 JSON 文件-->

<!--export default {-->
<!--  data() {-->
<!--    return {-->
<!--      showStations: false,-->
<!--      mapSrc: 'http://127.0.0.1:5000/london_bus_route_2024_gray.html', // 初始地图路径-->
<!--      activeTab: 0,-->
<!--      selectedNumber: null, // 选中的公交号码-->
<!--      tabs: tabsData.map(tab => ({-->
<!--        ...tab,-->
<!--        sortedNumbers: tab.numbers.sort((a, b) => a - b)-->
<!--      })), // 对每个分类的号码进行排序-->
<!--      isGray: false // 新增：地图是否为灰色-->
<!--    };-->
<!--  },-->
<!--  computed: {-->
<!--    filteredTabs() {-->
<!--      return this.tabs.filter(tab => tab.numbers.length > 0);-->
<!--    }-->
<!--  },-->
<!--  methods: {-->
<!--    updateMapSrc() {-->
<!--      if (this.showStations) {-->
<!--        this.mapSrc = this.isGray ? 'http://127.0.0.1:5000/london_bus_stations_2024.html' : 'http://127.0.0.1:5000/london_bus_stations_2024_gray.html';-->
<!--      } else {-->
<!--        this.mapSrc = this.isGray ? 'http://127.0.0.1:5000/london_bus_route_2024.html' : 'http://127.0.0.1:5000/london_bus_route_2024_gray.html';-->
<!--      }-->
<!--    },-->
<!--    setActiveTab(index) {-->
<!--      this.activeTab = index;-->
<!--    },-->
<!--    loadRoute(routeNumber) {-->
<!--      this.selectedNumber = routeNumber; // 设置选中的公交号码-->
<!--      this.mapSrc = `http://127.0.0.1:5000/routes/london_bus_route_${routeNumber}.html`;-->
<!--    },-->
<!--    reset() {-->
<!--      this.showStations = false;-->
<!--      this.isGray = false;-->
<!--      this.mapSrc = 'http://127.0.0.1:5000/london_bus_route_2024_gray.html'; // 恢复初始地图路径-->
<!--      this.activeTab = 0;-->
<!--      this.selectedNumber = null; // 清除选中的公交号码-->
<!--    }-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--html, body, #app {-->
<!--  height: 100%;-->
<!--  margin: 0;-->
<!--  overflow: hidden; /* 确保其他部分没有滚动条 */-->
<!--}-->

<!--#map-container {-->
<!--  width: 100%;-->
<!--  height: 100%;-->
<!--  overflow: hidden; /* 确保地图部分没有滚动条 */-->
<!--}-->

<!--.sidebar-content {-->
<!--  padding: 20px;-->
<!--}-->

<!--.switch-container {-->
<!--  margin-bottom: 20px; /* 添加间距 */-->
<!--}-->

<!--.bus-index {-->
<!--  padding: 15px 0;-->
<!--}-->

<!--.tab-container {-->
<!--  display: flex;-->
<!--  flex-wrap: wrap;-->
<!--  margin-bottom: 20px;-->
<!--}-->

<!--.tab {-->
<!--  padding: 5px 10px;-->
<!--  font-size: 0.9em;-->
<!--  cursor: pointer;-->
<!--  background-color: #f2f2f2;-->
<!--  margin-right: 10px;-->
<!--  margin-bottom: 10px;-->
<!--  border-radius: 4px;-->
<!--}-->

<!--.tab.active {-->
<!--  background-color: #3c3c3c;-->
<!--  color: white;-->
<!--}-->

<!--.bus-numbers {-->
<!--  display: flex;-->
<!--  flex-wrap: wrap;-->
<!--}-->

<!--.bus-number {-->
<!--  width: 40px;-->
<!--  height: 40px;-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  justify-content: center;-->
<!--  background-color: #e6f7ff;-->
<!--  margin-right: 10px;-->
<!--  margin-bottom: 10px;-->
<!--  border-radius: 4px;-->
<!--  border: 2px solid transparent; /* 添加边框 */-->
<!--}-->

<!--.bus-number a {-->
<!--  text-decoration: none;-->
<!--  color: #007bff;-->
<!--  font-size: 0.9em;-->
<!--}-->

<!--.bus-number.selected {-->
<!--  border: 2px solid #007bff; /* 仅改变边框颜色 */-->
<!--  font-weight: bold; /* 可以增加字体粗细以突出显示 */-->
<!--}-->

<!--.reset-button {-->
<!--  text-align: center;-->
<!--  margin-top: 10px;-->
<!--}-->

<!--.toggle-map-style {-->
<!--  text-align: center;-->
<!--  margin-top: 10px;-->
<!--}-->
<!--</style>-->




<!--<template>-->
<!--  <div id="container">-->
<!--    <div id="map"></div>-->
<!--    <div id="navbar">-->
<!--      <el-switch-->
<!--        v-model="backgroundSwitch"-->
<!--        size="large"-->
<!--        active-text="Color"-->
<!--        inactive-text="Gray"-->
<!--        @change="toggleBackground"-->
<!--      />-->
<!--      <el-switch-->
<!--        v-model="viewSwitch"-->
<!--        size="large"-->
<!--        active-text="Routes"-->
<!--        inactive-text="Stations"-->
<!--        @change="toggleView"-->
<!--      />-->
<!--      <div class="slider-container">-->
<!--        <el-slider-->
<!--          v-model="lineWeight"-->
<!--          :min="3"-->
<!--          :max="10"-->
<!--          :show-stops="true"-->
<!--          label="Line Weight"-->
<!--          class="slider-short"-->
<!--        />-->
<!--        <div class="slider-labels">-->
<!--          <span>3</span>-->
<!--          <span>10</span>-->
<!--        </div>-->
<!--      </div>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { onMounted, ref, onBeforeUnmount, watch } from 'vue';-->
<!--import axios from 'axios';-->
<!--import L from 'leaflet';-->
<!--import 'leaflet/dist/leaflet.css';-->
<!--import { ElSwitch, ElSlider } from 'element-plus';-->
<!--import 'element-plus/dist/index.css';-->

<!--export default {-->
<!--  name: 'MapView',-->
<!--  components: {-->
<!--    ElSwitch,-->
<!--    ElSlider,-->
<!--  },-->
<!--  setup() {-->
<!--    const colorMap = [-->
<!--      "rgb(186,104,48)", "rgb(13,77,161)", "rgb(190,200,212)", "rgb(128,130,133)", "rgb(0,169,157)",-->
<!--      "rgb(242,135,182)", "rgb(64,199,244)", "rgb(124,203,192)", "rgb(150,46,51)", "rgb(185,151,115)",-->
<!--      "rgb(34,30,31)", "rgb(35,178,75)", "rgb(237,2,140)", "rgb(238,29,35)", "rgb(0,114,54)",-->
<!--      "rgb(145,38,143)", "rgb(255,200,150)", "rgb(247,147,29)", "rgb(0,149,217)", "rgb(177,1,106)", "rgb(166,206,57)"-->
<!--    ];-->

<!--    const map = ref(null);-->
<!--    const backgroundSwitch = ref(false);-->
<!--    const viewSwitch = ref(false); // false for Routes, true for Stations-->
<!--    const lineWeight = ref(3); // Initial line weight-->
<!--    const currentLayerGroup = ref(null);-->

<!--    const fetchRoutes = async () => {-->
<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes');-->
<!--        const routes = response.data;-->
<!--        const routePromises = routes.map(route => fetchRouteData(route));-->
<!--        const routeData = await Promise.all(routePromises);-->
<!--        initializeMapWithRoutes(routeData.filter(route => route !== null));-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching routes:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRouteData = async (route) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        return {-->
<!--          routeId: routeData.route_id,-->
<!--          points-->
<!--        };-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${route}:`, error);-->
<!--        return null;-->
<!--      }-->
<!--    };-->

<!--    const fetchAllStations = async () => {-->
<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes');-->
<!--        const routes = response.data;-->
<!--        const stationPromises = routes.map(route => fetchStationData(route));-->
<!--        const allStations = (await Promise.all(stationPromises)).flat();-->
<!--        initializeMapWithStations(allStations);-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching all stations data:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchStationData = async (routeId) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = response.data;-->
<!--        return routeData.points.map(point => ({-->
<!--          Latitude: point.Latitude,-->
<!--          Longitude: point.Longitude,-->
<!--          Stop_Name: point.Stop_Name-->
<!--        }));-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching station data for ${routeId}:`, error);-->
<!--        return [];-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithRoutes = (routes) => {-->
<!--      clearMap();-->
<!--      routes.forEach((route, index) => {-->
<!--        L.polyline(route.points, { color: colorMap[index % colorMap.length], weight: lineWeight.value, opacity: 0.8 }).addTo(currentLayerGroup.value);-->
<!--      });-->
<!--      currentLayerGroup.value.addTo(map.value);-->
<!--    };-->

<!--    const initializeMapWithStations = (stations) => {-->
<!--      clearMap();-->
<!--      stations.forEach(station => {-->
<!--        const marker = L.circleMarker([station.Latitude, station.Longitude], {-->
<!--          radius: 5,-->
<!--          color: 'white',-->
<!--          weight: 1,-->
<!--          fill: true,-->
<!--          fillColor: '#BC403A',-->
<!--          fillOpacity: 1-->
<!--        });-->

<!--        marker.bindTooltip(station.Stop_Name, { permanent: false, direction: 'top' });-->
<!--        marker.on('mouseover', function () {-->
<!--          this.openTooltip();-->
<!--        });-->
<!--        marker.on('mouseout', function () {-->
<!--          this.closeTooltip();-->
<!--        });-->

<!--        marker.addTo(currentLayerGroup.value);-->
<!--      });-->
<!--      currentLayerGroup.value.addTo(map.value);-->
<!--    };-->

<!--    const clearMap = () => {-->
<!--      if (currentLayerGroup.value) {-->
<!--        currentLayerGroup.value.clearLayers();-->
<!--      }-->
<!--    };-->

<!--    const updateMapLayer = () => {-->
<!--      if (map.value) {-->
<!--        const tileLayerUrl = backgroundSwitch.value-->
<!--          ? 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'-->
<!--          : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';-->

<!--        L.tileLayer(tileLayerUrl, {-->
<!--          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',-->
<!--          maxZoom: 19-->
<!--        }).addTo(map.value);-->
<!--      }-->
<!--    };-->

<!--    const toggleBackground = () => {-->
<!--      updateMapLayer();-->
<!--    };-->

<!--    const toggleView = () => {-->
<!--      if (viewSwitch.value) {-->
<!--        fetchAllStations();-->
<!--      } else {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    watch(lineWeight, () => {-->
<!--      if (!viewSwitch.value) {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    });-->

<!--    onMounted(() => {-->
<!--      map.value = L.map('map').setView([51.5074, -0.1278], 12);-->
<!--      currentLayerGroup.value = L.layerGroup().addTo(map.value);-->
<!--      updateMapLayer();-->
<!--      fetchRoutes();-->
<!--    });-->

<!--    onBeforeUnmount(() => {-->
<!--      if (map.value) {-->
<!--        map.value.remove();-->
<!--        map.value = null;-->
<!--      }-->
<!--      if (currentLayerGroup.value) {-->
<!--        currentLayerGroup.value.clearLayers();-->
<!--        currentLayerGroup.value = null;-->
<!--      }-->
<!--    });-->

<!--    return {-->
<!--      backgroundSwitch,-->
<!--      viewSwitch,-->
<!--      lineWeight,-->
<!--      toggleBackground,-->
<!--      toggleView-->
<!--    };-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style>-->
<!--#container {-->
<!--  display: flex;-->
<!--  height: 100vh;-->
<!--}-->

<!--#map {-->
<!--  flex-grow: 1;-->
<!--}-->

<!--#navbar {-->
<!--  width: 300px;-->
<!--  background-color: white;-->
<!--  border-left: 1px solid #ccc;-->
<!--  padding: 10px;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  justify-content: flex-start; /* Align items at the top */-->
<!--  align-items: center; /* Center items horizontally */-->
<!--}-->

<!--.slider-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--  margin-top: 20px; /* Move the slider down */-->
<!--}-->

<!--.slider-short {-->
<!--  width: 150px; /* Make the slider shorter */-->
<!--}-->

<!--.slider-labels {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--  width: 100%;-->
<!--  padding: 0 20px; /* Add padding to align with slider */-->
<!--}-->
<!--</style>-->




<!--<template>-->
<!--  <div id="container">-->
<!--    <div id="map"></div>-->
<!--    <div id="navbar">-->
<!--      <div class="switch-container">-->
<!--        <el-switch-->
<!--          v-model="backgroundSwitch"-->
<!--          size="large"-->
<!--          active-text="Color"-->
<!--          inactive-text="Grey"-->
<!--          @change="toggleBackground"-->
<!--          class="switch-item"-->
<!--        />-->
<!--        <el-switch-->
<!--          v-model="viewSwitch"-->
<!--          size="large"-->
<!--          active-text="Stations"-->
<!--          inactive-text="Routes"-->
<!--          @change="toggleView"-->
<!--          class="switch-item"-->
<!--        />-->
<!--      </div>-->
<!--      <div class="slider-container">-->
<!--        <el-slider-->
<!--          v-model="lineWeight"-->
<!--          :min="3"-->
<!--          :max="10"-->
<!--          :show-stops="true"-->
<!--          label="Line Weight"-->
<!--          class="slider-short"-->
<!--        />-->
<!--        <div class="slider-labels">-->
<!--          <span>3</span>-->
<!--          <span>10</span>-->
<!--        </div>-->
<!--      </div>-->
<!--      <div class="category-menu">-->
<!--        <button-->
<!--          v-for="category in filteredCategories"-->
<!--          :key="category.label"-->
<!--          @click="selectCategory(category)"-->
<!--          :class="{ active: selectedCategory === category.label }"-->
<!--        >-->
<!--          {{ category.label }}-->
<!--        </button>-->
<!--      </div>-->
<!--      <div class="bus-list">-->
<!--        <button-->
<!--          v-for="bus in sortedBuses"-->
<!--          :key="bus"-->
<!--          @click="selectBus(bus)"-->
<!--        >-->
<!--          {{ bus }}-->
<!--        </button>-->
<!--      </div>-->
<!--      <button @click="reset" class="reset-button">Reset</button>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { onMounted, ref, onBeforeUnmount, watch, computed, toRaw } from 'vue';-->
<!--import axios from 'axios';-->
<!--import L from 'leaflet';-->
<!--import 'leaflet/dist/leaflet.css';-->
<!--import { ElSwitch, ElSlider } from 'element-plus';-->
<!--import 'element-plus/dist/index.css';-->

<!--import tabsData from '@/data/tabs_data.json';-->

<!--export default {-->
<!--  name: 'MapView',-->
<!--  components: {-->
<!--    ElSwitch,-->
<!--    ElSlider,-->
<!--  },-->
<!--  setup() {-->
<!--    const colorMap = [-->
<!--      "rgb(186,104,48)", "rgb(13,77,161)", "rgb(190,200,212)", "rgb(128,130,133)", "rgb(0,169,157)",-->
<!--      "rgb(242,135,182)", "rgb(64,199,244)", "rgb(124,203,192)", "rgb(150,46,51)", "rgb(185,151,115)",-->
<!--      "rgb(34,30,31)", "rgb(35,178,75)", "rgb(237,2,140)", "rgb(238,29,35)", "rgb(0,114,54)",-->
<!--      "rgb(145,38,143)", "rgb(255,200,150)", "rgb(247,147,29)", "rgb(0,149,217)", "rgb(177,1,106)", "rgb(166,206,57)"-->
<!--    ];-->

<!--    const map = ref(null);-->
<!--    const backgroundSwitch = ref(false);-->
<!--    const viewSwitch = ref(false); // false for Routes, true for Stations-->
<!--    const lineWeight = ref(3); // Initial line weight-->
<!--    const currentLayerGroup = ref(null);-->
<!--    const mapInitialized = ref(false);-->

<!--    const categories = ref(tabsData.filter(category => category.numbers.length > 0));-->
<!--    const selectedCategory = ref(categories.value[0]?.label || '');-->
<!--    const selectedBuses = ref(categories.value[0]?.numbers || []);-->
<!--    const filteredCategories = ref(categories.value);-->
<!--    const sortedBuses = computed(() => {-->
<!--      return [...selectedBuses.value].sort((a, b) => a - b);-->
<!--    });-->

<!--    const initialState = {-->
<!--      backgroundSwitch: false,-->
<!--      viewSwitch: false,-->
<!--      lineWeight: 3,-->
<!--      selectedCategory: selectedCategory.value,-->
<!--      selectedBuses: selectedBuses.value,-->
<!--      center: [51.5074, -0.1278],-->
<!--      zoom: 12,-->
<!--    };-->

<!--    const reset = () => {-->
<!--      backgroundSwitch.value = initialState.backgroundSwitch;-->
<!--      viewSwitch.value = initialState.viewSwitch;-->
<!--      lineWeight.value = initialState.lineWeight;-->
<!--      selectedCategory.value = initialState.selectedCategory;-->
<!--      selectedBuses.value = initialState.selectedBuses;-->
<!--      clearMap();-->
<!--      fetchRoutes();-->
<!--      if (map.value) {-->
<!--        toRaw(map.value).setView(initialState.center, initialState.zoom);-->
<!--      }-->
<!--      console.log('State has been reset to initial values');-->
<!--    };-->

<!--    const selectCategory = (category) => {-->
<!--      selectedCategory.value = category.label;-->
<!--      selectedBuses.value = category.numbers;-->
<!--      console.log('Category selected:', selectedCategory.value, 'Buses:', selectedBuses.value);-->
<!--    };-->

<!--    const selectBus = async (bus) => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      console.log(`Selected bus: ${bus}`);-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${bus}`);-->
<!--        console.log('Route data fetched:', response.data);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        clearMap();-->
<!--        const routeColor = colorMap[Math.floor(Math.random() * colorMap.length)];-->
<!--        const polyline = L.polyline(points, { color: routeColor, weight: lineWeight.value, opacity: 0.8 }).addTo(toRaw(currentLayerGroup.value));-->

<!--        points.forEach((point, index) => {-->
<!--          const marker = L.circleMarker(point, {-->
<!--            radius: 5,-->
<!--            color: 'white',-->
<!--            weight: 1,-->
<!--            fill: true,-->
<!--            fillColor: routeColor,-->
<!--            fillOpacity: 1-->
<!--          });-->
<!--          marker.bindTooltip(routeData.points[index].Stop_Name, { permanent: false, direction: 'top' });-->
<!--          marker.on('mouseover', function () {-->
<!--            this.openTooltip();-->
<!--          });-->
<!--          marker.on('mouseout', function () {-->
<!--            this.closeTooltip();-->
<!--          });-->
<!--          marker.addTo(toRaw(currentLayerGroup.value));-->
<!--        });-->

<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--        toRaw(map.value).fitBounds(polyline.getBounds());-->
<!--        console.log('Route rendered successfully');-->

<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${bus}:`, error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRoutes = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes');-->
<!--        const routes = response.data;-->
<!--        const routePromises = routes.map(route => fetchRouteData(route));-->
<!--        const routeData = await Promise.all(routePromises);-->
<!--        initializeMapWithRoutes(routeData.filter(route => route !== null));-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching routes:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRouteData = async (route) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        return {-->
<!--          routeId: routeData.route_id,-->
<!--          points-->
<!--        };-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${route}:`, error);-->
<!--        return null;-->
<!--      }-->
<!--    };-->

<!--    const fetchAllStations = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes');-->
<!--        const routes = response.data;-->
<!--        const stationPromises = routes.map(route => fetchStationData(route));-->
<!--        const allStations = (await Promise.all(stationPromises)).flat();-->
<!--        initializeMapWithStations(allStations);-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching all stations data:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchStationData = async (routeId) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = response.data;-->
<!--        return routeData.points.map(point => ({-->
<!--          Latitude: point.Latitude,-->
<!--          Longitude: point.Longitude,-->
<!--          Stop_Name: point.Stop_Name-->
<!--        }));-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching station data for ${routeId}:`, error);-->
<!--        return [];-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithRoutes = (routes) => {-->
<!--      clearMap();-->
<!--      routes.forEach((route, index) => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          L.polyline(route.points, { color: colorMap[index % colorMap.length], weight: lineWeight.value, opacity: 0.8 }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithStations = (stations) => {-->
<!--      clearMap();-->
<!--      stations.forEach(station => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const marker = L.circleMarker([station.Latitude, station.Longitude], {-->
<!--            radius: 5,-->
<!--            color: 'white',-->
<!--            weight: 1,-->
<!--            fill: true,-->
<!--            fillColor: '#BC403A',-->
<!--            fillOpacity: 1-->
<!--          });-->

<!--          marker.bindTooltip(station.Stop_Name, { permanent: false, direction: 'top' });-->
<!--          marker.on('mouseover', function () {-->
<!--            this.openTooltip();-->
<!--          });-->
<!--          marker.on('mouseout', function () {-->
<!--            this.closeTooltip();-->
<!--          });-->

<!--          marker.addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const clearMap = () => {-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).clearLayers();-->
<!--      }-->
<!--    };-->

<!--    const updateMapLayer = () => {-->
<!--      if (map.value) {-->
<!--        const tileLayerUrl = backgroundSwitch.value-->
<!--          ? 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'-->
<!--          : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';-->

<!--        L.tileLayer(tileLayerUrl, {-->
<!--          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',-->
<!--          maxZoom: 19-->
<!--        }).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const toggleBackground = () => {-->
<!--      updateMapLayer();-->
<!--    };-->

<!--    const toggleView = () => {-->
<!--      if (viewSwitch.value) {-->
<!--        fetchAllStations();-->
<!--      } else {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    watch(lineWeight, () => {-->
<!--      if (!viewSwitch.value) {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    });-->

<!--    onMounted(() => {-->
<!--      // 修复 Leaflet 的 _animateZoom 方法-->
<!--      L.Popup.prototype._animateZoom = function (e) {-->
<!--        if (!this._map) {-->
<!--          return;-->
<!--        }-->
<!--        var pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),-->
<!--            anchor = this._getAnchor();-->
<!--        L.DomUtil.setPosition(this._container, pos.add(anchor));-->
<!--      };-->

<!--      // 初始化 Leaflet 地图-->
<!--      map.value = L.map('map').setView(initialState.center, initialState.zoom);-->
<!--      currentLayerGroup.value = L.layerGroup().addTo(toRaw(map.value));-->
<!--      mapInitialized.value = true;-->
<!--      updateMapLayer();-->
<!--      fetchRoutes();-->
<!--    });-->

<!--    onBeforeUnmount(() => {-->
<!--      mapInitialized.value = false;-->
<!--      if (map.value) {-->
<!--        toRaw(map.value).remove();-->
<!--        map.value = null;-->
<!--      }-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).clearLayers();-->
<!--        currentLayerGroup.value = null;-->
<!--      }-->
<!--    });-->

<!--    return {-->
<!--      backgroundSwitch,-->
<!--      viewSwitch,-->
<!--      lineWeight,-->
<!--      toggleBackground,-->
<!--      toggleView,-->
<!--      categories,-->
<!--      filteredCategories,-->
<!--      selectedCategory,-->
<!--      selectedBuses,-->
<!--      sortedBuses,-->
<!--      selectCategory,-->
<!--      selectBus,-->
<!--      reset,-->
<!--    };-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style>-->
<!--#container {-->
<!--  display: flex;-->
<!--  height: 100vh;-->
<!--}-->

<!--#map {-->
<!--  flex-grow: 1;-->
<!--}-->

<!--#navbar {-->
<!--  width: 300px;-->
<!--  background-color: white;-->
<!--  border-left: 1px solid #ccc;-->
<!--  padding: 10px;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  justify-content: flex-start;-->
<!--  align-items: center;-->
<!--  overflow-y: auto;-->
<!--}-->

<!--.switch-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--  justify-content: center; /* Vertically centers the items */-->
<!--  margin-bottom: 20px;-->
<!--  width: 100%; /* Ensure the switches take full width */-->
<!--}-->

<!--.switch-item {-->
<!--  margin-bottom: 20px;-->
<!--}-->

<!--.slider-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--  margin-top: 20px;-->
<!--}-->

<!--.slider-short {-->
<!--  width: 150px;-->
<!--}-->

<!--.slider-labels {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--  width: 100%;-->
<!--  padding: 0 20px;-->
<!--}-->

<!--.category-menu {-->
<!--  display: grid;-->
<!--  grid-template-columns: repeat(3, 1fr);-->
<!--  gap: 10px;-->
<!--  margin-top: 20px;-->
<!--  font-size: 0.9em;-->
<!--}-->

<!--.category-menu button {-->
<!--  padding: 10px;-->
<!--  border: none;-->
<!--  background-color: #eee;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  border-radius: 10px;-->
<!--}-->

<!--.category-menu button.active {-->
<!--  background-color: #333;-->
<!--  color: white;-->
<!--}-->

<!--.bus-list {-->
<!--  display: grid;-->
<!--  grid-template-columns: repeat(5, 1fr);-->
<!--  gap: 10px;-->
<!--  margin-top: 20px;-->
<!--  width: 100%;-->
<!--  font-size: 0.9em;-->
<!--}-->

<!--.bus-list button {-->
<!--  height: 40px;-->
<!--  border: none;-->
<!--  background-color: #f0f8ff;-->
<!--  color: #0000ee;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  line-height: 40px;-->
<!--  border-radius: 5px;-->
<!--}-->

<!--.reset-button {-->
<!--  margin-top: 20px;-->
<!--  padding: 10px 20px;-->
<!--  border: none;-->
<!--  background-color: #ff6347;-->
<!--  color: white;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  border-radius: 5px;-->
<!--}-->
<!--</style>-->




<!--<template>-->
<!--  <div id="container">-->
<!--    <div id="map"></div>-->
<!--    <div id="navbar">-->
<!--      <div class="switch-container">-->
<!--        <div class="switch-row">-->
<!--          <el-switch-->
<!--            v-model="backgroundSwitch"-->
<!--            size="medium"-->
<!--            active-text="Color"-->
<!--            inactive-text="Grey"-->
<!--            @change="toggleBackground"-->
<!--            class="switch-item"-->
<!--          />-->
<!--          <el-switch-->
<!--            v-model="viewSwitch"-->
<!--            size="medium"-->
<!--            active-text="Stations"-->
<!--            inactive-text="Routes"-->
<!--            @change="toggleView"-->
<!--            class="switch-item"-->
<!--          />-->
<!--        </div>-->
<!--      </div>-->

<!--      <div style="margin-top: 0px">-->
<!--        <el-radio-group v-model="colorOption" @change="handleColorChange">-->
<!--          <el-radio value="1" size="medium" border>Color 1</el-radio>-->
<!--          <el-radio value="2" size="medium" border>Color 2</el-radio>-->
<!--        </el-radio-group>-->
<!--      </div>-->

<!--      <div class="knob-radio-container" style="margin-top: 20px">-->
<!--        <div class="knob-control-container">-->
<!--          <knob-control-->
<!--            v-model="angleRange"-->
<!--            :min="0"-->
<!--            :max="360"-->
<!--            :step="1"-->
<!--            size="100"-->
<!--            stroke-width="5"-->
<!--            @change="handleAngleChange"-->
<!--          />-->
<!--          <div class="angle-labels">-->
<!--            <div class="angle-input">-->
<!--              <label>Start Angle:</label>-->
<!--              <el-input-number-->
<!--                v-model.number="angleRange[0]"-->
<!--                :min="0"-->
<!--                :max="360"-->
<!--                size="small"-->
<!--                class="input-narrow"-->
<!--                @change="validateAngle('start')"-->
<!--              />-->
<!--            </div>-->
<!--            <div class="angle-input">-->
<!--              <label>End Angle:</label>-->
<!--              <el-input-number-->
<!--                v-model.number="angleRange[1]"-->
<!--                :min="0"-->
<!--                :max="360"-->
<!--                size="small"-->
<!--                class="input-narrow"-->
<!--                @change="validateAngle('end')"-->
<!--              />-->
<!--            </div>-->
<!--          </div>-->
<!--          <el-button @click="applyAngleRange" class="confirm-button">Submit</el-button>-->
<!--        </div>-->
<!--        <el-radio-group v-model="radio" class="radio-group" @change="handleRadioChange">-->
<!--          <el-radio :value="'routes'">Routes</el-radio>-->
<!--          <el-radio :value="'directions'">Directions</el-radio>-->
<!--          <el-radio :value="'start'">Start</el-radio>-->
<!--        </el-radio-group>-->
<!--      </div>-->

<!--      <div class="slider-container">-->
<!--        <el-slider-->
<!--          v-model="lineWeight"-->
<!--          :min="3"-->
<!--          :max="10"-->
<!--          :show-stops="true"-->
<!--          label="Line Weight"-->
<!--          class="slider-short"-->
<!--        />-->
<!--        <div class="slider-labels">-->
<!--          <span>3</span>-->
<!--          <span>10</span>-->
<!--        </div>-->
<!--      </div>-->

<!--      <div class="category-menu">-->
<!--        <button-->
<!--          v-for="category in filteredCategories"-->
<!--          :key="category.label"-->
<!--          @click="selectCategory(category)"-->
<!--          :class="{ active: selectedCategory === category.label }"-->
<!--        >-->
<!--          {{ category.label }}-->
<!--        </button>-->
<!--      </div>-->
<!--      <div class="bus-list">-->
<!--        <button-->
<!--          v-for="bus in sortedBuses"-->
<!--          :key="bus"-->
<!--          @click="selectBus(bus)"-->
<!--          :class="{ 'bus-active': selectedBus === bus }"-->
<!--        >-->
<!--          {{ bus }}-->
<!--        </button>-->
<!--      </div>-->
<!--      <button @click="reset" class="reset-button">Reset</button>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { onMounted, ref, onBeforeUnmount, watch, computed, toRaw } from 'vue';-->
<!--import axios from 'axios';-->
<!--import L from 'leaflet';-->
<!--import 'leaflet/dist/leaflet.css';-->
<!--import { ElSwitch, ElSlider, ElRadio, ElRadioGroup, ElInputNumber, ElButton, ElMessage } from 'element-plus';-->
<!--import 'element-plus/dist/index.css';-->
<!--import KnobControl from './KnobControl.vue';-->
<!--import tabsData from '@/data/tabs_data.json';-->

<!--export default {-->
<!--  name: 'MapView',-->
<!--  components: {-->
<!--    ElSwitch,-->
<!--    ElSlider,-->
<!--    ElRadio,-->
<!--    ElRadioGroup,-->
<!--    ElInputNumber,-->
<!--    ElButton,-->
<!--    KnobControl,-->
<!--  },-->
<!--  setup() {-->
<!--    const colorMap8 = ["rgb(248,215,73)", "rgb(231,135,60)", "rgb(218,55,62)", "rgb(111,48,140)", "rgb(50,71,153)", "rgb(78,155,195)", "rgb(120,186,87)", "rgb(225,231,121)"];-->
<!--    const colorMap1 = ["#FF0D00", "#FF8900", "#FFB600", "#FFEE00", "#C9FF00", "#0DFF00", "#00FFF5", "#109CFF", "#186EFF", "#4B1FFF", "#9E10FF", "#FF0196"];-->
<!--    const colorMap360 = Array.from({ length: 360 }, (_, i) => `hsl(${i}, 90%, 50%)`);-->

<!--    const map = ref(null);-->
<!--    const backgroundSwitch = ref(false);-->
<!--    const viewSwitch = ref(false);-->
<!--    const lineWeight = ref(3);-->
<!--    const currentLayerGroup = ref(null);-->
<!--    const mapInitialized = ref(false);-->
<!--    const radio = ref('routes');-->
<!--    const use360Colors = ref(false);-->
<!--    const angleRange = ref([0, 360]);-->
<!--    const colorOption = ref('1');-->
<!--    const selectedBus = ref(null);-->

<!--    const categories = ref(tabsData.filter(category => category.numbers.length > 0));-->
<!--    const selectedCategory = ref(categories.value[0]?.label || '');-->
<!--    const selectedBuses = ref(categories.value[0]?.numbers || []);-->
<!--    const filteredCategories = ref(categories.value);-->
<!--    const sortedBuses = computed(() => {-->
<!--      return [...selectedBuses.value].sort((a, b) => a - b);-->
<!--    });-->

<!--    const initialState = {-->
<!--      backgroundSwitch: false,-->
<!--      viewSwitch: false,-->
<!--      lineWeight: 3,-->
<!--      selectedCategory: selectedCategory.value,-->
<!--      selectedBuses: selectedBuses.value,-->
<!--      center: [51.5074, -0.1278],-->
<!--      zoom: 12,-->
<!--    };-->

<!--    const reset = () => {-->
<!--      backgroundSwitch.value = initialState.backgroundSwitch;-->
<!--      viewSwitch.value = initialState.viewSwitch;-->
<!--      lineWeight.value = initialState.lineWeight;-->
<!--      selectedCategory.value = initialState.selectedCategory;-->
<!--      selectedBuses.value = initialState.selectedBuses;-->
<!--      selectedBus.value = null;-->
<!--      use360Colors.value = false;-->
<!--      clearMap();-->
<!--      fetchRoutes();-->
<!--      if (map.value) {-->
<!--        toRaw(map.value).setView(initialState.center, initialState.zoom);-->
<!--      }-->
<!--      console.log('State has been reset to initial values');-->
<!--    };-->

<!--    const selectCategory = (category) => {-->
<!--      selectedCategory.value = category.label;-->
<!--      selectedBuses.value = category.numbers;-->
<!--      console.log('Category selected:', selectedCategory.value, 'Buses:', selectedBuses.value);-->
<!--    };-->

<!--    const getColorByAngle = (angle) => {-->
<!--      if (use360Colors.value) {-->
<!--        return colorMap360[Math.round(angle) % 360];-->
<!--      } else if (colorOption.value === '1') {-->
<!--        const index = Math.floor(angle / 45) % 8;-->
<!--        return colorMap8[index];-->
<!--      } else {-->
<!--        const index = Math.floor(angle / 30) % 12;-->
<!--        return colorMap1[index];-->
<!--      }-->
<!--    };-->

<!--    const createArrowIcon = (angle, color) => {-->
<!--      return L.divIcon({-->
<!--        className: 'arrow-icon',-->
<!--        html: `-->
<!--          <div class="arrow-icon" style="transform: rotate(${angle}deg);">-->
<!--            <svg class="arrow-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">-->
<!--              <polygon points="50,0 15,100 85,100" fill="${color}" />-->
<!--            </svg>-->
<!--          </div>-->
<!--        `,-->
<!--        iconSize: [20, 20],-->
<!--        iconAnchor: [10, 10]-->
<!--      });-->
<!--    };-->

<!--    const selectBus = async (bus) => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      console.log(`Selected bus: ${bus}`);-->
<!--      selectedBus.value = bus;-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${bus}`);-->
<!--        console.log('Route data fetched:', response.data);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        clearMap();-->
<!--        const routeColor = getColorByAngle(routeData.angle);-->
<!--        const polyline = L.polyline(points, { color: routeColor, weight: lineWeight.value, opacity: 0.8 }).addTo(toRaw(currentLayerGroup.value));-->

<!--        points.forEach((point, index) => {-->
<!--          const marker = L.circleMarker(point, {-->
<!--            radius: 5,-->
<!--            color: 'white',-->
<!--            weight: 1,-->
<!--            fill: true,-->
<!--            fillColor: routeColor,-->
<!--            fillOpacity: 1-->
<!--          });-->
<!--          marker.bindTooltip(routeData.points[index].Stop_Name, { permanent: false, direction: 'top' });-->
<!--          marker.on('mouseover', function () {-->
<!--            this.openTooltip();-->
<!--          });-->
<!--          marker.on('mouseout', function () {-->
<!--            this.closeTooltip();-->
<!--          });-->
<!--          marker.addTo(toRaw(currentLayerGroup.value));-->
<!--        });-->

<!--        const startPoint = routeData.points[0];-->
<!--        const arrowIcon = createArrowIcon(routeData.angle, routeColor);-->
<!--        L.marker([startPoint.Latitude, startPoint.Longitude], { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->

<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--        toRaw(map.value).fitBounds(polyline.getBounds());-->
<!--        console.log('Route rendered successfully');-->

<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${bus}:`, error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRoutes = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1]-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->
<!--        const routePromises = routes.map(route => fetchRouteData(route));-->
<!--        const routeData = await Promise.all(routePromises);-->
<!--        initializeMapWithRoutes(routeData.filter(route => route !== null));-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching routes:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRouteData = async (route) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        return {-->
<!--          routeId: routeData.route_id,-->
<!--          points,-->
<!--          angle: routeData.angle-->
<!--        };-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${route}:`, error);-->
<!--        return null;-->
<!--      }-->
<!--    };-->

<!--    const fetchAllStations = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1]-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->
<!--        const stationPromises = routes.map(route => fetchStationData(route));-->
<!--        const allStations = (await Promise.all(stationPromises)).flat();-->
<!--        initializeMapWithStations(allStations);-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching all stations data:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchStationData = async (routeId) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = response.data;-->
<!--        return routeData.points.map(point => ({-->
<!--          Latitude: point.Latitude,-->
<!--          Longitude: point.Longitude,-->
<!--          Stop_Name: point.Stop_Name-->
<!--        }));-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching station data for ${routeId}:`, error);-->
<!--        return [];-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithRoutes = (routes) => {-->
<!--      clearMap();-->
<!--      routes.forEach((route) => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const routeColor = getColorByAngle(route.angle);-->
<!--          L.polyline(route.points, { color: routeColor, weight: lineWeight.value, opacity: 0.7 }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithStations = (stations) => {-->
<!--      clearMap();-->
<!--      stations.forEach(station => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const marker = L.circleMarker([station.Latitude, station.Longitude], {-->
<!--            radius: 5,-->
<!--            color: 'white',-->
<!--            weight: 1,-->
<!--            fill: true,-->
<!--            fillColor: '#BC403A',-->
<!--            fillOpacity: 1-->
<!--          });-->

<!--          marker.bindTooltip(station.Stop_Name, { permanent: false, direction: 'top' });-->
<!--          marker.on('mouseover', function () {-->
<!--            this.openTooltip();-->
<!--          });-->
<!--          marker.on('mouseout', function () {-->
<!--            this.closeTooltip();-->
<!--          });-->

<!--          marker.addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithStartPoints = (routes) => {-->
<!--      clearMap();-->
<!--      routes.forEach(route => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const routeColor = getColorByAngle(route.angle);-->
<!--          const startPoint = route.points[0];-->
<!--          const arrowIcon = createArrowIcon(route.angle, routeColor);-->
<!--          L.marker(startPoint, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const clearMap = () => {-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).clearLayers();-->
<!--      }-->
<!--    };-->

<!--    const updateMapLayer = () => {-->
<!--      if (map.value) {-->
<!--        const tileLayerUrl = backgroundSwitch.value-->
<!--          ? 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'-->
<!--          : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';-->

<!--        L.tileLayer(tileLayerUrl, {-->
<!--          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',-->
<!--          maxZoom: 19-->
<!--        }).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const toggleBackground = () => {-->
<!--      updateMapLayer();-->
<!--    };-->

<!--    const toggleView = () => {-->
<!--      if (viewSwitch.value) {-->
<!--        fetchAllStations();-->
<!--      } else {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    const handleRadioChange = async (value) => {-->
<!--      if (value === 'directions') {-->
<!--        use360Colors.value = true;-->
<!--        await fetchDirections();-->
<!--      } else if (value === 'start') {-->
<!--        use360Colors.value = true;-->
<!--        await fetchStartPoints();-->
<!--      } else {-->
<!--        use360Colors.value = false;-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    const fetchDirections = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1]-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->

<!--        clearMap();-->

<!--        for (const route of routes) {-->
<!--          const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);-->
<!--          const routeData = routeResponse.data;-->

<!--          const start = [routeData.points[0].Latitude, routeData.points[0].Longitude];-->
<!--          const end = [routeData.points[routeData.points.length - 1].Latitude, routeData.points[routeData.points.length - 1].Longitude];-->
<!--          const angle = routeData.angle;-->
<!--          const routeColor = getColorByAngle(angle);-->

<!--          L.polyline([start, end], { color: routeColor, weight: lineWeight.value, opacity: 0.6 }).addTo(toRaw(currentLayerGroup.value));-->

<!--          const arrowIcon = createArrowIcon(angle, routeColor);-->
<!--          L.marker(start, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->

<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--        console.log('Directions rendered successfully');-->

<!--      } catch (error) {-->
<!--        console.error('Error fetching directions:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchStartPoints = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1]-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->

<!--        clearMap();-->

<!--        const routePromises = routes.map(route => fetchRouteData(route));-->
<!--        const routeData = await Promise.all(routePromises);-->

<!--        initializeMapWithStartPoints(routeData.filter(route => route !== null));-->

<!--        console.log('Start points rendered successfully');-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching start points:', error);-->
<!--      }-->
<!--    };-->

<!--    const handleAngleChange = () => {-->
<!--      if (viewSwitch.value) {-->
<!--        fetchAllStations();-->
<!--      } else if (radio.value === 'directions') {-->
<!--        fetchDirections();-->
<!--      } else if (radio.value === 'start') {-->
<!--        fetchStartPoints();-->
<!--      } else {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    const handleColorChange = () => {-->
<!--      if (!viewSwitch.value) {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    const validateAngle = (type) => {-->
<!--      if (type === 'start' && angleRange.value[0] > 360) {-->
<!--        ElMessage.error('Start point cannot be greater than 360');-->
<!--        angleRange.value[0] = 360;-->
<!--      } else if (type === 'end' && angleRange.value[1] > 360) {-->
<!--        ElMessage.error('End point cannot be greater than 360');-->
<!--        angleRange.value[1] = 360;-->
<!--      }-->
<!--    };-->

<!--    const applyAngleRange = () => {-->
<!--      if (viewSwitch.value) {-->
<!--        fetchAllStations();-->
<!--      } else if (radio.value === 'directions') {-->
<!--        fetchDirections();-->
<!--      } else if (radio.value === 'start') {-->
<!--        fetchStartPoints();-->
<!--      } else {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    watch(lineWeight, () => {-->
<!--      if (!viewSwitch.value) {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    });-->

<!--    onMounted(() => {-->
<!--      L.Popup.prototype._animateZoom = function (e) {-->
<!--        if (!this._map) {-->
<!--          return;-->
<!--        }-->
<!--        var pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),-->
<!--            anchor = this._getAnchor();-->
<!--        L.DomUtil.setPosition(this._container, pos.add(anchor));-->
<!--      };-->

<!--      map.value = L.map('map').setView(initialState.center, initialState.zoom);-->
<!--      currentLayerGroup.value = L.layerGroup().addTo(toRaw(map.value));-->
<!--      mapInitialized.value = true;-->
<!--      updateMapLayer();-->
<!--      fetchRoutes();-->
<!--    });-->

<!--    onBeforeUnmount(() => {-->
<!--      mapInitialized.value = false;-->
<!--      if (map.value) {-->
<!--        toRaw(map.value).remove();-->
<!--        map.value = null;-->
<!--      }-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).clearLayers();-->
<!--        currentLayerGroup.value = null;-->
<!--      }-->
<!--    });-->

<!--    return {-->
<!--      backgroundSwitch,-->
<!--      viewSwitch,-->
<!--      lineWeight,-->
<!--      toggleBackground,-->
<!--      toggleView,-->
<!--      categories,-->
<!--      filteredCategories,-->
<!--      selectedCategory,-->
<!--      selectedBuses,-->
<!--      sortedBuses,-->
<!--      selectCategory,-->
<!--      selectBus,-->
<!--      reset,-->
<!--      radio,-->
<!--      handleRadioChange,-->
<!--      angleRange,-->
<!--      handleAngleChange,-->
<!--      colorOption,-->
<!--      handleColorChange,-->
<!--      validateAngle,-->
<!--      applyAngleRange,-->
<!--      selectedBus-->
<!--    };-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--#container {-->
<!--  display: flex;-->
<!--  height: 100vh;-->
<!--}-->

<!--#map {-->
<!--  flex-grow: 1;-->
<!--}-->

<!--#navbar {-->
<!--  width: 350px;-->
<!--  background-color: white;-->
<!--  border-left: 1px solid #ccc;-->
<!--  padding: 10px;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  justify-content: flex-start;-->
<!--  align-items: center;-->
<!--  overflow-y: auto;-->
<!--}-->

<!--.switch-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--  justify-content: center;-->
<!--  margin-bottom: 10px;-->
<!--  width: 100%;-->
<!--}-->

<!--.switch-row {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--  width: 100%;-->
<!--}-->

<!--.switch-item {-->
<!--  margin-bottom: 10px;-->
<!--}-->

<!--.knob-radio-container {-->
<!--  border: 3px solid #5a9cf8;-->
<!--  border-radius: 10px;-->
<!--  padding: 10px;-->
<!--  margin-bottom: 10px;-->
<!--  width: 90%;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--}-->

<!--.knob-control-container {-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  justify-content: center;-->
<!--  margin-bottom: 10px;-->
<!--  width: 100%;-->
<!--}-->

<!--.angle-labels {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: flex-start;-->
<!--  justify-content: center;-->
<!--  margin-left: 20px;-->
<!--}-->

<!--.angle-labels span {-->
<!--  font-size: 0.8em;-->
<!--  margin-bottom: 5px;-->
<!--}-->

<!--.angle-input {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: flex-start;-->
<!--  font-size: 0.8em;-->
<!--  margin-bottom: 5px;-->
<!--}-->

<!--.input-narrow .el-input-number {-->
<!--  width: 80px;-->
<!--}-->

<!--.confirm-button {-->
<!--  margin-top: 10px;-->
<!--  margin-left: 10px; /* 增加左边距，使按钮离左边的输入框远一点 */-->
<!--  padding: 5px 10px; /* 调整内边距，使按钮更小 */-->
<!--  font-size: 12px; /* 调整字体大小 */-->
<!--  border-radius: 5px; /* 调整圆角半径 */-->
<!--}-->

<!--.el-input-number&#45;&#45;small .el-input__inner {-->
<!--  height: 22px;-->
<!--  padding: 0 7px;-->
<!--}-->

<!--.radio-group {-->
<!--  margin-bottom: 10px;-->
<!--}-->

<!--.slider-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--  margin-top: 10px;-->
<!--}-->

<!--.slider-short {-->
<!--  width: 150px;-->
<!--}-->

<!--.slider-labels {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--  width: 100%;-->
<!--  padding: 0 20px;-->
<!--}-->

<!--.slider-label {-->
<!--  font-size: 0.8em;-->
<!--}-->

<!--.category-menu {-->
<!--  display: grid;-->
<!--  grid-template-columns: repeat(3, 1fr);-->
<!--  gap: 10px;-->
<!--  margin-top: 20px;-->
<!--  font-size: 0.9em;-->
<!--}-->

<!--.category-menu button {-->
<!--  padding: 10px;-->
<!--  border: none;-->
<!--  background-color: #eee;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  border-radius: 10px;-->
<!--}-->

<!--.category-menu button.active {-->
<!--  background-color: #333;-->
<!--  color: white;-->
<!--}-->

<!--.bus-list {-->
<!--  display: grid;-->
<!--  grid-template-columns: repeat(5, 1fr);-->
<!--  gap: 10px;-->
<!--  margin-top: 20px;-->
<!--  width: 100%;-->
<!--  font-size: 0.9em;-->
<!--}-->

<!--.bus-list button {-->
<!--  height: 40px;-->
<!--  border: none;-->
<!--  background-color: #f0f8ff;-->
<!--  color: #0000ee;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  line-height: 40px;-->
<!--  border-radius: 5px;-->
<!--}-->

<!--.bus-list button.bus-active {-->
<!--  border: 2px solid blue; /* 蓝色的框 */-->
<!--  font-weight: bold; /* 字体加粗 */-->
<!--}-->

<!--.reset-button {-->
<!--  margin-top: 20px;-->
<!--  padding: 10px 20px;-->
<!--  border: none;-->
<!--  background-color: #ff6347;-->
<!--  color: white;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  border-radius: 5px;-->
<!--}-->

<!--.arrow-icon {-->
<!--  display: flex;-->
<!--  justify-content: center;-->
<!--  align-items: center;-->
<!--  transform-origin: center;-->
<!--}-->

<!--.arrow-svg {-->
<!--  width: 20px;-->
<!--  height: 20px;-->
<!--}-->
<!--</style>-->





<!--<template>-->
<!--  <div id="container">-->
<!--    <div id="map"></div>-->
<!--    <div id="navbar">-->
<!--      <div class="menu-bar">-->
<!--        <button @click="selectMenu('routes')" :class="{ active: activeMenu === 'routes' }">Routes</button>-->
<!--        <button @click="selectMenu('passengerFlow')" :class="{ active: activeMenu === 'passengerFlow' }">Passenger Flow</button>-->
<!--      </div>-->
<!--      <div class="switch-container">-->
<!--        <div class="switch-row">-->
<!--          <el-switch-->
<!--            v-model="backgroundSwitch"-->
<!--            size="medium"-->
<!--            active-text="Color"-->
<!--            inactive-text="Grey"-->
<!--            @change="toggleBackground"-->
<!--            class="switch-item"-->
<!--          />-->
<!--          <el-switch-->
<!--            v-model="viewSwitch"-->
<!--            size="medium"-->
<!--            active-text="Stations"-->
<!--            inactive-text="Routes"-->
<!--            @change="toggleView"-->
<!--            class="switch-item"-->
<!--          />-->
<!--        </div>-->
<!--      </div>-->

<!--      <div style="margin-top: 0px">-->
<!--        <el-radio-group v-model="colorOption" @change="handleColorChange">-->
<!--          <el-radio value="1" size="medium" border>Color 1</el-radio>-->
<!--          <el-radio value="2" size="medium" border>Color 2</el-radio>-->
<!--        </el-radio-group>-->
<!--      </div>-->

<!--      <div class="knob-radio-container" style="margin-top: 20px">-->
<!--        <div class="knob-control-container">-->
<!--          <knob-control-->
<!--            v-model="angleRange"-->
<!--            :min="0"-->
<!--            :max="360"-->
<!--            :step="1"-->
<!--            size="100"-->
<!--            stroke-width="5"-->
<!--            @change="handleAngleChange"-->
<!--          />-->
<!--          <div class="angle-labels">-->
<!--            <div class="angle-input">-->
<!--              <label>Start Angle:</label>-->
<!--              <el-input-number-->
<!--                v-model.number="angleRange[0]"-->
<!--                :min="0"-->
<!--                :max="360"-->
<!--                size="small"-->
<!--                class="input-narrow"-->
<!--                @change="validateAngle('start')"-->
<!--              />-->
<!--            </div>-->
<!--            <div class="angle-input">-->
<!--              <label>End Angle:</label>-->
<!--              <el-input-number-->
<!--                v-model.number="angleRange[1]"-->
<!--                :min="0"-->
<!--                :max="360"-->
<!--                size="small"-->
<!--                class="input-narrow"-->
<!--                @change="validateAngle('end')"-->
<!--              />-->
<!--            </div>-->
<!--          </div>-->
<!--          <el-button @click="applyAngleRange" class="confirm-button">Submit</el-button>-->
<!--        </div>-->
<!--        <el-radio-group v-model="radio" class="radio-group" @change="handleRadioChange">-->
<!--          <el-radio :value="'routes'">Routes</el-radio>-->
<!--          <el-radio :value="'directions'">Directions</el-radio>-->
<!--          <el-radio :value="'start'">Start</el-radio>-->
<!--        </el-radio-group>-->
<!--      </div>-->

<!--      <div class="slider-container">-->
<!--        <el-slider-->
<!--          v-model="lineWeight"-->
<!--          :min="3"-->
<!--          :max="10"-->
<!--          :show-stops="true"-->
<!--          label="Line Weight"-->
<!--          class="slider-short"-->
<!--          @change="applyAngleRange"-->
<!--        />-->
<!--        <div class="slider-labels">-->
<!--          <span>3</span>-->
<!--          <span>10</span>-->
<!--        </div>-->
<!--      </div>-->

<!--      <div class="category-menu">-->
<!--        <button-->
<!--          v-for="category in filteredCategories"-->
<!--          :key="category.label"-->
<!--          @click="selectCategory(category)"-->
<!--          :class="{ active: selectedCategory === category.label }"-->
<!--        >-->
<!--          {{ category.label }}-->
<!--        </button>-->
<!--      </div>-->
<!--      <div class="bus-list">-->
<!--        <button-->
<!--          v-for="bus in sortedBuses"-->
<!--          :key="bus"-->
<!--          @click="selectBus(bus)"-->
<!--          :class="{ 'bus-active': selectedBus === bus }"-->
<!--        >-->
<!--          {{ bus }}-->
<!--        </button>-->
<!--      </div>-->
<!--      <button @click="reset" class="reset-button">Reset</button>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { onMounted, ref, onBeforeUnmount, watch, computed, toRaw } from 'vue';-->
<!--import axios from 'axios';-->
<!--import L from 'leaflet';-->
<!--import 'leaflet/dist/leaflet.css';-->
<!--import { ElSwitch, ElSlider, ElRadio, ElRadioGroup, ElInputNumber, ElButton, ElMessage } from 'element-plus';-->
<!--import 'element-plus/dist/index.css';-->
<!--import KnobControl from './KnobControl.vue';-->
<!--import tabsData from '@/data/tabs_data.json';-->

<!--export default {-->
<!--  name: 'MapView',-->
<!--  components: {-->
<!--    ElSwitch,-->
<!--    ElSlider,-->
<!--    ElRadio,-->
<!--    ElRadioGroup,-->
<!--    ElInputNumber,-->
<!--    ElButton,-->
<!--    KnobControl,-->
<!--  },-->
<!--  setup() {-->
<!--    const colorMap8 = ["rgb(248,215,73)", "rgb(231,135,60)", "rgb(218,55,62)", "rgb(111,48,140)", "rgb(50,71,153)", "rgb(78,155,195)", "rgb(120,186,87)", "rgb(225,231,121)"];-->
<!--    const colorMap1 = ["#FF0D00", "#FF8900", "#FFB600", "#FFEE00", "#C9FF00", "#0DFF00", "#00FFF5", "#109CFF", "#186EFF", "#4B1FFF", "#9E10FF", "#FF0196"];-->
<!--    const colorMap360 = Array.from({ length: 360 }, (_, i) => `hsl(${i}, 90%, 50%)`);-->

<!--    const map = ref(null);-->
<!--    const backgroundSwitch = ref(false);-->
<!--    const viewSwitch = ref(false);-->
<!--    const lineWeight = ref(3);-->
<!--    const currentLayerGroup = ref(null);-->
<!--    const mapInitialized = ref(false);-->
<!--    const radio = ref('routes');-->
<!--    const use360Colors = ref(false);-->
<!--    const angleRange = ref([0, 360]);-->
<!--    const colorOption = ref('1');-->
<!--    const selectedBus = ref(null);-->
<!--    const activeMenu = ref('routes');-->

<!--    const categories = ref(tabsData.filter(category => category.numbers.length > 0));-->
<!--    const selectedCategory = ref(categories.value[0]?.label || '');-->
<!--    const selectedBuses = ref(categories.value[0]?.numbers || []);-->
<!--    const filteredCategories = ref(categories.value);-->
<!--    const sortedBuses = computed(() => {-->
<!--      return [...selectedBuses.value].sort((a, b) => a - b);-->
<!--    });-->

<!--    const initialState = {-->
<!--      backgroundSwitch: false,-->
<!--      viewSwitch: false,-->
<!--      lineWeight: 3,-->
<!--      selectedCategory: selectedCategory.value,-->
<!--      selectedBuses: selectedBuses.value,-->
<!--      center: [51.5074, -0.1278],-->
<!--      zoom: 12,-->
<!--    };-->

<!--    const reset = () => {-->
<!--      backgroundSwitch.value = initialState.backgroundSwitch;-->
<!--      viewSwitch.value = initialState.viewSwitch;-->
<!--      lineWeight.value = initialState.lineWeight;-->
<!--      selectedCategory.value = initialState.selectedCategory;-->
<!--      selectedBuses.value = initialState.selectedBuses;-->
<!--      selectedBus.value = null;-->
<!--      use360Colors.value = false;-->
<!--      clearMap();-->
<!--      fetchRoutes();-->
<!--      if (map.value) {-->
<!--        toRaw(map.value).setView(initialState.center, initialState.zoom);-->
<!--      }-->
<!--      console.log('State has been reset to initial values');-->
<!--    };-->

<!--    const selectCategory = (category) => {-->
<!--      selectedCategory.value = category.label;-->
<!--      selectedBuses.value = category.numbers;-->
<!--      console.log('Category selected:', selectedCategory.value, 'Buses:', selectedBuses.value);-->
<!--    };-->

<!--    const getColorByAngle = (angle) => {-->
<!--      if (use360Colors.value) {-->
<!--        return colorMap360[Math.round(angle) % 360];-->
<!--      } else if (colorOption.value === '1') {-->
<!--        const index = Math.floor(angle / 45) % 8;-->
<!--        return colorMap8[index];-->
<!--      } else {-->
<!--        const index = Math.floor(angle / 30) % 12;-->
<!--        return colorMap1[index];-->
<!--      }-->
<!--    };-->

<!--    const getRouteColor = (angle) => {-->
<!--      if (angleRange.value[0] <= angleRange.value[1]) {-->
<!--        return angle >= angleRange.value[0] && angle <= angleRange.value[1]-->
<!--          ? getColorByAngle(angle)-->
<!--          : 'lightgray';-->
<!--      } else {-->
<!--        return (angle >= angleRange.value[0] || angle <= angleRange.value[1])-->
<!--          ? getColorByAngle(angle)-->
<!--          : 'lightgray';-->
<!--      }-->
<!--    };-->

<!--    const createArrowIcon = (angle, color) => {-->
<!--      return L.divIcon({-->
<!--        className: 'arrow-icon',-->
<!--        html: `-->
<!--          <div class="arrow-icon" style="transform: rotate(${angle}deg);">-->
<!--            <svg class="arrow-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">-->
<!--              <polygon points="50,0 15,100 85,100" fill="${color}" />-->
<!--            </svg>-->
<!--          </div>-->
<!--        `,-->
<!--        iconSize: [20, 20],-->
<!--        iconAnchor: [10, 10]-->
<!--      });-->
<!--    };-->

<!--    const selectBus = async (bus) => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      console.log(`Selected bus: ${bus}`);-->
<!--      selectedBus.value = bus;-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${bus}`);-->
<!--        console.log('Route data fetched:', response.data);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        clearMap();-->

<!--        // Draw grey route-->
<!--        L.polyline(points, { color: 'lightgray', weight: lineWeight.value, opacity: 0.5 }).addTo(toRaw(currentLayerGroup.value));-->

<!--        // Draw colored route on top if within angle range-->
<!--        const routeColor = getRouteColor(routeData.angle);-->
<!--        const polyline = L.polyline(points, { color: routeColor, weight: lineWeight.value, opacity: 0.8 }).addTo(toRaw(currentLayerGroup.value));-->

<!--        points.forEach((point, index) => {-->
<!--          const marker = L.circleMarker(point, {-->
<!--            radius: 5,-->
<!--            color: 'white',-->
<!--            weight: 1,-->
<!--            fill: true,-->
<!--            fillColor: routeColor,-->
<!--            fillOpacity: 1-->
<!--          });-->
<!--          marker.bindTooltip(routeData.points[index].Stop_Name, { permanent: false, direction: 'top' });-->
<!--          marker.on('mouseover', function () {-->
<!--            this.openTooltip();-->
<!--          });-->
<!--          marker.on('mouseout', function () {-->
<!--            this.closeTooltip();-->
<!--          });-->
<!--          marker.addTo(toRaw(currentLayerGroup.value));-->
<!--        });-->

<!--        const startPoint = routeData.points[0];-->
<!--        const arrowIcon = createArrowIcon(routeData.angle, routeColor);-->
<!--        L.marker([startPoint.Latitude, startPoint.Longitude], { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->

<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--        toRaw(map.value).fitBounds(polyline.getBounds());-->
<!--        console.log('Route rendered successfully');-->

<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${bus}:`, error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRoutes = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: 0,-->
<!--            max_angle: 360-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->
<!--        const routePromises = routes.map(route => fetchRouteData(route));-->
<!--        const routeData = await Promise.all(routePromises);-->
<!--        initializeMapWithRoutes(routeData.filter(route => route !== null));-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching routes:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRouteData = async (route) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        return {-->
<!--          routeId: routeData.route_id,-->
<!--          points,-->
<!--          angle: routeData.angle-->
<!--        };-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${route}:`, error);-->
<!--        return null;-->
<!--      }-->
<!--    };-->

<!--    const fetchAllStations = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: 0,-->
<!--            max_angle: 360-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->
<!--        const stationPromises = routes.map(route => fetchStationData(route));-->
<!--        const allStations = (await Promise.all(stationPromises)).flat();-->
<!--        initializeMapWithStations(allStations);-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching all stations data:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchStationData = async (routeId) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = response.data;-->
<!--        return routeData.points.map(point => ({-->
<!--          Latitude: point.Latitude,-->
<!--          Longitude: point.Longitude,-->
<!--          Stop_Name: point.Stop_Name-->
<!--        }));-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching station data for ${routeId}:`, error);-->
<!--        return [];-->
<!--      }-->
<!--    };-->

<!--    const fetchPassengerFlowRoutes = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1]-->
<!--          }-->
<!--        });-->
<!--        const passengerFlowRoutes = response.data;-->
<!--        const routePromises = passengerFlowRoutes.map(route => fetchRouteDataWithPassengerFlow(route.route_id, route.usage_recorded));-->
<!--        const routeData = await Promise.all(routePromises);-->
<!--        initializeMapWithPassengerFlowRoutes(routeData.filter(route => route !== null));-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching passenger flow routes:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRouteDataWithPassengerFlow = async (routeId, usageRecorded) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        const weight = getLineWeight(usageRecorded);-->
<!--        return {-->
<!--          routeId: routeData.route_id,-->
<!--          points,-->
<!--          angle: routeData.angle,-->
<!--          weight-->
<!--        };-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${routeId}:`, error);-->
<!--        return null;-->
<!--      }-->
<!--    };-->

<!--    const getLineWeight = (usageRecorded) => {-->
<!--      if (usageRecorded <= 629233.75) {-->
<!--        return 3;-->
<!--      } else if (usageRecorded <= 2048661.50) {-->
<!--        return 4.5;-->
<!--      } else if (usageRecorded <= 4042106.50) {-->
<!--        return 6;-->
<!--      } else {-->
<!--        return 7.5;-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithRoutes = (routes) => {-->
<!--      clearMap();-->
<!--      // First draw grey routes-->
<!--      routes.forEach((route) => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          L.polyline(route.points, { color: 'lightgray', weight: lineWeight.value, opacity: 0.5 }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      // Then draw colored routes-->
<!--      routes.forEach((route) => {-->
<!--        if (currentLayerGroup.value && (angleRange.value[0] <= angleRange.value[1]-->
<!--          ? route.angle >= angleRange.value[0] && route.angle <= angleRange.value[1]-->
<!--          : route.angle >= angleRange.value[0] || route.angle <= angleRange.value[1])) {-->
<!--          const routeColor = getColorByAngle(route.angle);-->
<!--          L.polyline(route.points, { color: routeColor, weight: lineWeight.value, opacity: 0.7 }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithPassengerFlowRoutes = (routes) => {-->
<!--      clearMap();-->
<!--      routes.forEach((route) => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const routeColor = getColorByAngle(route.angle);-->
<!--          L.polyline(route.points, { color: routeColor, weight: route.weight, opacity: 0.9 }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithStations = (stations) => {-->
<!--      clearMap();-->
<!--      stations.forEach(station => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const marker = L.circleMarker([station.Latitude, station.Longitude], {-->
<!--            radius: 5,-->
<!--            color: 'white',-->
<!--            weight: 1,-->
<!--            fill: true,-->
<!--            fillColor: '#BC403A',-->
<!--            fillOpacity: 1-->
<!--          });-->

<!--          marker.bindTooltip(station.Stop_Name, { permanent: false, direction: 'top' });-->
<!--          marker.on('mouseover', function () {-->
<!--            this.openTooltip();-->
<!--          });-->
<!--          marker.on('mouseout', function () {-->
<!--            this.closeTooltip();-->
<!--          });-->

<!--          marker.addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const initializeMapWithStartPoints = (routes) => {-->
<!--      clearMap();-->
<!--      routes.forEach(route => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const routeColor = getColorByAngle(route.angle);-->
<!--          const startPoint = route.points[0];-->
<!--          const arrowIcon = createArrowIcon(route.angle, routeColor);-->
<!--          L.marker(startPoint, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const clearMap = () => {-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).clearLayers();-->
<!--      }-->
<!--    };-->

<!--    const updateMapLayer = () => {-->
<!--      if (map.value) {-->
<!--        const tileLayerUrl = backgroundSwitch.value-->
<!--          ? 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png'-->
<!--          : 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';-->

<!--        L.tileLayer(tileLayerUrl, {-->
<!--          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',-->
<!--          maxZoom: 19-->
<!--        }).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const toggleBackground = () => {-->
<!--      updateMapLayer();-->
<!--    };-->

<!--    const toggleView = () => {-->
<!--      if (viewSwitch.value) {-->
<!--        fetchAllStations();-->
<!--      } else {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    const handleRadioChange = async (value) => {-->
<!--      if (value === 'directions') {-->
<!--        use360Colors.value = true;-->
<!--        await fetchDirections();-->
<!--      } else if (value === 'start') {-->
<!--        use360Colors.value = true;-->
<!--        await fetchStartPoints();-->
<!--      } else {-->
<!--        use360Colors.value = false;-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    const fetchDirections = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1]-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->

<!--        clearMap();-->

<!--        for (const route of routes) {-->
<!--          const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${route}`);-->
<!--          const routeData = routeResponse.data;-->

<!--          const start = [routeData.points[0].Latitude, routeData.points[0].Longitude];-->
<!--          const end = [routeData.points[routeData.points.length - 1].Latitude, routeData.points[routeData.points.length - 1].Longitude];-->
<!--          const angle = routeData.angle;-->
<!--          const routeColor = getColorByAngle(angle);-->

<!--          L.polyline([start, end], { color: routeColor, weight: lineWeight.value, opacity: 0.6 }).addTo(toRaw(currentLayerGroup.value));-->

<!--          const arrowIcon = createArrowIcon(angle, routeColor);-->
<!--          L.marker(start, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->
<!--        }-->

<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--        console.log('Directions rendered successfully');-->

<!--      } catch (error) {-->
<!--        console.error('Error fetching directions:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchStartPoints = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->

<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/routes', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1]-->
<!--          }-->
<!--        });-->
<!--        const routes = response.data;-->

<!--        clearMap();-->

<!--        const routePromises = routes.map(route => fetchRouteData(route));-->
<!--        const routeData = await Promise.all(routePromises);-->

<!--        initializeMapWithStartPoints(routeData.filter(route => route !== null));-->

<!--        console.log('Start points rendered successfully');-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching start points:', error);-->
<!--      }-->
<!--    };-->

<!--    const handleAngleChange = () => {-->
<!--      applyAngleRange();-->
<!--    };-->

<!--    const handleColorChange = () => {-->
<!--      applyAngleRange();-->
<!--    };-->

<!--    const validateAngle = (type) => {-->
<!--      if (type === 'start' && angleRange.value[0] > 360) {-->
<!--        ElMessage.error('Start point cannot be greater than 360');-->
<!--        angleRange.value[0] = 360;-->
<!--      } else if (type === 'end' && angleRange.value[1] > 360) {-->
<!--        ElMessage.error('End point cannot be greater than 360');-->
<!--        angleRange.value[1] = 360;-->
<!--      }-->
<!--    };-->

<!--    const applyAngleRange = () => {-->
<!--      if (activeMenu.value === 'passengerFlow') {-->
<!--        fetchPassengerFlowRoutes();-->
<!--      } else if (viewSwitch.value) {-->
<!--        fetchAllStations();-->
<!--      } else if (radio.value === 'directions') {-->
<!--        fetchDirections();-->
<!--      } else if (radio.value === 'start') {-->
<!--        fetchStartPoints();-->
<!--      } else {-->
<!--        fetchRoutes();-->
<!--      }-->
<!--    };-->

<!--    const selectMenu = (menu) => {-->
<!--      activeMenu.value = menu;-->
<!--      console.log(`Selected menu: ${menu}`);-->
<!--      applyAngleRange();-->
<!--    };-->

<!--    watch(lineWeight, () => {-->
<!--      applyAngleRange();-->
<!--    });-->

<!--    watch(backgroundSwitch, () => {-->
<!--      updateMapLayer();-->
<!--    });-->

<!--    onMounted(() => {-->
<!--      L.Popup.prototype._animateZoom = function (e) {-->
<!--        if (!this._map) {-->
<!--          return;-->
<!--        }-->
<!--        var pos = this._map._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),-->
<!--            anchor = this._getAnchor();-->
<!--        L.DomUtil.setPosition(this._container, pos.add(anchor));-->
<!--      };-->

<!--      map.value = L.map('map').setView(initialState.center, initialState.zoom);-->
<!--      currentLayerGroup.value = L.layerGroup().addTo(toRaw(map.value));-->
<!--      mapInitialized.value = true;-->
<!--      updateMapLayer();-->
<!--      fetchRoutes();-->
<!--    });-->

<!--    onBeforeUnmount(() => {-->
<!--      mapInitialized.value = false;-->
<!--      if (map.value) {-->
<!--        toRaw(map.value).remove();-->
<!--        map.value = null;-->
<!--      }-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).clearLayers();-->
<!--        currentLayerGroup.value = null;-->
<!--      }-->
<!--    });-->

<!--    return {-->
<!--      backgroundSwitch,-->
<!--      viewSwitch,-->
<!--      lineWeight,-->
<!--      toggleBackground,-->
<!--      toggleView,-->
<!--      categories,-->
<!--      filteredCategories,-->
<!--      selectedCategory,-->
<!--      selectedBuses,-->
<!--      sortedBuses,-->
<!--      selectCategory,-->
<!--      selectBus,-->
<!--      reset,-->
<!--      radio,-->
<!--      handleRadioChange,-->
<!--      angleRange,-->
<!--      handleAngleChange,-->
<!--      colorOption,-->
<!--      handleColorChange,-->
<!--      validateAngle,-->
<!--      applyAngleRange,-->
<!--      selectedBus,-->
<!--      activeMenu,-->
<!--      selectMenu,-->
<!--    };-->
<!--  }-->
<!--};-->
<!--</script>-->

<!--<style scoped>-->
<!--#container {-->
<!--  display: flex;-->
<!--  height: 100vh;-->
<!--}-->

<!--#map {-->
<!--  flex-grow: 1;-->
<!--}-->

<!--#navbar {-->
<!--  width: 350px;-->
<!--  background-color: white;-->
<!--  border-left: 1px solid #ccc;-->
<!--  padding: 10px;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  justify-content: flex-start;-->
<!--  align-items: center;-->
<!--  overflow-y: auto;-->
<!--}-->

<!--.menu-bar {-->
<!--  width: 100%;-->
<!--  display: flex;-->
<!--  justify-content: space-around;-->
<!--  background-color: #ffffff;-->
<!--  padding: 10px 0;-->
<!--  margin-bottom: 10px;-->
<!--}-->

<!--.menu-bar button {-->
<!--  width: 45%;-->
<!--  border: none;-->
<!--  background-color: #d9e6fc;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  padding: 10px 0;-->
<!--  border-radius: 5px;-->
<!--  font-size: 16px;-->
<!--}-->

<!--.menu-bar button.active {-->
<!--  background-color: #5a9cf8;-->
<!--  color: white;-->
<!--}-->

<!--.switch-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--  justify-content: center;-->
<!--  margin-bottom: 10px;-->
<!--  width: 100%;-->
<!--}-->

<!--.switch-row {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--  width: 100%;-->
<!--}-->

<!--.switch-item {-->
<!--  margin-bottom: 10px;-->
<!--}-->

<!--.knob-radio-container {-->
<!--  border: 3px solid #5a9cf8;-->
<!--  border-radius: 10px;-->
<!--  padding: 10px;-->
<!--  margin-bottom: 10px;-->
<!--  width: 90%;-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--}-->

<!--.knob-control-container {-->
<!--  display: flex;-->
<!--  align-items: center;-->
<!--  justify-content: center;-->
<!--  margin-bottom: 10px;-->
<!--  width: 100%;-->
<!--}-->

<!--.angle-labels {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: flex-start;-->
<!--  justify-content: center;-->
<!--  margin-left: 20px;-->
<!--}-->

<!--.angle-labels span {-->
<!--  font-size: 0.8em;-->
<!--  margin-bottom: 5px;-->
<!--}-->

<!--.angle-input {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: flex-start;-->
<!--  font-size: 0.8em;-->
<!--  margin-bottom: 5px;-->
<!--}-->

<!--.input-narrow .el-input-number {-->
<!--  width: 80px;-->
<!--}-->

<!--.confirm-button {-->
<!--  margin-top: 10px;-->
<!--  margin-left: 10px;-->
<!--  padding: 5px 10px;-->
<!--  font-size: 12px;-->
<!--  border-radius: 5px;-->
<!--}-->

<!--.el-input-number&#45;&#45;small .el-input__inner {-->
<!--  height: 22px;-->
<!--  padding: 0 7px;-->
<!--}-->

<!--.radio-group {-->
<!--  margin-bottom: 10px;-->
<!--}-->

<!--.slider-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  align-items: center;-->
<!--  margin-top: 10px;-->
<!--}-->

<!--.slider-short {-->
<!--  width: 150px;-->
<!--}-->

<!--.slider-labels {-->
<!--  display: flex;-->
<!--  justify-content: space-between;-->
<!--  width: 100%;-->
<!--  padding: 0 20px;-->
<!--}-->

<!--.slider-label {-->
<!--  font-size: 0.8em;-->
<!--}-->

<!--.category-menu {-->
<!--  display: grid;-->
<!--  grid-template-columns: repeat(3, 1fr);-->
<!--  gap: 10px;-->
<!--  margin-top: 20px;-->
<!--  font-size: 0.9em;-->
<!--}-->

<!--.category-menu button {-->
<!--  padding: 10px;-->
<!--  border: none;-->
<!--  background-color: #eee;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  border-radius: 10px;-->
<!--}-->

<!--.category-menu button.active {-->
<!--  background-color: #333;-->
<!--  color: white;-->
<!--}-->

<!--.bus-list {-->
<!--  display: grid;-->
<!--  grid-template-columns: repeat(5, 1fr);-->
<!--  gap: 10px;-->
<!--  margin-top: 20px;-->
<!--  width: 100%;-->
<!--  font-size: 0.9em;-->
<!--}-->

<!--.bus-list button {-->
<!--  height: 40px;-->
<!--  border: none;-->
<!--  background-color: #f0f8ff;-->
<!--  color: #0000ee;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  line-height: 40px;-->
<!--  border-radius: 5px;-->
<!--}-->

<!--.bus-list button.bus-active {-->
<!--  border: 2px solid blue;-->
<!--  font-weight: bold;-->
<!--}-->

<!--.reset-button {-->
<!--  margin-top: 20px;-->
<!--  padding: 10px 20px;-->
<!--  border: none;-->
<!--  background-color: #ff6347;-->
<!--  color: white;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  border-radius: 5px;-->
<!--}-->

<!--.arrow-icon {-->
<!--  display: flex;-->
<!--  justify-content: center;-->
<!--  align-items: center;-->
<!--  transform-origin: center;-->
<!--}-->

<!--.arrow-svg {-->
<!--  width: 20px;-->
<!--  height: 20px;-->
<!--}-->
<!--</style>-->


<template>
  <div id="container">
    <div id="map"></div>
    <div id="navbar">
      <div class="menu-bar">
        <button @click="selectMenu('routes')" :class="{ active: activeMenu === 'routes' }">Routes</button>
        <button @click="selectMenu('passengerFlow')" :class="{ active: activeMenu === 'passengerFlow' }">Passenger Flow</button>
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
  name: 'MapView',
  components: {
    ElSwitch,
    ElSlider,
    ElRadio,
    ElRadioGroup,
    ElInputNumber,
    ElButton,
    KnobControl,
  },
  setup() {
    const colorMap8 = ["rgb(248,215,73)", "rgb(231,135,60)", "rgb(218,55,62)", "rgb(111,48,140)", "rgb(50,71,153)", "rgb(78,155,195)", "rgb(120,186,87)", "rgb(225,231,121)"];
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
    const isPassengerFlowMode = ref(false); // 标志位

    const categories = ref(tabsData.filter(category => category.numbers.length > 0));
    const selectedCategory = ref(categories.value[0]?.label || '');
    const selectedBuses = ref(categories.value[0]?.numbers || []);
    const filteredCategories = ref(categories.value);
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
      zoom: 12,
    };

    const reset = () => {
      backgroundSwitch.value = initialState.backgroundSwitch;
      viewSwitch.value = initialState.viewSwitch;
      lineWeight.value = initialState.lineWeight;
      selectedCategory.value = initialState.selectedCategory;
      selectedBuses.value = initialState.selectedBuses;
      selectedBus.value = null;
      use360Colors.value = false;
      clearMap();
      if (isPassengerFlowMode.value) {
        fetchPassengerFlowRoutes();
      } else {
        fetchRoutes();
      }
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
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${bus}`);
        console.log('Route data fetched:', response.data);
        const routeData = response.data;
        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);
        clearMap();

        // Draw grey route
        L.polyline(points, { color: 'lightgray', weight: lineWeight.value, opacity: 0.5 }).addTo(toRaw(currentLayerGroup.value));

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

        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
        toRaw(map.value).fitBounds(polyline.getBounds());
        console.log('Route rendered successfully');

      } catch (error) {
        console.error(`Error fetching route data for ${bus}:`, error);
      }
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

    const fetchAllStations = async () => {
      if (!map.value || !currentLayerGroup.value) return;

      try {
        const response = await axios.get('http://127.0.0.1:5000/api/routes', {
          params: {
            min_angle: 0,
            max_angle: 360
          }
        });
        const routes = response.data;
        const stationPromises = routes.map(route => fetchStationData(route));
        const allStations = (await Promise.all(stationPromises)).flat();
        initializeMapWithStations(allStations);
      } catch (error) {
        console.error('Error fetching all stations data:', error);
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

    const fetchPassengerFlowRoutes = async () => {
      if (!map.value || !currentLayerGroup.value) return;

      try {
        const response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {
          params: {
            min_angle: angleRange.value[0],
            max_angle: angleRange.value[1]
          }
        });
        const passengerFlowRoutes = response.data;
        const routePromises = passengerFlowRoutes.map(route => fetchRouteDataWithPassengerFlow(route.route_id, route.usage_recorded));
        const routeData = await Promise.all(routePromises);
        initializeMapWithPassengerFlowRoutes(routeData.filter(route => route !== null));
      } catch (error) {
        console.error('Error fetching passenger flow routes:', error);
      }
    };

    const fetchRouteDataWithPassengerFlow = async (routeId, usageRecorded) => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
        const routeData = response.data;
        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);
        const weight = getLineWeight(usageRecorded);
        return {
          routeId: routeData.route_id,
          points,
          angle: routeData.angle,
          weight
        };
      } catch (error) {
        console.error(`Error fetching route data for ${routeId}:`, error);
        return null;
      }
    };

    const getLineWeight = (usageRecorded) => {
      if (usageRecorded <= 629233.75) {
        return 3;
      } else if (usageRecorded <= 2048661.50) {
        return 4.5;
      } else if (usageRecorded <= 4042106.50) {
        return 6;
      } else {
        return 7.5;
      }
    };

    const initializeMapWithRoutes = (routes) => {
      clearMap();
      // First draw grey routes
      routes.forEach((route) => {
        if (currentLayerGroup.value) {
          L.polyline(route.points, { color: 'lightgray', weight: lineWeight.value, opacity: 0.5 }).addTo(toRaw(currentLayerGroup.value));
        }
      });
      // Then draw colored routes
      routes.forEach((route) => {
        if (currentLayerGroup.value && (angleRange.value[0] <= angleRange.value[1]
          ? route.angle >= angleRange.value[0] && route.angle <= angleRange.value[1]
          : route.angle >= angleRange.value[0] || route.angle <= angleRange.value[1])) {
          const routeColor = getColorByAngle(route.angle);
          L.polyline(route.points, { color: routeColor, weight: lineWeight.value, opacity: 0.7 }).addTo(toRaw(currentLayerGroup.value));
        }
      });
      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
      }
    };

    const initializeMapWithPassengerFlowRoutes = (routes) => {
      clearMap();
      routes.forEach((route) => {
        if (currentLayerGroup.value) {
          const routeColor = getColorByAngle(route.angle);
          L.polyline(route.points, { color: routeColor, weight: route.weight, opacity: 0.9 }).addTo(toRaw(currentLayerGroup.value));
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

          marker.bindTooltip(station.Stop_Name, { permanent: false, direction: 'top' });
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

    const initializeMapWithStartPoints = (routes) => {
      clearMap();
      routes.forEach(route => {
        if (currentLayerGroup.value) {
          const routeColor = getColorByAngle(route.angle);
          const startPoint = route.points[0];
          const arrowIcon = createArrowIcon(route.angle, routeColor);
          L.marker(startPoint, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));
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
        fetchAllStations();
      } else {
        fetchRoutes();
      }
    };

    const handleRadioChange = async (value) => {
      if (isPassengerFlowMode.value) {
        if (value === 'directions') {
          use360Colors.value = true;
          await fetchDirectionsPassengerFlow();
        } else if (value === 'start') {
          use360Colors.value = true;
          await fetchStartPointsPassengerFlow();
        } else {
          use360Colors.value = false;
          fetchPassengerFlowRoutes();
        }
      } else {
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

          L.polyline([start, end], { color: routeColor, weight: lineWeight.value, opacity: 0.6 }).addTo(toRaw(currentLayerGroup.value));

          const arrowIcon = createArrowIcon(angle, routeColor);
          L.marker(start, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));
        }

        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
        console.log('Directions rendered successfully');

      } catch (error) {
        console.error('Error fetching directions:', error);
      }
    };

    const fetchDirectionsPassengerFlow = async () => {
      if (!map.value || !currentLayerGroup.value) return;

      try {
        const response = await axios.get('http://127.0.0.1:5000/api/passenger_flow_directions', {
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

          L.polyline([start, end], { color: routeColor, weight: lineWeight.value, opacity: 0.6 }).addTo(toRaw(currentLayerGroup.value));

          const arrowIcon = createArrowIcon(angle, routeColor);
          L.marker(start, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));
        }

        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
        console.log('Passenger Flow Directions rendered successfully');

      } catch (error) {
        console.error('Error fetching passenger flow directions:', error);
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

    const fetchStartPointsPassengerFlow = async () => {
      if (!map.value || !currentLayerGroup.value) return;

      try {
        const response = await axios.get('http://127.0.0.1:5000/api/passenger_flow_start', {
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

        console.log('Passenger Flow Start points rendered successfully');
      } catch (error) {
        console.error('Error fetching passenger flow start points:', error);
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
      if (isPassengerFlowMode.value) {
        fetchPassengerFlowRoutes();
      } else if (viewSwitch.value) {
        fetchAllStations();
      } else if (radio.value === 'directions') {
        if (isPassengerFlowMode.value) {
          fetchDirectionsPassengerFlow();
        } else {
          fetchDirections();
        }
      } else if (radio.value === 'start') {
        if (isPassengerFlowMode.value) {
          fetchStartPointsPassengerFlow();
        } else {
          fetchStartPoints();
        }
      } else {
        if (isPassengerFlowMode.value) {
          fetchPassengerFlowRoutes();
        } else {
          fetchRoutes();
        }
      }
    };

    const selectMenu = (menu) => {
      activeMenu.value = menu;
      isPassengerFlowMode.value = (menu === 'passengerFlow');
      console.log(`Selected menu: ${menu}`);
      applyAngleRange();
    };

    watch(lineWeight, () => {
      applyAngleRange();
    });

    watch(backgroundSwitch, () => {
      updateMapLayer();
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
      isPassengerFlowMode,
    };
  }
};
</script>

<style scoped>
#container {
  display: flex;
  height: 100vh;
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
  margin-bottom: 10px;
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
  grid-template-columns: repeat(3, 1fr);
  gap: 10px;
  margin-top: 20px;
  font-size: 0.9em;
}

.category-menu button {
  padding: 10px;
  border: none;
  background-color: #eee;
  cursor: pointer;
  text-align: center;
  border-radius: 10px;
}

.category-menu button.active {
  background-color: #333;
  color: white;
}

.bus-list {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 10px;
  margin-top: 20px;
  width: 100%;
  font-size: 0.9em;
}

.bus-list button {
  height: 40px;
  border: none;
  background-color: #f0f8ff;
  color: #0000ee;
  cursor: pointer;
  text-align: center;
  line-height: 40px;
  border-radius: 5px;
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


