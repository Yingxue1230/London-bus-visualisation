<!--<template>-->
<!--  <div id="container">-->
<!--    <div id="map"></div>-->
<!--    <div id="navbar">-->
<!--      <div class="menu-bar">-->
<!--        &lt;!&ndash; 这个按钮用于切换主视图 &ndash;&gt;-->
<!--        <button @click="switchView('routes')" :class="{ active: activeMenu === 'routes' }">Routes</button>-->
<!--        <button @click="switchView('passengerFlow')" :class="{ active: activeMenu === 'passengerFlow' }">Passenger Flow</button>-->
<!--      </div>-->
<!--      <div class="switch-container">-->
<!--        <el-radio-group v-model="colorMode" @change="toggleColorMode">-->
<!--          <el-radio :value="'gray'">Gray</el-radio>-->
<!--          <el-radio :value="'color'">Colour</el-radio>-->
<!--          <el-radio :value="'dark'">Dark</el-radio>-->
<!--        </el-radio-group>-->
<!--      </div>-->
<!--      <div style="margin-top: 10px">-->
<!--        <el-radio-group v-model="colorOption" @change="handleColorChange">-->
<!--          <el-radio value="1" size="default" border>Color 1</el-radio>-->
<!--          <el-radio value="2" size="default" border>Color 2</el-radio>-->
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
<!--            :stroke-width="5"-->
<!--            @change="applyAngleRange"-->
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
<!--        &lt;!&ndash; 这个部分用于在主视图下切换模式 &ndash;&gt;-->
<!--        <el-radio-group v-model="radio" class="radio-group" @change="handleRadioChange">-->
<!--          <el-radio :value="'routes'">Routes</el-radio>-->
<!--          <el-radio :value="'directions'">Directions</el-radio>-->
<!--          <el-radio :value="'start'">Start</el-radio>-->
<!--        </el-radio-group>-->
<!--      </div>-->
<!--      <div class="switch-container" style="margin-top: 10px">-->
<!--        <el-switch-->
<!--          v-model="timePeriodSwitch"-->
<!--          size="large"-->
<!--          active-text="Daily"-->
<!--          inactive-text="Yearly"-->
<!--          @change="handleTimePeriodChange"-->
<!--        />-->
<!--      </div>-->
<!--      <div v-if="timePeriodSwitch && activeMenu === 'passengerFlow'" style="margin-top: 10px">-->
<!--        <el-radio-group v-model="selectedDay" size="large" @change="fetchDailyPassengerFlow">-->
<!--          <el-radio-button label="Weekday" value="Weekday" />-->
<!--          <el-radio-button label="Saturday" value="Saturday" />-->
<!--          <el-radio-button label="Sunday" value="Sunday" />-->
<!--        </el-radio-group>-->
<!--      </div>-->

<!--      &lt;!&ndash; 分类标签部分 &ndash;&gt;-->
<!--      <div v-if="timePeriodSwitch && activeMenu === 'passengerFlow'" class="category-container" style="margin-top: 10px">-->
<!--        <div class="category-menu">-->
<!--          <button-->
<!--            v-for="category in categories"-->
<!--            :key="category.label"-->
<!--            @click="selectCategory(category)"-->
<!--            :class="{ active: selectedCategory && selectedCategory.label === category.label }"-->
<!--          >-->
<!--            {{ category.label }}-->
<!--          </button>-->
<!--        </div>-->
<!--        <div v-if="selectedCategory" class="bus-list">-->
<!--          <button-->
<!--            v-for="bus in selectedCategory.numbers"-->
<!--            :key="String(bus)"-->
<!--            @click="selectBus(bus)"-->
<!--            :class="{ 'bus-active': selectedBus === String(bus) }"-->
<!--            :style="{ backgroundColor: lineColors[bus] }"-->
<!--          >-->
<!--            {{ bus }}-->
<!--          </button>-->
<!--        </div>-->
<!--      </div>-->

<!--      &lt;!&ndash; 仅在 Daily 模式且选择线路后显示滑块部分 &ndash;&gt;-->
<!--      <div v-if="timePeriodSwitch && activeMenu === 'passengerFlow' && selectedBus" class="slider-container" style="margin-top: 10px">-->
<!--        <div class="slider-demo-block">-->
<!--          <span class="demonstration">Hour: {{ selectedHour }}</span>-->
<!--          <el-slider v-model="selectedHour" :min="0" :max="23" :step="1" @input="onSliderInput" @change="onSliderChange" style="width: 250px;"/>-->
<!--        </div>-->
<!--        <div class="slider-demo-block">-->
<!--          <span class="demonstration">Minute: {{ selectedMinute }}</span>-->
<!--          <el-slider v-model="selectedMinute" :min="0" :max="45" :step="15" @input="onSliderInput" @change="onSliderChange" style="width: 250px;"/>-->
<!--        </div>-->

<!--        <div class="selectedStop">-->
<!--          <el-radio-group v-model="selectedStop" @change="handleStopChange">-->
<!--            <el-radio value="1" border>Route</el-radio>-->
<!--            <el-radio value="2" border>Stop</el-radio>-->
<!--          </el-radio-group>-->
<!--        </div>-->

<!--        <div class="animation-button-container">-->
<!--        <el-button v-if="timePeriodSwitch && selectedBus" type="danger" @click="toggleBusStopAnimation" class="mt-4">-->
<!--          <el-icon><animate/></el-icon>-->
<!--          Animation-->
<!--        </el-button>-->
<!--        </div>-->
<!--      </div>-->

<!--      <button @click="reset" class="reset-button">Reset</button>-->
<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script>-->
<!--import { onMounted, ref, onBeforeUnmount, toRaw, watch } from 'vue';-->
<!--import axios from 'axios';-->
<!--import L from 'leaflet';-->
<!--import 'leaflet/dist/leaflet.css';-->
<!--import { ElSwitch, ElRadio, ElRadioGroup, ElInputNumber, ElButton, ElMessage } from 'element-plus';-->
<!--import 'element-plus/dist/index.css';-->
<!--import {animate} from '@element-plus/icons-vue'-->
<!--import KnobControl from './KnobControl.vue';-->
<!--import tabsDataWithColors from '@/data/tabs_data1_with_colors.json';-->

<!--export default {-->
<!--  name: 'PassengerFlowView',-->
<!--  components: {-->
<!--    ElSwitch,-->
<!--    ElRadio,-->
<!--    ElRadioGroup,-->
<!--    ElInputNumber,-->
<!--    ElButton,-->
<!--    KnobControl,-->
<!--  },-->
<!--  setup(props, { emit }) {-->
<!--    const categories = ref(tabsDataWithColors);-->
<!--    const selectedCategory = ref(null);-->
<!--    const selectedBus = ref(null);-->
<!--    const map = ref(null);-->
<!--    const lineWeight = ref(3);-->
<!--    const currentLayerGroup = ref(null);-->
<!--    const mapInitialized = ref(false);-->
<!--    const radio = ref('routes');-->
<!--    const use360Colors = ref(false);-->
<!--    const angleRange = ref([0, 360]);-->
<!--    const colorOption = ref('1');-->
<!--    const activeMenu = ref('passengerFlow');-->
<!--    const selectedStop = ref('1');-->
<!--    const timePeriodSwitch = ref(false); // false 表示 Yearly, true 表示 Daily-->
<!--    const selectedDay = ref('Weekday'); // 默认选择工作日-->
<!--    const currentPolyline = ref(null); // 使用 ref-->
<!--    const isPaused = ref(false);-->
<!--    const currentStep = ref(0);-->
<!--    const lineColors = ref({});-->
<!--    const totalSteps = 24 * 4; // 96 steps for 15-minute intervals over 24 hours-->
<!--    const initialState = {-->
<!--      lineWeight: 3,-->
<!--      center: [51.5074, -0.1278],-->
<!--      zoom: 11,-->
<!--    };-->

<!--    L.Icon.Default.mergeOptions({-->
<!--    iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',-->
<!--    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',-->
<!--    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',-->
<!--    });-->

<!--    const selectedHour = ref(0);-->
<!--    const selectedMinute = ref(0);-->
<!--    const firstDailyClick = ref(true); // Track if it's the first click in Daily mode-->

<!--    const colorMode = ref('gray'); // 默认是灰色模式-->
<!--    const isSliding = ref(false);-->

<!--    const animateBusStops = ref(false) // 是否启用动画-->
<!--    const stopMarkers = ref([]) // 存储当前显示的公交车站点标记-->
<!--    let animationIntervalId = null // 保存动画的interval ID-->

<!--    const toggleColorMode = () => {-->
<!--      updateMapLayer();-->
<!--    };-->

<!--    const createArrowIcon = (angle, color, size) => {-->
<!--      return L.divIcon({-->
<!--            className: 'arrow-icon',-->
<!--            html: `-->
<!--              <div class="arrow-icon" style="transform: rotate(${angle}deg);">-->
<!--                <svg class="arrow-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}">-->
<!--                  <polygon points="50,0 15,100 85,100" fill="${color}" />-->
<!--                </svg>-->
<!--              </div>-->
<!--            `,-->
<!--            iconSize: [size, size],-->
<!--            iconAnchor: [size / 2, size / 2],-->
<!--        });-->
<!--    };-->

<!--    const naturalSort = (a, b) => {-->
<!--      const ax = [], bx = [];-->
<!--      a.toString().replace(/(\d+)|(\D+)/g, (_, $1, $2) => ax.push([$1 || Infinity, $2 || ""]));-->
<!--      b.toString().replace(/(\d+)|(\D+)/g, (_, $1, $2) => bx.push([$1 || Infinity, $2 || ""]));-->
<!--      while (ax.length && bx.length) {-->
<!--        const an = ax.shift();-->
<!--        const bn = bx.shift();-->
<!--        const nn = (an[0] - bn[0]) || an[1].localeCompare(bn[1]);-->
<!--        if (nn) return nn;-->
<!--      }-->
<!--      return ax.length - bx.length;-->
<!--    };-->

<!--    watch(selectedCategory, (newCategory) => {-->
<!--      if (newCategory) newCategory.numbers.sort(naturalSort);-->
<!--    });-->

<!--    const reset = () => {-->
<!--      timePeriodSwitch.value = false; // 重置为 Yearly-->
<!--      lineWeight.value = initialState.lineWeight;-->
<!--      use360Colors.value = false;-->
<!--      angleRange.value = [0, 360];-->
<!--      clearMap();-->
<!--      fetchPassengerFlowRoutes();-->
<!--      if (map.value) toRaw(map.value).setView(initialState.center, initialState.zoom);-->
<!--      updateMapLayer();-->
<!--      selectedCategory.value = null;-->
<!--      selectedBus.value = null;-->

<!--      // 重置时隐藏信息框-->
<!--      map.value.routeInfoControl.hideInfo();-->
<!--    };-->

<!--    const selectCategory = (category) => {-->
<!--      selectedCategory.value = category;-->
<!--    };-->

<!--    const selectBus = async (bus) => {-->
<!--      const busString = String(bus);-->
<!--      selectedBus.value = busString;-->

<!--      selectedCategory.value = categories.value.find(category =>-->
<!--        category.numbers.map(String).includes(busString)-->
<!--      );-->

<!--      // 重置小时和分钟-->
<!--      selectedHour.value = 0;-->
<!--      selectedMinute.value = 0;-->

<!--      // 重置动画的步数，使时间从00:00开始-->
<!--      currentStep.value = 0;-->

<!--      // 根据当前选择是显示线路还是显示站点，调用相应的函数-->
<!--      if (selectedStop.value === '1') {-->
<!--        await displayRoute(bus);-->
<!--      } else if (selectedStop.value === '2') {-->
<!--        await displayStop(bus);-->
<!--      }-->

<!--      // 获取新线路的客流数据-->
<!--      await fetchPassengerFlowData();-->
<!--    };-->

<!--    const onSliderInput = () => {-->
<!--      // 标志滑块正在被滑动-->
<!--      isSliding.value = true;-->
<!--    };-->

<!--    const onSliderChange = () => {-->
<!--        if (isSliding.value) {-->
<!--          isSliding.value = false;-->

<!--          // 更新信息框的内容，调用 fetchPassengerFlowData 函数-->
<!--          fetchPassengerFlowData();-->

<!--          // 暂停时更新页面显示到当前时间-->
<!--          if (isPaused.value || !animateBusStops.value) {-->
<!--            if (selectedStop.value === '2') {-->
<!--              displayStop(selectedBus.value);-->
<!--            } else {-->
<!--              displayRoute(selectedBus.value);-->
<!--            }-->
<!--          }-->
<!--        }-->
<!--      };-->



<!--    // 在 watch 函数中确保在时间改变时自动更新显示-->
<!--    watch([selectedHour, selectedMinute], () => {-->
<!--      if (selectedStop.value === '1' && selectedBus.value) {-->
<!--        displayRoute(selectedBus.value); // 更新路线-->
<!--      } else if (selectedStop.value === '2' && selectedBus.value) {-->
<!--        displayStop(selectedBus.value);  // 更新站点-->
<!--      }-->
<!--    });-->

<!--    const displayRoute = async (routeId) => {-->
<!--      try {-->
<!--        clearMap();-->

<!--        const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = routeResponse.data;-->

<!--        const points = routeData.points.map((point) => [point.Latitude, point.Longitude]);-->
<!--        const routeColor = getColorByAngle(routeData.angle);-->

<!--        // 默认使用最小粗细，实际粗细将在 fetchPassengerFlowData 中计算并设置-->
<!--        currentPolyline.value = L.polyline(points, {-->
<!--          color: routeColor,-->
<!--          weight: 2, // 这是一个默认值，稍后会被动态更新-->
<!--          opacity: 0.8-->
<!--        }).addTo(toRaw(currentLayerGroup.value));-->

<!--        const latitudes = points.map(p => p[0]);-->
<!--        const longitudes = points.map(p => p[1]);-->
<!--        const center = [-->
<!--          latitudes.reduce((a, b) => a + b, 0) / latitudes.length,-->
<!--          longitudes.reduce((a, b) => a + b, 0) / longitudes.length-->
<!--        ];-->

<!--        const zoomLevel = 12.5;-->
<!--        map.value.setView(center, zoomLevel);-->

<!--        points.forEach((point, index) => {-->
<!--          const marker = L.circleMarker(point, {-->
<!--            radius: 5,-->
<!--            color: 'white',-->
<!--            weight: 2,-->
<!--            fill: true,-->
<!--            fillColor: routeColor,-->
<!--            fillOpacity: 1-->
<!--          }).bindTooltip(`<b>${routeData.points[index].Stop_Name}</b>`, {-->
<!--            permanent: false,-->
<!--            direction: 'top'-->
<!--          });-->
<!--          marker.addTo(toRaw(currentLayerGroup.value));-->
<!--        });-->

<!--        selectedBus.value = String(routeId);-->

<!--        selectedCategory.value = categories.value.find(category => {-->
<!--          return category.numbers.map(String).includes(selectedBus.value);-->
<!--        });-->

<!--        // 获取客流量数据并更新线路粗细-->
<!--        await fetchPassengerFlowData();-->

<!--      } catch (error) {-->
<!--        console.error(`Error displaying route ${routeId}:`, error);-->
<!--      }-->
<!--    };-->

<!--    const displayStop = async (routeId) => {-->
<!--        try {-->
<!--            // 清空地图上当前的图层-->
<!--            clearMap();-->

<!--            // 获取路线的颜色-->
<!--            const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--            const routeData = routeResponse.data;-->
<!--            const routeColor = getColorByAngle(routeData.angle);-->

<!--            // 调用后端API获取指定路线在特定时间点的站点数据-->
<!--            const response = await axios.get(`http://127.0.0.1:5000/api/stop_passenger_flow/${routeId}`, {-->
<!--                params: {-->
<!--                    day_type: selectedDay.value.toLowerCase(),-->
<!--                    hour: selectedHour.value,-->
<!--                    minute: selectedMinute.value-->
<!--                }-->
<!--            });-->

<!--            const stopData = response.data;-->

<!--            if (stopData && stopData.stops.length > 0) {-->
<!--                // 获取最大和最小的 Boardings 和 Load 值-->
<!--                const maxBoardings = stopData.max_boardings;-->
<!--                const minBoardings = stopData.min_boardings;-->
<!--                const maxLoad = stopData.max_load;-->
<!--                const minLoad = stopData.min_load;-->

<!--                let previousStop = null;-->

<!--               // 添加起点标志-->
<!--                const startPoint = [routeData.points[0].Latitude, routeData.points[0].Longitude];-->
<!--                L.marker(startPoint).addTo(toRaw(currentLayerGroup.value)); // 简单地添加起点标志-->

<!--                stopData.stops.forEach((stop) => {-->
<!--                    if (previousStop) {-->
<!--                        // 根据Load值计算线路粗细和颜色-->
<!--                        let lineWeight;-->
<!--                        let lineColor;-->


<!--                        if (previousStop.Load === 'NaN') {-->
<!--                            // 如果Load为0，设置白色线条，粗细为2-->
<!--                            lineWeight = 2;-->
<!--                            lineColor = routeColor;-->
<!--                        } else {-->
<!--                            // 否则根据Load值计算粗细，并使用路线颜色-->
<!--                            lineWeight = 2 + 30 * ((previousStop.Load - minLoad) / (maxLoad - minLoad));-->
<!--                            lineColor = routeColor;-->
<!--                        }-->

<!--                        const polyline = L.polyline([-->
<!--                            [previousStop.Latitude, previousStop.Longitude],-->
<!--                            [stop.Latitude, stop.Longitude]-->
<!--                        ], {-->
<!--                            color: lineColor,-->
<!--                            weight: lineWeight,-->
<!--                            opacity: 1-->
<!--                        }).addTo(toRaw(currentLayerGroup.value));-->

<!--                        // 绑定tooltip，显示Load-->
<!--                        polyline.bindTooltip(`Load: ${previousStop.Load}`, {-->
<!--                            permanent: false,-->
<!--                            direction: 'center',-->
<!--                            offset: L.point(0, 0),-->
<!--                            className: 'line-tooltip'-->
<!--                        });-->
<!--                    }-->
<!--                    // 更新 previousStop 为当前 stop-->
<!--                    previousStop = stop;-->
<!--                });-->

<!--                // 然后绘制点-->
<!--                stopData.stops.forEach((stop) => {-->
<!--                    // 计算点的大小，基于 Boardings-->
<!--                    let radius;-->
<!--                    let fillColor;-->

<!--                    if (stop.Boardings === 'NaN') {-->
<!--                        // 如果 Boardings 是 NaN，设置空心圆-->
<!--                        radius = 5; // 您可以根据需要调整半径大小-->
<!--                        fillColor = 'none'; // 空心圆，无填充-->
<!--                    } else {-->
<!--                        // 否则，设置填充颜色-->
<!--                        radius = 5 + 15 * ((stop.Boardings - minBoardings) / (maxBoardings - minBoardings));-->
<!--                        fillColor = routeColor; // 根据实际颜色设置-->
<!--                    }-->

<!--                    // 在地图上为每个站点绘制一个标记-->
<!--                    const marker = L.circleMarker([stop.Latitude, stop.Longitude], {-->
<!--                        radius: Math.max(radius, 5),  // 最小值为5-->
<!--                        color: 'white',-->
<!--                        weight: fillColor === 'none' ? 4 : 2,-->
<!--                        fill: true,-->
<!--                        fillColor: fillColor,  // 使用路线颜色或空心-->
<!--                        fillOpacity: fillColor === 'none' ? 0 : 1  // 如果是空心圆，设置填充透明度为0-->
<!--                    }).bindTooltip(`<b>${stop.Stop_Name}</b><br/>Boardings: ${stop.Boardings}`, {-->
<!--                        permanent: false,-->
<!--                        direction: 'top'-->
<!--                    });-->

<!--                    marker.addTo(toRaw(currentLayerGroup.value));-->
<!--                });-->

<!--                // 调整地图的视角到合适的位置-->
<!--                const latitudes = stopData.stops.map(s => s.Latitude);-->
<!--                const longitudes = stopData.stops.map(s => s.Longitude);-->
<!--                const center = [-->
<!--                    latitudes.reduce((a, b) => a + b, 0) / latitudes.length,-->
<!--                    longitudes.reduce((a, b) => a + b, 0) / longitudes.length-->
<!--                ];-->

<!--                const zoomLevel = 12.5;-->
<!--                map.value.setView(center, zoomLevel);-->
<!--            }-->

<!--        } catch (error) {-->
<!--            console.error(`Error displaying stops for route ${routeId}:`, error);-->
<!--        }-->
<!--    };-->




<!--    const fetchPassengerFlowData = async () => {-->
<!--      try {-->
<!--        if (!selectedBus.value) {-->
<!--          console.error('未选择任何路线');-->
<!--          return;-->
<!--        }-->

<!--        const params = {-->
<!--          day_type: selectedDay.value.toLowerCase(),-->
<!--          hour: selectedHour.value,-->
<!--          minute: selectedMinute.value-->
<!--        };-->

<!--        const response = await axios.get(`http://127.0.0.1:5000/api/daily_passenger_flow/${selectedBus.value}`, { params });-->
<!--        const passengerFlowData = response.data;-->

<!--        let infoContent = `<div>Route: ${selectedBus.value}</div>`;-->

<!--        if (passengerFlowData && passengerFlowData.total_boardings !== undefined) {-->
<!--          const totalBoardings = passengerFlowData.total_boardings;-->
<!--          const maxBoardings = passengerFlowData.max_boardings;-->
<!--          const minBoardings = passengerFlowData.min_boardings;-->

<!--          // 设置最大和最小粗细-->
<!--          const maxWeight = 20;  // 最大粗细-->
<!--          const minWeight = 2;   // 最小粗细-->

<!--          // 根据客流量动态计算线路的粗细-->
<!--          const weight = minWeight + (maxWeight - minWeight) * ((totalBoardings - minBoardings) / (maxBoardings - minBoardings));-->

<!--          // 更新线路的粗细-->
<!--          if (currentPolyline.value) {-->
<!--            currentPolyline.value.setStyle({ weight: weight });-->
<!--          }-->

<!--          const formattedTotalBoardings = totalBoardings.toLocaleString();-->

<!--          infoContent += `<div>Time: ${selectedHour.value}:${selectedMinute.value}</div>`;-->
<!--          infoContent += `<div>Boardings: ${formattedTotalBoardings}</div>`;-->
<!--        } else {-->
<!--          infoContent += `<div>No data available</div>`;-->
<!--        }-->

<!--        map.value.routeInfoControl.showInfo(infoContent);-->

<!--      } catch (error) {-->
<!--        console.error('Error fetching passenger flow data:', error);-->
<!--        map.value.routeInfoControl.showInfo('<div>No data available</div>');-->
<!--      }-->
<!--    };-->

<!--    const getColorByAngle = (angle) => {-->
<!--      const colorMap8 = [-->
<!--        'rgb(248,215,73)',-->
<!--        'rgb(231,135,60)',-->
<!--        'rgb(218,55,62)',-->
<!--        'rgb(111,48,140)',-->
<!--        'rgb(50,71,153)',-->
<!--        'rgb(78,155,195)',-->
<!--        'rgb(120,186,87)',-->
<!--        'rgb(225,231,121)',-->
<!--      ];-->
<!--      const colorMap1 = [-->
<!--        '#FF0D00',-->
<!--        '#FF8900',-->
<!--        '#FFB600',-->
<!--        '#FFEE00',-->
<!--        '#C9FF00',-->
<!--        '#0DFF00',-->
<!--        '#00FFF5',-->
<!--        '#109CFF',-->
<!--        '#186EFF',-->
<!--        '#4B1FFF',-->
<!--        '#9E10FF',-->
<!--        '#FF0196',-->
<!--      ];-->
<!--      const colorMap360 = Array.from({ length: 360 }, (_, i) => `hsl(${i}, 90%, 50%)`);-->

<!--      if (use360Colors.value) return colorMap360[Math.round(angle) % 360];-->
<!--      else if (colorOption.value === '1') {-->
<!--        const index = Math.floor(angle / 45) % 8;-->
<!--        return colorMap8[index];-->
<!--      } else {-->
<!--        const index = Math.floor(angle / 30) % 12;-->
<!--        return colorMap1[index];-->
<!--      }-->
<!--    };-->

<!--    const RouteInfoControl = L.Control.extend({-->
<!--      options: { position: 'topright' },-->

<!--      onAdd: function () {-->
<!--        const container = L.DomUtil.create('div', 'route-info-control');-->
<!--        container.style.backgroundColor = 'white';-->
<!--        container.style.padding = '10px';-->
<!--        container.style.borderRadius = '5px';-->
<!--        container.style.boxShadow = '0 2px 6px rgba(0, 0, 0, 0.3)';-->
<!--        container.style.display = 'none';-->

<!--        container.innerHTML = `-->
<!--        <div id="route-info">请选择一条线路</div>-->
<!--        <div id="time-info"></div>-->
<!--      `;-->

<!--        L.DomEvent.disableClickPropagation(container);-->
<!--        return container;-->
<!--      },-->

<!--      showInfo: function (routeInfo, timeInfo) {-->
<!--        this.getContainer().style.display = 'block';-->
<!--        this.getContainer().querySelector('#route-info').innerHTML = routeInfo;-->
<!--        this.getContainer().querySelector('#time-info').innerHTML = timeInfo || '';-->
<!--      },-->

<!--      hideInfo: function () {-->
<!--        this.getContainer().style.display = 'none';-->
<!--      }-->
<!--    });-->

<!--    const fetchPassengerFlowRoutes = async () => {-->
<!--      if (!map.value || !currentLayerGroup.value) return;-->
<!--      try {-->
<!--        const response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1],-->
<!--          },-->
<!--        });-->
<!--        const passengerFlowRoutes = response.data;-->
<!--        const routePromises = passengerFlowRoutes.map((route) =>-->
<!--          fetchRouteDataWithPassengerFlow(route.route_id, route.usage_recorded)-->
<!--        );-->
<!--        const routeData = await Promise.all(routePromises);-->
<!--        initializeMapWithPassengerFlowRoutes(routeData.filter((route) => route !== null));-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching passenger flow routes:', error);-->
<!--      }-->
<!--    };-->

<!--    const fetchRouteDataWithPassengerFlow = async (routeId, usageRecorded) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map((point) => [point.Latitude, point.Longitude]);-->
<!--        const weight = getLineWeight(usageRecorded);-->

<!--        const formattedUsageRecorded = usageRecorded.toLocaleString();-->

<!--        return {-->
<!--          routeId: routeData.route_id,-->
<!--          points,-->
<!--          angle: routeData.angle,-->
<!--          weight,-->
<!--          usageRecorded: formattedUsageRecorded,-->
<!--          time: '2022-2023',-->
<!--        };-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${routeId}:`, error);-->
<!--        return null;-->
<!--      }-->
<!--    };-->

<!--    const getLineWeight = (usageRecorded) => {-->
<!--      const minUsage = 8381;-->
<!--      const maxUsage = 12630186;-->
<!--      const minWeight = 2;-->
<!--      const maxWeight = 10;-->
<!--      return ((usageRecorded - minUsage) / (maxUsage - minUsage)) * (maxWeight - minWeight) + minWeight;-->
<!--    };-->

<!--    const initializeMapWithPassengerFlowRoutes = (routes) => {-->
<!--      clearMap();-->
<!--      routes.forEach((route) => {-->
<!--        if (currentLayerGroup.value) {-->
<!--          const routeColor = getColorByAngle(route.angle);-->
<!--          const polyline = L.polyline(route.points, { color: routeColor, weight: route.weight, opacity: 0.8 })-->
<!--            .addTo(toRaw(currentLayerGroup.value))-->
<!--            .bindTooltip(-->
<!--              `<div>Route: ${route.routeId}</div>-->
<!--               <div>Usage: ${route.usageRecorded}</div>-->
<!--               <div>Time: ${route.time}</div>`,-->
<!--              { permanent: false, direction: 'top' }-->
<!--            );-->

<!--          const startPoint = route.points[0];-->
<!--          L.circleMarker(startPoint, {-->
<!--            radius: 6,-->
<!--            color: 'white',-->
<!--            weight: 2,-->
<!--            fill: true,-->
<!--            fillColor: routeColor,-->
<!--            fillOpacity: 1,-->
<!--          }).addTo(toRaw(currentLayerGroup.value));-->

<!--          polyline.on('mouseover', function (e) {-->
<!--            this.openTooltip(e.latlng);-->
<!--          });-->

<!--          polyline.on('mousemove', function (e) {-->
<!--            this._tooltip.setLatLng(e.latlng);-->
<!--          });-->

<!--          polyline.on('mouseout', function () {-->
<!--            this.closeTooltip();-->
<!--          });-->

<!--        }-->
<!--      });-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const updateMapLayer = () => {-->
<!--      if (map.value) {-->
<!--        let tileLayerUrl;-->
<!--        if (colorMode.value === 'gray') {-->
<!--          tileLayerUrl = 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';-->
<!--        } else if (colorMode.value === 'color') {-->
<!--          tileLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';-->
<!--        } else if (colorMode.value === 'dark') {-->
<!--          tileLayerUrl = 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png';-->
<!--        }-->

<!--        L.tileLayer(tileLayerUrl, {-->
<!--          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',-->
<!--          maxZoom: 19,-->
<!--        }).addTo(toRaw(map.value));-->
<!--      }-->
<!--    };-->

<!--    const clearMap = () => {-->
<!--      if (currentLayerGroup.value) toRaw(currentLayerGroup.value).clearLayers();-->
<!--    };-->

<!--    const handleStopChange = (value) => {-->
<!--      if (value === '1') {-->
<!--        if (selectedBus.value) {-->
<!--          displayRoute(selectedBus.value);-->
<!--        }-->
<!--      } else if (value === '2') {-->
<!--        if (selectedBus.value) {-->
<!--          displayStop(selectedBus.value);-->
<!--        }-->
<!--      }-->
<!--    };-->

<!--    const handleRadioChange = async (value) => {-->
<!--      if (value === 'routes') {-->
<!--        use360Colors.value = false;-->

<!--        if (timePeriodSwitch.value) {-->
<!--          console.log('Fetching Daily Passenger Flow Data');-->
<!--          await fetchDailyPassengerFlow(selectedDay.value);-->
<!--        } else {-->
<!--          console.log('Fetching Yearly Passenger Flow Data');-->
<!--          await fetchPassengerFlowRoutes();-->
<!--        }-->
<!--      } else if (value === 'directions' || value === 'start') {-->
<!--        use360Colors.value = true;-->

<!--        if (value === 'directions') {-->
<!--          if (timePeriodSwitch.value) {-->
<!--            console.log('Fetching Daily Directions Data');-->
<!--            await fetchDirectionsPassengerFlow(true);-->
<!--          } else {-->
<!--            console.log('Fetching Yearly Directions Data');-->
<!--            await fetchDirectionsPassengerFlow(false);-->
<!--          }-->
<!--        } else if (value === 'start') {-->
<!--          if (timePeriodSwitch.value) {-->
<!--            console.log('Fetching Daily Start Points Data');-->
<!--            await fetchStartPointsPassengerFlow(true);-->
<!--          } else {-->
<!--            console.log('Fetching Yearly Start Points Data');-->
<!--            await fetchStartPointsPassengerFlow(false);-->
<!--          }-->
<!--        }-->
<!--      }-->
<!--    };-->

<!--    const fetchDirectionsPassengerFlow = async (isDaily) => {-->
<!--        if (!map.value || !currentLayerGroup.value) return;-->

<!--        try {-->
<!--            let response;-->
<!--            let dataKey; // 用于区分是 usage_recorded 还是 total_boardings-->

<!--            if (isDaily) {-->
<!--                response = await axios.get(`http://127.0.0.1:5000/api/daily_passenger_flow`, {-->
<!--                    params: {-->
<!--                        day_type: selectedDay.value.toLowerCase(),-->
<!--                        min_angle: angleRange.value[0],-->
<!--                        max_angle: angleRange.value[1],-->
<!--                    },-->
<!--                });-->
<!--                dataKey = 'total_boardings';-->
<!--            } else {-->
<!--                response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {-->
<!--                    params: {-->
<!--                        min_angle: angleRange.value[0],-->
<!--                        max_angle: angleRange.value[1],-->
<!--                    },-->
<!--                });-->
<!--                dataKey = 'usage_recorded';-->
<!--            }-->

<!--            const routes = response.data;-->

<!--            if (routes.length === 0) {-->
<!--                console.warn('No routes found for the given parameters.');-->
<!--                return;-->
<!--            }-->

<!--            // 获取最大和最小的客流量数据（取决于 dataKey 是 usage_recorded 还是 total_boardings）-->
<!--            const maxUsage = Math.max(...routes.map(route => route[dataKey]));-->
<!--            const minUsage = Math.min(...routes.map(route => route[dataKey]));-->

<!--            clearMap();-->

<!--            for (const route of routes) {-->
<!--                const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${route.route_id}`);-->
<!--                const routeData = routeResponse.data;-->

<!--                const start = [routeData.points[0].Latitude, routeData.points[0].Longitude];-->
<!--                const end = [routeData.points[routeData.points.length - 1].Latitude, routeData.points[routeData.points.length - 1].Longitude];-->
<!--                const angle = routeData.angle;-->
<!--                const routeColor = getColorByAngle(angle);-->

<!--                // 动态计算线条粗细和箭头大小-->
<!--                const lineWeight = Math.max(2, Math.min(10, ((route[dataKey] - minUsage) / (maxUsage - minUsage)) * 8 + 2));-->
<!--                const arrowSize = Math.max(10, Math.min(40, ((route[dataKey] - minUsage) / (maxUsage - minUsage)) * 40 + 10));-->

<!--                const polyline = L.polyline([start, end], {-->
<!--                    color: routeColor,-->
<!--                    weight: lineWeight,-->
<!--                    opacity: 0.6-->
<!--                }).addTo(toRaw(currentLayerGroup.value));-->

<!--                const arrowIcon = createArrowIcon(angle, routeColor, arrowSize);-->
<!--                L.marker(start, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->

<!--                polyline.bindTooltip(-->
<!--                    `<div>Route: ${route.route_id}</div>-->
<!--                     <div>${dataKey === 'total_boardings' ? 'Total Boardings' : 'Usage Recorded'}: ${route[dataKey]}</div>-->
<!--                     <div>Time Period: ${timePeriodSwitch.value ? 'Daily' : 'Yearly'}</div>`,-->
<!--                    { permanent: false, direction: 'top' }-->
<!--                );-->
<!--            }-->

<!--            toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->

<!--        } catch (error) {-->
<!--            console.error('Error fetching directions:', error);-->
<!--        }-->
<!--    };-->


<!--   const fetchStartPointsPassengerFlow = async (isDaily) => {-->
<!--    if (!map.value || !currentLayerGroup.value) return;-->

<!--    try {-->
<!--        let response;-->
<!--        let dataKey;-->

<!--        // 根据是否为日常数据来设置请求参数和 dataKey-->
<!--        if (isDaily) {-->
<!--            response = await axios.get(`http://127.0.0.1:5000/api/daily_passenger_flow`, {-->
<!--                params: {-->
<!--                    day_type: selectedDay.value.toLowerCase(),-->
<!--                    min_angle: angleRange.value[0],-->
<!--                    max_angle: angleRange.value[1],-->
<!--                },-->
<!--            });-->
<!--            dataKey = 'total_boardings';-->
<!--        } else {-->
<!--            response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {-->
<!--                params: {-->
<!--                    min_angle: angleRange.value[0],-->
<!--                    max_angle: angleRange.value[1],-->
<!--                },-->
<!--            });-->
<!--            dataKey = 'usage_recorded';-->
<!--        }-->

<!--        const routes = response.data;-->


<!--        if (routes.length === 0) {-->
<!--            console.warn('No routes found for the given parameters.');-->
<!--            return;-->
<!--        }-->

<!--        // 计算最大和最小的客流量-->
<!--        const maxUsage = Math.max(...routes.map(route => route[dataKey]));-->
<!--        const minUsage = Math.min(...routes.map(route => route[dataKey]));-->

<!--        clearMap();-->

<!--        // 获取每个路线的数据-->
<!--        const routePromises = routes.map(route => fetchRouteData(route.route_id));-->
<!--        const routeData = await Promise.all(routePromises);-->

<!--        routeData.forEach(route => {-->
<!--            if (route && currentLayerGroup.value) {-->
<!--                const routeColor = getColorByAngle(route.angle);-->
<!--                const startPoint = route.points[0];-->

<!--                // 在 routes 中找到匹配的 usageValue-->
<!--                const matchedRoute = routes.find(r => r.route_id === route.routeId);-->
<!--                const usageValue = matchedRoute ? matchedRoute[dataKey] : undefined;-->

<!--                if (usageValue === undefined) {-->
<!--                    console.warn(`Usage data is missing for route ${route.routeId}. Skipping this route.`);-->
<!--                    return; // 如果数据缺失，跳过这条线路-->
<!--                }-->

<!--                // 动态计算箭头大小-->
<!--                let arrowSize = Math.max(10, Math.min(40, ((usageValue - minUsage) / (maxUsage - minUsage)) * 40 + 10));-->

<!--                // 创建箭头图标-->
<!--                const arrowIcon = createArrowIcon(route.angle, routeColor, arrowSize);-->
<!--                const marker = L.marker(startPoint, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));-->

<!--                // 为每个标记绑定工具提示-->
<!--                marker.bindTooltip(-->
<!--                    `<div>Route: ${route.routeId}</div>-->
<!--                     <div>Time Period: ${timePeriodSwitch.value ? 'Daily' : 'Yearly'}</div>`,-->
<!--                    { permanent: false, direction: 'top' }-->
<!--                );-->
<!--            }-->
<!--        });-->

<!--        // 将图层组添加到地图中-->
<!--        if (currentLayerGroup.value) {-->
<!--            toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->
<!--        }-->

<!--    } catch (error) {-->
<!--        console.error('Error fetching passenger flow start points:', error);-->
<!--    }-->
<!--};-->


<!--    const fetchRouteData = async (routeId) => {-->
<!--      try {-->
<!--        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--        const routeData = response.data;-->
<!--        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);-->
<!--        return {-->
<!--          routeId: routeData.route_id,-->
<!--          points,-->
<!--          angle: routeData.angle-->
<!--        };-->
<!--      } catch (error) {-->
<!--        console.error(`Error fetching route data for ${routeId}:`, error);-->
<!--        return null;-->
<!--      }-->
<!--    };-->

<!--    const handleAngleChange = () => {-->
<!--      applyAngleRange();-->
<!--    };-->

<!--    const handleColorChange = () => {-->
<!--        // 如果当前显示的是路线模式-->
<!--        if (selectedBus.value && selectedStop.value === '1') {-->
<!--            // 重新显示当前选中的路线，并应用新的颜色选项-->
<!--            displayRoute(selectedBus.value);-->
<!--        } else if (selectedBus.value && selectedStop.value === '2') {-->
<!--            // 如果当前显示的是站点模式，更新站点显示-->
<!--            displayStop(selectedBus.value);-->
<!--        } else {-->
<!--            // 如果没有特定的路线或站点选中，则按照原来的逻辑处理-->
<!--            if (timePeriodSwitch.value) {-->
<!--                if (radio.value === 'routes') {-->
<!--                    fetchDailyPassengerFlow(selectedDay.value);-->
<!--                } else if (radio.value === 'directions') {-->
<!--                    fetchDirectionsPassengerFlow(true);-->
<!--                } else if (radio.value === 'start') {-->
<!--                    fetchStartPointsPassengerFlow(true);-->
<!--                }-->
<!--            } else {-->
<!--                // Yearly模式下的处理-->
<!--                if (radio.value === 'routes') {-->
<!--                    fetchPassengerFlowRoutes();-->
<!--                } else if (radio.value === 'directions') {-->
<!--                    fetchDirectionsPassengerFlow(false);-->
<!--                } else if (radio.value === 'start') {-->
<!--                    fetchStartPointsPassengerFlow(false);-->
<!--                }-->
<!--            }-->
<!--        }-->
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
<!--      if (timePeriodSwitch.value) {-->
<!--        if (radio.value === 'routes') {-->
<!--          fetchDailyPassengerFlow(selectedDay.value);-->
<!--        } else if (radio.value === 'directions') {-->
<!--          fetchDirectionsPassengerFlow(true);-->
<!--        } else if (radio.value === 'start') {-->
<!--          fetchStartPointsPassengerFlow(true);-->
<!--        }-->
<!--      } else {-->
<!--        if (radio.value === 'routes') {-->
<!--          fetchPassengerFlowRoutes();-->
<!--        } else if (radio.value === 'directions') {-->
<!--          fetchDirectionsPassengerFlow(false);-->
<!--        } else if (radio.value === 'start') {-->
<!--          fetchStartPointsPassengerFlow(false);-->
<!--        }-->
<!--      }-->
<!--    };-->

<!--    const handleTimePeriodChange = async (value) => {-->
<!--      console.log('Time Period Switch changed to:', value ? 'Daily' : 'Yearly');-->
<!--      if (value) {-->
<!--        firstDailyClick.value = true;-->
<!--        if (radio.value === 'routes') {-->
<!--          await fetchDailyPassengerFlow(selectedDay.value);-->
<!--        } else if (radio.value === 'directions') {-->
<!--          await fetchDirectionsPassengerFlow(true);-->
<!--        } else if (radio.value === 'start') {-->
<!--          await fetchStartPointsPassengerFlow(true);-->
<!--        }-->
<!--      } else {-->
<!--        map.value.routeInfoControl.hideInfo();-->
<!--        if (radio.value === 'routes') {-->
<!--          await fetchPassengerFlowRoutes();-->
<!--        } else if (radio.value === 'directions') {-->
<!--          await fetchDirectionsPassengerFlow(false);-->
<!--        } else if (radio.value === 'start') {-->
<!--          await fetchStartPointsPassengerFlow(false);-->
<!--        }-->
<!--      }-->
<!--    };-->

<!--    const fetchDailyPassengerFlow = async (day) => {-->
<!--      let apiUrl = '';-->
<!--      switch (day) {-->
<!--        case 'Weekday':-->
<!--          apiUrl = 'http://127.0.0.1:5000/api/daily_passenger_flow?day_type=weekday';-->
<!--          break;-->
<!--        case 'Saturday':-->
<!--          apiUrl = 'http://127.0.0.1:5000/api/daily_passenger_flow?day_type=saturday';-->
<!--          break;-->
<!--        case 'Sunday':-->
<!--          apiUrl = 'http://127.0.0.1:5000/api/daily_passenger_flow?day_type=sunday';-->
<!--          break;-->
<!--        default:-->
<!--          console.error('Invalid day selection');-->
<!--          return;-->
<!--      }-->

<!--      try {-->
<!--        const response = await axios.get(apiUrl, {-->
<!--          params: {-->
<!--            min_angle: angleRange.value[0],-->
<!--            max_angle: angleRange.value[1],-->
<!--          },-->
<!--        });-->

<!--        clearMap();-->

<!--        if (radio.value === 'directions') {-->
<!--          await fetchDirectionsPassengerFlow(true);-->
<!--        } else if (radio.value === 'start') {-->
<!--          await fetchStartPointsPassengerFlow(true);-->
<!--        } else {-->
<!--          const dailyData = response.data;-->

<!--          const maxBoardings = 18598.00759;-->
<!--          const minBoardings = 16.57183;-->
<!--          const maxThickness = 10;-->
<!--          const minThickness = 2;-->

<!--          for (const route of dailyData) {-->
<!--            const routeResponse = await fetchRouteData(route.route_id);-->
<!--            if (routeResponse && currentLayerGroup.value) {-->
<!--              const routeColor = getColorByAngle(routeResponse.angle || 0);-->

<!--              let dynamicWeight = ((route.total_boardings - minBoardings) / (maxBoardings - minBoardings)) * (maxThickness - minThickness) + minThickness;-->
<!--              dynamicWeight = Math.max(dynamicWeight, minThickness);-->

<!--              const formattedBoardings = route.total_boardings.toLocaleString();-->

<!--              const polyline = L.polyline(routeResponse.points, {-->
<!--                color: routeColor,-->
<!--                weight: dynamicWeight,-->
<!--                opacity: 0.8-->
<!--              }).addTo(toRaw(currentLayerGroup.value)).bindTooltip(-->
<!--                `<div>Route: ${route.route_id}</div>-->
<!--                 <div>Boardings: ${formattedBoardings}</div>`,-->
<!--                { permanent: false, direction: 'top' }-->
<!--              );-->

<!--              const startPoint = routeResponse.points[0];-->
<!--              L.circleMarker(startPoint, {-->
<!--                radius: 6,-->
<!--                color: 'white',-->
<!--                weight: 2,-->
<!--                fill: true,-->
<!--                fillColor: routeColor,-->
<!--                fillOpacity: 1,-->
<!--              }).addTo(toRaw(currentLayerGroup.value));-->

<!--              polyline.on('mouseover', function (e) {-->
<!--                this.openTooltip(e.latlng);-->
<!--              });-->

<!--              polyline.on('mousemove', function (e) {-->
<!--                this._tooltip.setLatLng(e.latlng);-->
<!--              });-->

<!--              polyline.on('mouseout', function () {-->
<!--                this.closeTooltip();-->
<!--              });-->

<!--              polyline.on('click', function () {-->
<!--                selectBus(route.route_id);-->
<!--              });-->
<!--            }-->
<!--          }-->

<!--          if (currentLayerGroup.value) toRaw(currentLayerGroup.value).addTo(toRaw(map.value));-->

<!--          if (firstDailyClick.value) {-->
<!--            map.value.routeInfoControl.hideInfo();-->
<!--            firstDailyClick.value = false;-->
<!--          }-->
<!--        }-->
<!--      } catch (error) {-->
<!--        console.error('Error fetching daily passenger flow data:', error);-->
<!--      }-->
<!--    };-->

<!--      const toggleBusStopAnimation = () => {-->
<!--      if (animateBusStops.value) {-->
<!--        if (isPaused.value) {-->
<!--          // 恢复动画-->
<!--          isPaused.value = false;-->
<!--          startBusStopAnimation();-->
<!--        } else {-->
<!--          // 暂停动画，保持当前页面不变-->
<!--          isPaused.value = true;-->
<!--          stopBusStopAnimation();-->
<!--        }-->
<!--      } else {-->
<!--        // 开始动画-->
<!--        clearBusStopAnimation();  // 清除已有的站点信息-->
<!--        drawRouteOnce(selectedBus.value); // 确保第一次绘制线路-->
<!--        startBusStopAnimation();-->
<!--        animateBusStops.value = true;-->
<!--      }-->
<!--    };-->


<!--    const startBusStopAnimation = () => {-->
<!--        if (!selectedBus.value) return;-->

<!--        if (!isPaused.value) {-->
<!--            clearBusStopAnimation(); // 仅在动画未暂停时清除之前的站点-->
<!--            drawRouteOnce(selectedBus.value); // 在恢复动画时重新绘制线路-->
<!--        }-->

<!--        animationIntervalId = setInterval(async () => {-->
<!--            if (isPaused.value) return; // 如果动画暂停，则不执行以下代码-->

<!--            const hour = Math.floor(currentStep.value / 4);-->
<!--            const minute = (currentStep.value % 4) * 15;-->

<!--            // Fetch and display bus stop data for the current time step-->
<!--            await displayBusStopsForTime(selectedBus.value, hour, minute);-->

<!--            // 更新到右上角信息框中-->
<!--            const timeInfo = `<div>Time: ${String(hour).padStart(2, '0')}:${String(minute).padStart(2, '0')}</div>`;-->
<!--            const routeInfo = `<div>Route: ${selectedBus.value}</div>`;-->
<!--            map.value.routeInfoControl.showInfo(routeInfo, timeInfo);-->

<!--            currentStep.value += 1;-->
<!--            if (currentStep.value >= totalSteps) {-->
<!--                currentStep.value = 0; // 重置到开始时的状态-->
<!--            }-->
<!--        }, 1000); // 每秒更新一次-->
<!--    }-->

<!--    const drawRouteOnce = async (routeId) => {-->
<!--        try {-->
<!--            clearMap();-->

<!--            // 获取路线的颜色-->
<!--            const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--            const routeData = routeResponse.data;-->
<!--            const routeColor = getColorByAngle(routeData.angle);-->

<!--            // 绘制线路-->
<!--            const points = routeData.points.map((point) => [point.Latitude, point.Longitude]);-->
<!--            L.polyline(points, {-->
<!--                color: routeColor,-->
<!--                weight: 3,  // 可以根据需要调整线路的粗细-->
<!--                opacity: 0.8-->
<!--            }).addTo(toRaw(currentLayerGroup.value));-->

<!--             // 使用默认的蓝色标记图标作为起点-->
<!--           L.marker(points[0]).addTo(toRaw(currentLayerGroup.value))-->

<!--        } catch (error) {-->
<!--            console.error('Error drawing route:', error);-->
<!--        }-->
<!--    };-->

<!--    const stopBusStopAnimation = () => {-->
<!--      // 停止动画的计时器-->
<!--      if (animationIntervalId) {-->
<!--        clearInterval(animationIntervalId);-->
<!--        animationIntervalId = null;-->
<!--      }-->

<!--      // 标记为暂停状态-->
<!--      isPaused.value = true;-->

<!--      // 保持当前显示的站点或路线，不进行任何重新绘制-->
<!--      // 注意：这里不调用 displayStop 或 displayRoute，以免重新绘制页面-->
<!--    }-->



<!--  const displayBusStopsForTime = async (routeId, hour, minute) => {-->
<!--        try {-->
<!--            // 使用 requestAnimationFrame 来批量更新地图内容-->
<!--            requestAnimationFrame(async () => {-->
<!--                // 清除之前的线路和站点-->
<!--                clearBusStopAnimation();-->

<!--                // 获取指定时间点的站点客流数据-->
<!--                const response = await axios.get(`http://127.0.0.1:5000/api/stop_passenger_flow/${routeId}`, {-->
<!--                    params: {-->
<!--                        day_type: selectedDay.value.toLowerCase(),-->
<!--                        hour,-->
<!--                        minute,-->
<!--                    },-->
<!--                });-->

<!--                const stopData = response.data;-->

<!--                // 获取路线数据-->
<!--                const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);-->
<!--                const routeData = routeResponse.data;-->

<!--                // 获取路线颜色-->
<!--                const routeColor = getColorByAngle(routeData.angle);-->

<!--                // 获取最大和最小的 Boardings 和 Load 值-->
<!--                const maxBoardings = stopData.max_boardings;-->
<!--                const minBoardings = stopData.min_boardings;-->
<!--                const maxLoad = stopData.max_load;-->
<!--                const minLoad = stopData.min_load;-->

<!--                let previousStop = null;-->

<!--                // 添加起点标志-->
<!--                const startPoint = [routeData.points[0].Latitude, routeData.points[0].Longitude];-->
<!--                L.marker(startPoint).addTo(toRaw(currentLayerGroup.value)); // 简单地添加起点标志-->

<!--                stopData.stops.forEach((stop) => {-->
<!--                    if (previousStop) {-->
<!--                        // 计算基于载客量的线路粗细-->
<!--                        let lineWeight;-->
<!--                        let lineColor;-->

<!--                        if (previousStop.Load === 'NaN') {-->
<!--                            // 如果 Load 为 NaN 或 null，设置默认线条粗细-->
<!--                            lineWeight = 2;-->
<!--                            lineColor = routeColor;-->
<!--                        } else {-->
<!--                            // 否则根据 Load 值计算粗细，并使用路线颜色-->
<!--                            lineWeight = 2 + 30 * ((previousStop.Load - minLoad) / (maxLoad - minLoad));-->
<!--                            lineColor = routeColor;-->
<!--                        }-->

<!--                        // 绘制站点之间的线路并将其移到背景-->
<!--                        const polyline = L.polyline([-->
<!--                            [previousStop.Latitude, previousStop.Longitude],-->
<!--                            [stop.Latitude, stop.Longitude]-->
<!--                        ], {-->
<!--                            color: lineColor,-->
<!--                            weight: lineWeight,-->
<!--                            opacity: 1-->
<!--                        }).addTo(toRaw(currentLayerGroup.value)).bringToBack();  // 确保线路在后面-->

<!--                        // 为线路绑定 Tooltip，显示 Load 信息-->
<!--                        polyline.bindTooltip(`Load: ${previousStop.Load}`, {-->
<!--                            permanent: false,  // 仅在鼠标悬停时显示-->
<!--                            direction: 'center'-->
<!--                        });-->

<!--                    }-->

<!--                    // 计算基于上客量的站点大小-->
<!--                    let radius;-->
<!--                    let fillColor = routeColor;-->

<!--                    if (stop.Boardings === 'NaN') {-->
<!--                        // 如果 Boardings 为 NaN 或 null，设置空心圆-->
<!--                        radius = 5; // 设置较小半径-->
<!--                        fillColor = 'none'; // 空心圆，无填充-->
<!--                    } else {-->
<!--                        // 否则，设置填充颜色-->
<!--                        radius = 5 + 15 * ((stop.Boardings - minBoardings) / (maxBoardings - minBoardings));-->
<!--                    }-->

<!--                    // 绘制站点并确保其在前面显示-->
<!--                    const marker = L.circleMarker([stop.Latitude, stop.Longitude], {-->
<!--                        radius: Math.max(radius, 5),  // 保证最小值为5-->
<!--                        color: 'white',-->
<!--                        weight: fillColor === 'none' ? 4 : 2, // 如果是空心圆，设置较粗的边框-->
<!--                        fill: true,-->
<!--                        fillColor: fillColor,-->
<!--                        fillOpacity: fillColor === 'none' ? 0 : 1 // 如果是空心圆，设置填充透明度为0-->
<!--                    }).addTo(toRaw(currentLayerGroup.value));-->

<!--                    // 使用 bringToFront 确保标记在前端显示-->
<!--                    marker.bringToFront();-->

<!--                    // 绑定上客量的工具提示-->
<!--                    marker.bindTooltip(`<b>${stop.Stop_Name}</b><br/>Boardings: ${stop.Boardings}`, {-->
<!--                        permanent: false,-->
<!--                        direction: 'top'-->
<!--                    });-->

<!--                    stopMarkers.value.push(marker);-->

<!--                    previousStop = stop;-->
<!--                });-->

<!--                // 更新信息框内容-->
<!--                const timeInfo = `<div>Time: ${String(hour).padStart(2, '0')}:${String(minute).padStart(2, '0')}</div>`;-->
<!--                const routeInfo = `<div>Route: ${routeId}</div>`;-->
<!--                map.value.routeInfoControl.showInfo(routeInfo, timeInfo);-->
<!--            });-->

<!--        } catch (error) {-->
<!--            console.error('Error updating stop data:', error);-->
<!--        }-->
<!--    };-->




<!--    const clearBusStopAnimation = () => {-->
<!--        // 清除站点标记-->
<!--        stopMarkers.value.forEach((marker) => {-->
<!--            if (currentLayerGroup.value) {-->
<!--                toRaw(currentLayerGroup.value).removeLayer(marker);-->
<!--            }-->
<!--        });-->
<!--        stopMarkers.value = []; // 清空站点标记数组-->

<!--        // 清除所有线路-->
<!--        if (currentLayerGroup.value) {-->
<!--            toRaw(currentLayerGroup.value).clearLayers();-->
<!--        }-->
<!--};-->

<!--    const switchView = (view) => {-->
<!--      emit('switch-view', view);-->
<!--      activeMenu.value = view;-->
<!--    };-->

<!--    watch(lineWeight, () => {-->
<!--      applyAngleRange();-->
<!--    });-->

<!--    watch(colorMode, () => {-->
<!--      toggleColorMode();-->
<!--    });-->

<!--    watch(colorOption, () => {-->
<!--      handleColorChange();-->
<!--    });-->

<!--    // 观察 selectedHour 的变化，当它改变时，将 selectedMinute 重置为 0-->
<!--    watch(selectedHour, () => {-->
<!--        selectedMinute.value = 0;-->
<!--        fetchPassengerFlowData();  // 当小时变化时，自动获取新的数据-->
<!--    });-->

<!--    watch([selectedHour, selectedMinute], () => {-->
<!--      if (selectedStop.value === '2' && selectedBus.value) {-->
<!--        displayStop(selectedBus.value);-->
<!--      }-->
<!--    });-->

<!--    watch(selectedStop, (newValue) => {-->
<!--      if (selectedBus.value) {-->
<!--        if (newValue === '1') {-->
<!--          displayRoute(selectedBus.value);-->
<!--        } else if (newValue === '2') {-->
<!--          displayStop(selectedBus.value);-->
<!--        }-->
<!--      }-->
<!--    });-->

<!--    onMounted(() => {-->
<!--  // 定义 L.Popup 的动画行为（你已有的代码）-->
<!--      L.Popup.prototype._animateZoom = function (e) {-->
<!--        if (!this._map) return;-->
<!--        var pos = toRaw(this._map)._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),-->
<!--          anchor = this._getAnchor();-->
<!--        L.DomUtil.setPosition(this._container, pos.add(anchor));-->
<!--      };-->

<!--      // 初始化地图（你已有的代码）-->
<!--      map.value = L.map('map').setView(initialState.center, initialState.zoom);-->
<!--      currentLayerGroup.value = L.layerGroup().addTo(toRaw(map.value));-->
<!--      mapInitialized.value = true;-->
<!--      updateMapLayer();-->

<!--      // 加载并应用颜色映射关系-->
<!--      categories.value = tabsDataWithColors;-->
<!--      categories.value.forEach((category) => {-->
<!--        category.numbers.forEach((number, index) => {-->
<!--          lineColors.value[number] = category.colors[index];-->
<!--        });-->
<!--      });-->

<!--      // 检查时间开关状态，并根据不同情况加载数据（你已有的代码）-->
<!--      if (timePeriodSwitch.value) {-->
<!--        fetchDailyPassengerFlow(selectedDay.value);-->
<!--      } else {-->
<!--        fetchPassengerFlowRoutes();-->
<!--      }-->

<!--      const routeInfoControl = new RouteInfoControl();-->
<!--      routeInfoControl.addTo(toRaw(map.value));-->
<!--      routeInfoControl.hideInfo();-->
<!--      map.value.routeInfoControl = routeInfoControl;-->
<!--    });-->

<!--    onBeforeUnmount(() => {-->
<!--      mapInitialized.value = false;-->
<!--      if (map.value) {-->
<!--        map.value.off(); // 解绑所有事件-->
<!--        map.value.remove(); // 清除地图-->
<!--        map.value = null;-->
<!--      }-->
<!--      if (currentLayerGroup.value) {-->
<!--        toRaw(currentLayerGroup.value).clearLayers(); // 在这里使用 toRaw-->
<!--        currentLayerGroup.value = null;-->
<!--      }-->
<!--    });-->

<!--    return {-->
<!--      lineWeight,-->
<!--      colorMode,-->
<!--      reset,-->
<!--      radio,-->
<!--      handleRadioChange,-->
<!--      angleRange,-->
<!--      handleAngleChange,-->
<!--      colorOption,-->
<!--      handleColorChange,-->
<!--      validateAngle,-->
<!--      applyAngleRange,-->
<!--      activeMenu,-->
<!--      switchView,-->
<!--      selectedStop,-->
<!--      onSliderInput,-->
<!--      onSliderChange,-->
<!--      timePeriodSwitch,-->
<!--      selectedDay,-->
<!--      fetchDailyPassengerFlow,-->
<!--      handleTimePeriodChange,-->
<!--      categories,-->
<!--      selectedCategory,-->
<!--      selectCategory,-->
<!--      selectedBus,-->
<!--      selectBus,-->
<!--      selectedHour,-->
<!--      selectedMinute,-->
<!--      fetchPassengerFlowData,-->
<!--      handleStopChange,-->
<!--      toggleBusStopAnimation,-->
<!--      animate,-->
<!--      lineColors,-->
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
<!--  margin-bottom: 10px;-->
<!--  width: 100%;-->
<!--  display: flex;-->
<!--  justify-content: center;-->
<!--}-->

<!--.knob-radio-container {-->
<!--  border: 3px solid #9bbef8;-->
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
<!--  margin-bottom: 0px;-->
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

<!--.category-container {-->
<!--  display: flex;-->
<!--  flex-direction: column;-->
<!--  width: 100%;-->
<!--  align-items: center;-->
<!--}-->

<!--.category-menu {-->
<!--  display: grid;-->
<!--  grid-template-columns: repeat(5, 1fr);-->
<!--  gap: 8px;-->
<!--  margin-top: 20px;-->
<!--  font-size: 0.8em;-->
<!--}-->

<!--.category-menu button {-->
<!--  padding: 5px;-->
<!--  height: 30px;-->
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
<!--  grid-template-columns: repeat(8, 1fr);-->
<!--  gap: 5px;-->
<!--  margin-top: 10px;-->
<!--  width: 100%;-->
<!--}-->

<!--.bus-list button {-->
<!--  color: white;-->
<!--  height: 30px;-->
<!--  border: none;-->
<!--  background-color: #f0f8ff;-->
<!--  cursor: pointer;-->
<!--  text-align: center;-->
<!--  line-height: 25px;-->
<!--  border-radius: 3px;-->
<!--  font-size: 0.9em;-->
<!--  text-shadow: 1px 1px 3px black; /* 添加黑色文本阴影 */-->
<!--  padding: 2px;-->
<!--}-->

<!--.bus-list button.bus-active {-->
<!--  font-weight: bold;-->
<!--  border: 2px solid;-->
<!--  box-shadow: 0 0 0 2px black;-->
<!--  text-shadow: 1px 1px 3px black; /* 选中时依然保持阴影 */-->
<!--}-->

<!--.selectedStop {-->
<!--  margin-top: 20px;-->
<!--  display: flex;-->
<!--  justify-content: center;-->
<!--}-->

<!--.slider-long {-->
<!--  width: 300px;-->
<!--}-->

<!--.animation-button-container {-->
<!--  display: flex;-->
<!--  justify-content: center; /* 居中 */-->
<!--  margin-top: 20px; /* 与上面的按钮保持一定距离 */-->
<!--}-->
<!--</style>-->


<template>
  <div id="container">
    <div id="map"></div>
    <div id="navbar">
      <div class="menu-bar">
        <!-- 这个按钮用于切换主视图 -->
        <button @click="switchView('routes')" :class="{ active: activeMenu === 'routes' }">Routes</button>
        <button @click="switchView('passengerFlow')" :class="{ active: activeMenu === 'passengerFlow' }">Passenger Flow</button>
      </div>
      <div class="switch-container">
        <el-radio-group v-model="colorMode" @change="toggleColorMode">
          <el-radio :value="'gray'">Gray</el-radio>
          <el-radio :value="'color'">Colour</el-radio>
          <el-radio :value="'dark'">Dark</el-radio>
        </el-radio-group>
      </div>
      <div style="margin-top: 10px">
        <el-radio-group v-model="colorOption" @change="handleColorChange">
          <el-radio value="1" size="default" border>Color 1</el-radio>
          <el-radio value="2" size="default" border>Color 2</el-radio>
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
            :stroke-width="5"
            @change="applyAngleRange"
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
        <!-- 这个部分用于在主视图下切换模式 -->
        <el-radio-group v-model="radio" class="radio-group" @change="handleRadioChange">
          <el-radio :value="'routes'">Routes</el-radio>
          <el-radio :value="'directions'">Directions</el-radio>
          <el-radio :value="'start'">Start</el-radio>
        </el-radio-group>
      </div>
      <div class="switch-container" style="margin-top: 10px">
        <el-switch
          v-model="timePeriodSwitch"
          size="large"
          active-text="Daily"
          inactive-text="Yearly"
          @change="handleTimePeriodChange"
        />
      </div>
      <div v-if="timePeriodSwitch && activeMenu === 'passengerFlow'" style="margin-top: 10px">
        <el-radio-group v-model="selectedDay" size="large" @change="fetchDailyPassengerFlow">
          <el-radio-button label="Weekday" value="Weekday" />
          <el-radio-button label="Saturday" value="Saturday" />
          <el-radio-button label="Sunday" value="Sunday" />
        </el-radio-group>
      </div>

      <!-- 分类标签部分 -->
      <div v-if="timePeriodSwitch && activeMenu === 'passengerFlow'" class="category-container" style="margin-top: 10px">
        <div class="category-menu">
          <button
            v-for="category in categories"
            :key="category.label"
            @click="selectCategory(category)"
            :class="{ active: selectedCategory && selectedCategory.label === category.label }"
          >
            {{ category.label }}
          </button>
        </div>
        <div v-if="selectedCategory" class="bus-list">
          <button
            v-for="bus in selectedCategory.numbers"
            :key="String(bus)"
            @click="selectBus(bus)"
            :class="{ 'bus-active': selectedBus === String(bus) }"
            :style="{ backgroundColor: lineColors[bus] }"
          >
            {{ bus }}
          </button>
        </div>
      </div>

      <!-- 仅在 Daily 模式且选择线路后显示滑块部分 -->
      <div v-if="timePeriodSwitch && activeMenu === 'passengerFlow' && selectedBus" class="slider-container" style="margin-top: 10px">
        <div class="slider-demo-block">
          <span class="demonstration">Hour: {{ selectedHour }}</span>
          <el-slider v-model="selectedHour" :min="0" :max="23" :step="1" @input="onSliderInput" @change="onSliderChange" style="width: 250px;"/>
        </div>
        <div class="slider-demo-block">
          <span class="demonstration">Minute: {{ selectedMinute }}</span>
          <el-slider v-model="selectedMinute" :min="0" :max="45" :step="15" @input="onSliderInput" @change="onSliderChange" style="width: 250px;"/>
        </div>

        <div class="selectedStop">
          <el-radio-group v-model="selectedStop" @change="handleStopChange">
            <el-radio value="1" border>Route</el-radio>
            <el-radio value="2" border>Stop</el-radio>
          </el-radio-group>
        </div>

        <div class="animation-button-container">
        <el-button v-if="timePeriodSwitch && selectedBus" type="danger" @click="toggleBusStopAnimation" class="mt-4">
          <el-icon><animate/></el-icon>
          Animation
        </el-button>
        </div>
      </div>

      <button @click="reset" class="reset-button">Reset</button>
    </div>
  </div>
</template>

<script>
import { onMounted, ref, onBeforeUnmount, toRaw, watch } from 'vue';
import axios from 'axios';
import L from 'leaflet';
import 'leaflet/dist/leaflet.css';
import { ElSwitch, ElRadio, ElRadioGroup, ElInputNumber, ElButton, ElMessage } from 'element-plus';
import 'element-plus/dist/index.css';
import {animate} from '@element-plus/icons-vue'
import KnobControl from './KnobControl.vue';
import tabsDataWithColors from '@/data/tabs_data1_with_colors.json';

export default {
  name: 'PassengerFlowView',
  components: {
    ElSwitch,
    ElRadio,
    ElRadioGroup,
    ElInputNumber,
    ElButton,
    KnobControl,
  },
  setup(props, { emit }) {
    const categories = ref(tabsDataWithColors);
    const selectedCategory = ref(null);
    const selectedBus = ref(null);
    const map = ref(null);
    const lineWeight = ref(3);
    const currentLayerGroup = ref(null);
    const mapInitialized = ref(false);
    const radio = ref('routes');
    const use360Colors = ref(false);
    const angleRange = ref([0, 360]);
    const colorOption = ref('1');
    const activeMenu = ref('passengerFlow');
    const selectedStop = ref('1');
    const timePeriodSwitch = ref(false); // false 表示 Yearly, true 表示 Daily
    const selectedDay = ref('Weekday'); // 默认选择工作日
    const currentPolyline = ref(null); // 使用 ref
    const isPaused = ref(false);
    const currentStep = ref(0);
    const lineColors = ref({});
    const totalSteps = 24 * 4; // 96 steps for 15-minute intervals over 24 hours
    const initialState = {
      lineWeight: 3,
      center: [51.5074, -0.1278],
      zoom: 11,
    };

    L.Icon.Default.mergeOptions({
    iconRetinaUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon-2x.png',
    iconUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-icon.png',
    shadowUrl: 'https://cdnjs.cloudflare.com/ajax/libs/leaflet/1.7.1/images/marker-shadow.png',
    });

    const selectedHour = ref(0);
    const selectedMinute = ref(0);
    const firstDailyClick = ref(true); // Track if it's the first click in Daily mode

    const colorMode = ref('gray'); // 默认是灰色模式
    const isSliding = ref(false);

    const animateBusStops = ref(false) // 是否启用动画
    const stopMarkers = ref([]) // 存储当前显示的公交车站点标记
    let animationIntervalId = null // 保存动画的interval ID

    const toggleColorMode = () => {
      updateMapLayer();
    };

    const createArrowIcon = (angle, color, size) => {
      return L.divIcon({
            className: 'arrow-icon',
            html: `
              <div class="arrow-icon" style="transform: rotate(${angle}deg);">
                <svg class="arrow-svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}">
                  <polygon points="50,0 15,100 85,100" fill="${color}" />
                </svg>
              </div>
            `,
            iconSize: [size, size],
            iconAnchor: [size / 2, size / 2],
        });
    };

    const naturalSort = (a, b) => {
      const ax = [], bx = [];
      a.toString().replace(/(\d+)|(\D+)/g, (_, $1, $2) => ax.push([$1 || Infinity, $2 || ""]));
      b.toString().replace(/(\d+)|(\D+)/g, (_, $1, $2) => bx.push([$1 || Infinity, $2 || ""]));
      while (ax.length && bx.length) {
        const an = ax.shift();
        const bn = bx.shift();
        const nn = (an[0] - bn[0]) || an[1].localeCompare(bn[1]);
        if (nn) return nn;
      }
      return ax.length - bx.length;
    };

    watch(selectedCategory, (newCategory) => {
      if (newCategory) newCategory.numbers.sort(naturalSort);
    });

    const reset = () => {
      timePeriodSwitch.value = false; // 重置为 Yearly
      lineWeight.value = initialState.lineWeight;
      use360Colors.value = false;
      angleRange.value = [0, 360];
      clearMap();
      fetchPassengerFlowRoutes();
      if (map.value) toRaw(map.value).setView(initialState.center, initialState.zoom);
      updateMapLayer();
      selectedCategory.value = null;
      selectedBus.value = null;

      // 重置时隐藏信息框
      map.value.routeInfoControl.hideInfo();
    };

    const selectCategory = (category) => {
      selectedCategory.value = category;
    };

    const selectBus = async (bus) => {
      const busString = String(bus);
      selectedBus.value = busString;

      selectedCategory.value = categories.value.find(category =>
        category.numbers.map(String).includes(busString)
      );

      // 重置小时和分钟
      selectedHour.value = 0;
      selectedMinute.value = 0;

      // 重置动画的步数，使时间从00:00开始
      currentStep.value = 0;

      // 根据当前选择是显示线路还是显示站点，调用相应的函数
      if (selectedStop.value === '1') {
        await displayRoute(bus);
      } else if (selectedStop.value === '2') {
        await displayStop(bus);
      }

      // 获取新线路的客流数据
      await fetchPassengerFlowData();
    };

    const onSliderInput = () => {
      // 标志滑块正在被滑动
      isSliding.value = true;
    };

    const onSliderChange = () => {
        if (isSliding.value) {
          isSliding.value = false;

          // 更新信息框的内容，调用 fetchPassengerFlowData 函数
          fetchPassengerFlowData();

          // 暂停时更新页面显示到当前时间
          if (isPaused.value || !animateBusStops.value) {
            if (selectedStop.value === '2') {
              displayStop(selectedBus.value);
            } else {
              displayRoute(selectedBus.value);
            }
          }
        }
      };



    // 在 watch 函数中确保在时间改变时自动更新显示
    watch([selectedHour, selectedMinute], () => {
      if (selectedStop.value === '1' && selectedBus.value) {
        displayRoute(selectedBus.value); // 更新路线
      } else if (selectedStop.value === '2' && selectedBus.value) {
        displayStop(selectedBus.value);  // 更新站点
      }
    });

    const displayRoute = async (routeId) => {
      try {
        clearMap();

        const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
        const routeData = routeResponse.data;

        const points = routeData.points.map((point) => [point.Latitude, point.Longitude]);
        const routeColor = getColorByAngle(routeData.angle);

        // 默认使用最小粗细，实际粗细将在 fetchPassengerFlowData 中计算并设置
        currentPolyline.value = L.polyline(points, {
          color: routeColor,
          weight: 2, // 这是一个默认值，稍后会被动态更新
          opacity: 0.8
        }).addTo(toRaw(currentLayerGroup.value));

        const latitudes = points.map(p => p[0]);
        const longitudes = points.map(p => p[1]);
        const center = [
          latitudes.reduce((a, b) => a + b, 0) / latitudes.length,
          longitudes.reduce((a, b) => a + b, 0) / longitudes.length
        ];

        const zoomLevel = 12.5;
        map.value.setView(center, zoomLevel);

        points.forEach((point, index) => {
          const marker = L.circleMarker(point, {
            radius: 5,
            color: 'white',
            weight: 2,
            fill: true,
            fillColor: routeColor,
            fillOpacity: 1
          }).bindTooltip(`<b>${routeData.points[index].Stop_Name}</b>`, {
            permanent: false,
            direction: 'top'
          });
          marker.addTo(toRaw(currentLayerGroup.value));
        });

        selectedBus.value = String(routeId);

        selectedCategory.value = categories.value.find(category => {
          return category.numbers.map(String).includes(selectedBus.value);
        });

        // 获取客流量数据并更新线路粗细
        await fetchPassengerFlowData();

      } catch (error) {
        console.error(`Error displaying route ${routeId}:`, error);
      }
    };

    const displayStop = async (routeId) => {
        try {
            // 清空地图上当前的图层
            clearMap();

            // 获取路线的颜色
            const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
            const routeData = routeResponse.data;
            const routeColor = getColorByAngle(routeData.angle);

            // 调用后端API获取指定路线在特定时间点的站点数据
            const response = await axios.get(`http://127.0.0.1:5000/api/stop_passenger_flow/${routeId}`, {
                params: {
                    day_type: selectedDay.value.toLowerCase(),
                    hour: selectedHour.value,
                    minute: selectedMinute.value
                }
            });

            const stopData = response.data;

            if (stopData && stopData.stops.length > 0) {
                // 获取最大和最小的 Boardings 和 Load 值
                const maxBoardings = stopData.max_boardings;
                const minBoardings = stopData.min_boardings;
                const maxLoad = stopData.max_load;
                const minLoad = stopData.min_load;

                let previousStop = null;

               // 添加起点标志
                const startPoint = [routeData.points[0].Latitude, routeData.points[0].Longitude];
                L.marker(startPoint).addTo(toRaw(currentLayerGroup.value)); // 简单地添加起点标志

                stopData.stops.forEach((stop) => {
                    if (previousStop) {
                        // 根据Load值计算线路粗细和颜色
                        let lineWeight;
                        let lineColor;


                        if (previousStop.Load === 'NaN') {
                            // 如果Load为0，设置白色线条，粗细为2
                            lineWeight = 2;
                            lineColor = routeColor;
                        } else {
                            // 否则根据Load值计算粗细，并使用路线颜色
                            lineWeight = 2 + 30 * ((previousStop.Load - minLoad) / (maxLoad - minLoad));
                            lineColor = routeColor;
                        }

                        const polyline = L.polyline([
                            [previousStop.Latitude, previousStop.Longitude],
                            [stop.Latitude, stop.Longitude]
                        ], {
                            color: lineColor,
                            weight: lineWeight,
                            opacity: 1
                        }).addTo(toRaw(currentLayerGroup.value));

                        // 绑定tooltip，显示Load
                        polyline.bindTooltip(`Load: ${previousStop.Load}`, {
                            permanent: false,
                            direction: 'center',
                            offset: L.point(0, 0),
                            className: 'line-tooltip'
                        });
                    }
                    // 更新 previousStop 为当前 stop
                    previousStop = stop;
                });

                // 然后绘制点
                stopData.stops.forEach((stop) => {
                    // 计算点的大小，基于 Boardings
                    let radius;
                    let fillColor;

                    if (stop.Boardings === 'NaN') {
                        // 如果 Boardings 是 NaN，设置空心圆
                        radius = 5; // 您可以根据需要调整半径大小
                        fillColor = 'none'; // 空心圆，无填充
                    } else {
                        // 否则，设置填充颜色
                        radius = 5 + 15 * ((stop.Boardings - minBoardings) / (maxBoardings - minBoardings));
                        fillColor = routeColor; // 根据实际颜色设置
                    }

                    // 在地图上为每个站点绘制一个标记
                    const marker = L.circleMarker([stop.Latitude, stop.Longitude], {
                        radius: Math.max(radius, 5),  // 最小值为5
                        color: 'white',
                        weight: fillColor === 'none' ? 4 : 2,
                        fill: true,
                        fillColor: fillColor,  // 使用路线颜色或空心
                        fillOpacity: fillColor === 'none' ? 0 : 1  // 如果是空心圆，设置填充透明度为0
                    }).bindTooltip(`<b>${stop.Stop_Name}</b><br/>Boardings: ${stop.Boardings}`, {
                        permanent: false,
                        direction: 'top'
                    });

                    marker.addTo(toRaw(currentLayerGroup.value));
                });

                // 调整地图的视角到合适的位置
                const latitudes = stopData.stops.map(s => s.Latitude);
                const longitudes = stopData.stops.map(s => s.Longitude);
                const center = [
                    latitudes.reduce((a, b) => a + b, 0) / latitudes.length,
                    longitudes.reduce((a, b) => a + b, 0) / longitudes.length
                ];

                const zoomLevel = 12.5;
                map.value.setView(center, zoomLevel);
            }

        } catch (error) {
            console.error(`Error displaying stops for route ${routeId}:`, error);
        }
    };




    const fetchPassengerFlowData = async () => {
      try {
        if (!selectedBus.value) {
          console.error('未选择任何路线');
          return;
        }

        const params = {
          day_type: selectedDay.value.toLowerCase(),
          hour: selectedHour.value,
          minute: selectedMinute.value
        };

        const response = await axios.get(`http://127.0.0.1:5000/api/daily_passenger_flow/${selectedBus.value}`, { params });
        const passengerFlowData = response.data;

        let infoContent = `<div>Route: ${selectedBus.value}</div>`;

        if (passengerFlowData && passengerFlowData.total_boardings !== undefined) {
          const totalBoardings = passengerFlowData.total_boardings;
          const maxBoardings = passengerFlowData.max_boardings;
          const minBoardings = passengerFlowData.min_boardings;

          // 设置最大和最小粗细
          const maxWeight = 20;  // 最大粗细
          const minWeight = 2;   // 最小粗细

          // 根据客流量动态计算线路的粗细
          const weight = minWeight + (maxWeight - minWeight) * ((totalBoardings - minBoardings) / (maxBoardings - minBoardings));

          // 更新线路的粗细
          if (currentPolyline.value) {
            currentPolyline.value.setStyle({ weight: weight });
          }

          const formattedTotalBoardings = totalBoardings.toLocaleString();

          infoContent += `<div>Time: ${selectedHour.value}:${selectedMinute.value}</div>`;
          infoContent += `<div>Boardings: ${formattedTotalBoardings}</div>`;
        } else {
          infoContent += `<div>No data available</div>`;
        }

        map.value.routeInfoControl.showInfo(infoContent);

      } catch (error) {
        console.error('Error fetching passenger flow data:', error);
        map.value.routeInfoControl.showInfo('<div>No data available</div>');
      }
    };

    const getColorByAngle = (angle) => {
      const colorMap8 = [
        'rgb(248,215,73)',
        'rgb(231,135,60)',
        'rgb(218,55,62)',
        'rgb(111,48,140)',
        'rgb(50,71,153)',
        'rgb(78,155,195)',
        'rgb(120,186,87)',
        'rgb(225,231,121)',
      ];
      const colorMap1 = [
        '#FF0D00',
        '#FF8900',
        '#FFB600',
        '#FFEE00',
        '#C9FF00',
        '#0DFF00',
        '#00FFF5',
        '#109CFF',
        '#186EFF',
        '#4B1FFF',
        '#9E10FF',
        '#FF0196',
      ];
      const colorMap360 = Array.from({ length: 360 }, (_, i) => `hsl(${i}, 90%, 50%)`);

      if (use360Colors.value) return colorMap360[Math.round(angle) % 360];
      else if (colorOption.value === '1') {
        const index = Math.floor(angle / 45) % 8;
        return colorMap8[index];
      } else {
        const index = Math.floor(angle / 30) % 12;
        return colorMap1[index];
      }
    };

    const RouteInfoControl = L.Control.extend({
      options: { position: 'topright' },

      onAdd: function () {
        const container = L.DomUtil.create('div', 'route-info-control');
        container.style.backgroundColor = 'white';
        container.style.padding = '10px';
        container.style.borderRadius = '5px';
        container.style.boxShadow = '0 2px 6px rgba(0, 0, 0, 0.3)';
        container.style.display = 'none';

        container.innerHTML = `
        <div id="route-info">请选择一条线路</div>
        <div id="time-info"></div>
      `;

        L.DomEvent.disableClickPropagation(container);
        return container;
      },

      showInfo: function (routeInfo, timeInfo) {
        this.getContainer().style.display = 'block';
        this.getContainer().querySelector('#route-info').innerHTML = routeInfo;
        this.getContainer().querySelector('#time-info').innerHTML = timeInfo || '';
      },

      hideInfo: function () {
        this.getContainer().style.display = 'none';
      }
    });

    const fetchPassengerFlowRoutes = async () => {
      if (!map.value || !currentLayerGroup.value) return;
      try {
        const response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {
          params: {
            min_angle: angleRange.value[0],
            max_angle: angleRange.value[1],
          },
        });
        const passengerFlowRoutes = response.data;
        const routePromises = passengerFlowRoutes.map((route) =>
          fetchRouteDataWithPassengerFlow(route.route_id, route.usage_recorded)
        );
        const routeData = await Promise.all(routePromises);
        initializeMapWithPassengerFlowRoutes(routeData.filter((route) => route !== null));
      } catch (error) {
        console.error('Error fetching passenger flow routes:', error);
      }
    };

    const fetchRouteDataWithPassengerFlow = async (routeId, usageRecorded) => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
        const routeData = response.data;
        const points = routeData.points.map((point) => [point.Latitude, point.Longitude]);
        const weight = getLineWeight(usageRecorded);

        const formattedUsageRecorded = usageRecorded.toLocaleString();

        return {
          routeId: routeData.route_id,
          points,
          angle: routeData.angle,
          weight,
          usageRecorded: formattedUsageRecorded,
          time: '2022-2023',
        };
      } catch (error) {
        console.error(`Error fetching route data for ${routeId}:`, error);
        return null;
      }
    };

    const getLineWeight = (usageRecorded) => {
      const minUsage = 8381;
      const maxUsage = 12630186;
      const minWeight = 2;
      const maxWeight = 10;
      return ((usageRecorded - minUsage) / (maxUsage - minUsage)) * (maxWeight - minWeight) + minWeight;
    };

    const initializeMapWithPassengerFlowRoutes = (routes) => {
      clearMap();
      routes.forEach((route) => {
        if (currentLayerGroup.value) {
          const routeColor = getColorByAngle(route.angle);
          const polyline = L.polyline(route.points, { color: routeColor, weight: route.weight, opacity: 0.8 })
            .addTo(toRaw(currentLayerGroup.value))
            .bindTooltip(
              `<div>Route: ${route.routeId}</div>
               <div>Usage: ${route.usageRecorded}</div>
               <div>Time: ${route.time}</div>`,
              { permanent: false, direction: 'top' }
            );

          const startPoint = route.points[0];
          L.circleMarker(startPoint, {
            radius: 6,
            color: 'white',
            weight: 2,
            fill: true,
            fillColor: routeColor,
            fillOpacity: 1,
          }).addTo(toRaw(currentLayerGroup.value));

          polyline.on('mouseover', function (e) {
            this.openTooltip(e.latlng);
          });

          polyline.on('mousemove', function (e) {
            this._tooltip.setLatLng(e.latlng);
          });

          polyline.on('mouseout', function () {
            this.closeTooltip();
          });

        }
      });
      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
      }
    };

    const updateMapLayer = () => {
      if (map.value) {
        let tileLayerUrl;
        if (colorMode.value === 'gray') {
          tileLayerUrl = 'https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png';
        } else if (colorMode.value === 'color') {
          tileLayerUrl = 'https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png';
        } else if (colorMode.value === 'dark') {
          tileLayerUrl = 'https://{s}.basemaps.cartocdn.com/dark_all/{z}/{x}/{y}{r}.png';
        }

        L.tileLayer(tileLayerUrl, {
          attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors',
          maxZoom: 19,
        }).addTo(toRaw(map.value));
      }
    };

    const clearMap = () => {
      if (currentLayerGroup.value) toRaw(currentLayerGroup.value).clearLayers();
    };

    const handleStopChange = (value) => {
      if (value === '1') {
        if (selectedBus.value) {
          displayRoute(selectedBus.value);
        }
      } else if (value === '2') {
        if (selectedBus.value) {
          displayStop(selectedBus.value);
        }
      }
    };

    const handleRadioChange = async (value) => {
      if (value === 'routes') {
        use360Colors.value = false;

        if (timePeriodSwitch.value) {
          console.log('Fetching Daily Passenger Flow Data');
          await fetchDailyPassengerFlow(selectedDay.value);
        } else {
          console.log('Fetching Yearly Passenger Flow Data');
          await fetchPassengerFlowRoutes();
        }
      } else if (value === 'directions' || value === 'start') {
        use360Colors.value = true;

        if (value === 'directions') {
          if (timePeriodSwitch.value) {
            console.log('Fetching Daily Directions Data');
            await fetchDirectionsPassengerFlow(true);
          } else {
            console.log('Fetching Yearly Directions Data');
            await fetchDirectionsPassengerFlow(false);
          }
        } else if (value === 'start') {
          if (timePeriodSwitch.value) {
            console.log('Fetching Daily Start Points Data');
            await fetchStartPointsPassengerFlow(true);
          } else {
            console.log('Fetching Yearly Start Points Data');
            await fetchStartPointsPassengerFlow(false);
          }
        }
      }
    };

    const fetchDirectionsPassengerFlow = async (isDaily) => {
        if (!map.value || !currentLayerGroup.value) return;

        try {
            let response;
            let dataKey; // 用于区分是 usage_recorded 还是 total_boardings

            if (isDaily) {
                response = await axios.get(`http://127.0.0.1:5000/api/daily_passenger_flow`, {
                    params: {
                        day_type: selectedDay.value.toLowerCase(),
                        min_angle: angleRange.value[0],
                        max_angle: angleRange.value[1],
                    },
                });
                dataKey = 'total_boardings';
            } else {
                response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {
                    params: {
                        min_angle: angleRange.value[0],
                        max_angle: angleRange.value[1],
                    },
                });
                dataKey = 'usage_recorded';
            }

            const routes = response.data;

            if (routes.length === 0) {
                console.warn('No routes found for the given parameters.');
                return;
            }

            // 获取最大和最小的客流量数据（取决于 dataKey 是 usage_recorded 还是 total_boardings）
            const maxUsage = Math.max(...routes.map(route => route[dataKey]));
            const minUsage = Math.min(...routes.map(route => route[dataKey]));

            clearMap();

            for (const route of routes) {
                const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${route.route_id}`);
                const routeData = routeResponse.data;

                const start = [routeData.points[0].Latitude, routeData.points[0].Longitude];
                const end = [routeData.points[routeData.points.length - 1].Latitude, routeData.points[routeData.points.length - 1].Longitude];
                const angle = routeData.angle;
                const routeColor = getColorByAngle(angle);

                // 动态计算线条粗细和箭头大小
                const lineWeight = Math.max(2, Math.min(10, ((route[dataKey] - minUsage) / (maxUsage - minUsage)) * 8 + 2));
                const arrowSize = Math.max(10, Math.min(40, ((route[dataKey] - minUsage) / (maxUsage - minUsage)) * 40 + 10));

                const polyline = L.polyline([start, end], {
                    color: routeColor,
                    weight: lineWeight,
                    opacity: 0.6
                }).addTo(toRaw(currentLayerGroup.value));

                const arrowIcon = createArrowIcon(angle, routeColor, arrowSize);
                L.marker(start, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));

                polyline.bindTooltip(
                    `<div>Route: ${route.route_id}</div>
                     <div>${dataKey === 'total_boardings' ? 'Total Boardings' : 'Usage Recorded'}: ${route[dataKey]}</div>
                     <div>Time Period: ${timePeriodSwitch.value ? 'Daily' : 'Yearly'}</div>`,
                    { permanent: false, direction: 'top' }
                );
            }

            toRaw(currentLayerGroup.value).addTo(toRaw(map.value));

        } catch (error) {
            console.error('Error fetching directions:', error);
        }
    };


   const fetchStartPointsPassengerFlow = async (isDaily) => {
    if (!map.value || !currentLayerGroup.value) return;

    try {
        let response;
        let dataKey;

        // 根据是否为日常数据来设置请求参数和 dataKey
        if (isDaily) {
            response = await axios.get(`http://127.0.0.1:5000/api/daily_passenger_flow`, {
                params: {
                    day_type: selectedDay.value.toLowerCase(),
                    min_angle: angleRange.value[0],
                    max_angle: angleRange.value[1],
                },
            });
            dataKey = 'total_boardings';
        } else {
            response = await axios.get('http://127.0.0.1:5000/api/passenger_flow', {
                params: {
                    min_angle: angleRange.value[0],
                    max_angle: angleRange.value[1],
                },
            });
            dataKey = 'usage_recorded';
        }

        const routes = response.data;


        if (routes.length === 0) {
            console.warn('No routes found for the given parameters.');
            return;
        }

        // 计算最大和最小的客流量
        const maxUsage = Math.max(...routes.map(route => route[dataKey]));
        const minUsage = Math.min(...routes.map(route => route[dataKey]));

        clearMap();

        // 获取每个路线的数据
        const routePromises = routes.map(route => fetchRouteData(route.route_id));
        const routeData = await Promise.all(routePromises);

        routeData.forEach(route => {
            if (route && currentLayerGroup.value) {
                const routeColor = getColorByAngle(route.angle);
                const startPoint = route.points[0];

                // 在 routes 中找到匹配的 usageValue
                const matchedRoute = routes.find(r => r.route_id === route.routeId);
                const usageValue = matchedRoute ? matchedRoute[dataKey] : undefined;

                if (usageValue === undefined) {
                    console.warn(`Usage data is missing for route ${route.routeId}. Skipping this route.`);
                    return; // 如果数据缺失，跳过这条线路
                }

                // 动态计算箭头大小
                let arrowSize = Math.max(10, Math.min(40, ((usageValue - minUsage) / (maxUsage - minUsage)) * 40 + 10));

                // 创建箭头图标
                const arrowIcon = createArrowIcon(route.angle, routeColor, arrowSize);
                const marker = L.marker(startPoint, { icon: arrowIcon }).addTo(toRaw(currentLayerGroup.value));

                // 为每个标记绑定工具提示
                marker.bindTooltip(
                    `<div>Route: ${route.routeId}</div>
                     <div>Time Period: ${timePeriodSwitch.value ? 'Daily' : 'Yearly'}</div>`,
                    { permanent: false, direction: 'top' }
                );
            }
        });

        // 将图层组添加到地图中
        if (currentLayerGroup.value) {
            toRaw(currentLayerGroup.value).addTo(toRaw(map.value));
        }

    } catch (error) {
        console.error('Error fetching passenger flow start points:', error);
    }
};


    const fetchRouteData = async (routeId) => {
      try {
        const response = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
        const routeData = response.data;
        const points = routeData.points.map(point => [point.Latitude, point.Longitude]);
        return {
          routeId: routeData.route_id,
          points,
          angle: routeData.angle
        };
      } catch (error) {
        console.error(`Error fetching route data for ${routeId}:`, error);
        return null;
      }
    };

    const handleAngleChange = () => {
      applyAngleRange();
    };

    const handleColorChange = () => {
        // 如果当前显示的是路线模式
        if (selectedBus.value && selectedStop.value === '1') {
            // 重新显示当前选中的路线，并应用新的颜色选项
            displayRoute(selectedBus.value);
        } else if (selectedBus.value && selectedStop.value === '2') {
            // 如果当前显示的是站点模式，更新站点显示
            displayStop(selectedBus.value);
        } else {
            // 如果没有特定的路线或站点选中，则按照原来的逻辑处理
            if (timePeriodSwitch.value) {
                if (radio.value === 'routes') {
                    fetchDailyPassengerFlow(selectedDay.value);
                } else if (radio.value === 'directions') {
                    fetchDirectionsPassengerFlow(true);
                } else if (radio.value === 'start') {
                    fetchStartPointsPassengerFlow(true);
                }
            } else {
                // Yearly模式下的处理
                if (radio.value === 'routes') {
                    fetchPassengerFlowRoutes();
                } else if (radio.value === 'directions') {
                    fetchDirectionsPassengerFlow(false);
                } else if (radio.value === 'start') {
                    fetchStartPointsPassengerFlow(false);
                }
            }
        }
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
      if (timePeriodSwitch.value) {
        if (radio.value === 'routes') {
          fetchDailyPassengerFlow(selectedDay.value);
        } else if (radio.value === 'directions') {
          fetchDirectionsPassengerFlow(true);
        } else if (radio.value === 'start') {
          fetchStartPointsPassengerFlow(true);
        }
      } else {
        if (radio.value === 'routes') {
          fetchPassengerFlowRoutes();
        } else if (radio.value === 'directions') {
          fetchDirectionsPassengerFlow(false);
        } else if (radio.value === 'start') {
          fetchStartPointsPassengerFlow(false);
        }
      }
    };

    const handleTimePeriodChange = async (value) => {
      console.log('Time Period Switch changed to:', value ? 'Daily' : 'Yearly');
      if (value) {
        firstDailyClick.value = true;
        if (radio.value === 'routes') {
          await fetchDailyPassengerFlow(selectedDay.value);
        } else if (radio.value === 'directions') {
          await fetchDirectionsPassengerFlow(true);
        } else if (radio.value === 'start') {
          await fetchStartPointsPassengerFlow(true);
        }
      } else {
        map.value.routeInfoControl.hideInfo();
        if (radio.value === 'routes') {
          await fetchPassengerFlowRoutes();
        } else if (radio.value === 'directions') {
          await fetchDirectionsPassengerFlow(false);
        } else if (radio.value === 'start') {
          await fetchStartPointsPassengerFlow(false);
        }
      }
    };

    const fetchDailyPassengerFlow = async (day) => {
      let apiUrl = '';
      switch (day) {
        case 'Weekday':
          apiUrl = 'http://127.0.0.1:5000/api/daily_passenger_flow?day_type=weekday';
          break;
        case 'Saturday':
          apiUrl = 'http://127.0.0.1:5000/api/daily_passenger_flow?day_type=saturday';
          break;
        case 'Sunday':
          apiUrl = 'http://127.0.0.1:5000/api/daily_passenger_flow?day_type=sunday';
          break;
        default:
          console.error('Invalid day selection');
          return;
      }

      try {
        const response = await axios.get(apiUrl, {
          params: {
            min_angle: angleRange.value[0],
            max_angle: angleRange.value[1],
          },
        });

        clearMap();

        if (radio.value === 'directions') {
          await fetchDirectionsPassengerFlow(true);
        } else if (radio.value === 'start') {
          await fetchStartPointsPassengerFlow(true);
        } else {
          const dailyData = response.data;

          const maxBoardings = 18598.00759;
          const minBoardings = 16.57183;
          const maxThickness = 10;
          const minThickness = 2;

          for (const route of dailyData) {
            const routeResponse = await fetchRouteData(route.route_id);
            if (routeResponse && currentLayerGroup.value) {
              const routeColor = getColorByAngle(routeResponse.angle || 0);

              let dynamicWeight = ((route.total_boardings - minBoardings) / (maxBoardings - minBoardings)) * (maxThickness - minThickness) + minThickness;
              dynamicWeight = Math.max(dynamicWeight, minThickness);

              const formattedBoardings = route.total_boardings.toLocaleString();

              const polyline = L.polyline(routeResponse.points, {
                color: routeColor,
                weight: dynamicWeight,
                opacity: 0.8
              }).addTo(toRaw(currentLayerGroup.value)).bindTooltip(
                `<div>Route: ${route.route_id}</div>
                 <div>Boardings: ${formattedBoardings}</div>`,
                { permanent: false, direction: 'top' }
              );

              const startPoint = routeResponse.points[0];
              L.circleMarker(startPoint, {
                radius: 6,
                color: 'white',
                weight: 2,
                fill: true,
                fillColor: routeColor,
                fillOpacity: 1,
              }).addTo(toRaw(currentLayerGroup.value));

              polyline.on('mouseover', function (e) {
                this.openTooltip(e.latlng);
              });

              polyline.on('mousemove', function (e) {
                this._tooltip.setLatLng(e.latlng);
              });

              polyline.on('mouseout', function () {
                this.closeTooltip();
              });

              polyline.on('click', function () {
                selectBus(route.route_id);
              });
            }
          }

          if (currentLayerGroup.value) toRaw(currentLayerGroup.value).addTo(toRaw(map.value));

          if (firstDailyClick.value) {
            map.value.routeInfoControl.hideInfo();
            firstDailyClick.value = false;
          }
        }
      } catch (error) {
        console.error('Error fetching daily passenger flow data:', error);
      }
    };

     const toggleBusStopAnimation = () => {
        if (animateBusStops.value) {
            if (isPaused.value) {
                // 恢复动画
                isPaused.value = false;
                startBusStopAnimation();
            } else {
                // 暂停动画，保持当前页面不变，但不要清除站点和线路
                isPaused.value = true;
                stopBusStopAnimation();
            }
        } else {
            // 开始动画
            clearBusStopAnimation();  // 清除已有的站点信息
            drawRouteOnce(selectedBus.value); // 确保第一次绘制线路
            startBusStopAnimation();
            animateBusStops.value = true;
        }
    };

    const startBusStopAnimation = () => {
        if (!selectedBus.value) return;

        // 继续动画或从暂停恢复时不清除站点，直接继续显示
        if (!isPaused.value) {
            drawRouteOnce(selectedBus.value); // 重新绘制线路
        }

        animationIntervalId = setInterval(async () => {
            if (isPaused.value) return; // 如果动画暂停，则不执行以下代码

            const hour = Math.floor(currentStep.value / 4);
            const minute = (currentStep.value % 4) * 15;

            // Fetch and display bus stop data for the current time step
            await displayBusStopsForTime(selectedBus.value, hour, minute);

            // 更新到右上角信息框中
            const timeInfo = `<div>Time: ${String(hour).padStart(2, '0')}:${String(minute).padStart(2, '0')}</div>`;
            const routeInfo = `<div>Route: ${selectedBus.value}</div>`;
            map.value.routeInfoControl.showInfo(routeInfo, timeInfo);

            currentStep.value += 1;
            if (currentStep.value >= totalSteps) {
                currentStep.value = 0; // 重置到开始时的状态
            }
        }, 1000); // 每秒更新一次
    };


    const drawRouteOnce = async (routeId) => {
        try {
            clearMap();

            // 获取路线的颜色
            const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
            const routeData = routeResponse.data;
            const routeColor = getColorByAngle(routeData.angle);

            // 绘制线路
            const points = routeData.points.map((point) => [point.Latitude, point.Longitude]);
            L.polyline(points, {
                color: routeColor,
                weight: 3,  // 可以根据需要调整线路的粗细
                opacity: 0.8
            }).addTo(toRaw(currentLayerGroup.value));

             // 使用默认的蓝色标记图标作为起点
           L.marker(points[0]).addTo(toRaw(currentLayerGroup.value))

        } catch (error) {
            console.error('Error drawing route:', error);
        }
    };

    const stopBusStopAnimation = () => {
        // 停止动画的计时器，但不要清除线路和站点
        if (animationIntervalId) {
            clearInterval(animationIntervalId);
            animationIntervalId = null;
        }

        // 标记为暂停状态
        isPaused.value = true;

        // 保持当前显示的站点或路线，不进行任何重新绘制
        // 注意：这里不调用 displayStop 或 displayRoute，以免重新绘制页面
    };


    const stopMarkersMap = ref({});  // 缓存站点
    const routePolylinesMap = ref({});  // 缓存线路

    const displayBusStopsForTime = async (routeId, hour, minute) => {
        try {
            // 获取指定时间点的站点客流数据
            const response = await axios.get(`http://127.0.0.1:5000/api/stop_passenger_flow/${routeId}`, {
                params: {
                    day_type: selectedDay.value.toLowerCase(),
                    hour,
                    minute,
                },
            });

            const stopData = response.data;

            // 获取路线数据
            const routeResponse = await axios.get(`http://127.0.0.1:5000/api/routes/${routeId}`);
            const routeData = routeResponse.data;

            // 获取路线颜色
            const routeColor = getColorByAngle(routeData.angle);

            // 获取最大和最小的 Boardings 和 Load 值
            const maxBoardings = stopData.max_boardings;
            const minBoardings = stopData.min_boardings;
            const maxLoad = stopData.max_load;
            const minLoad = stopData.min_load;

            let previousStop = null;
            const currentStops = new Set(); // 用于记录当前时间步中的站点
            const currentRoutes = new Set(); // 用于记录当前时间步中的线路

            // 遍历站点，更新或创建站点和线路
            stopData.stops.forEach((stop) => {
                const stopId = stop.Stop_Name;
                currentStops.add(stopId);  // 记录当前显示的站点

                let radius;
                let fillColor;
                let routeWeight;

                // 如果 Boardings 是 NaN，则设置为空心圈和默认半径、边框宽度
                if (stop.Boardings === 'NaN') {
                    radius = 5;  // 默认半径
                    fillColor = 'none';  // 空心圈
                    routeWeight = 4;  // 边框宽度为 4
                } else {
                    // 否则，计算半径，设置实心圈和边框宽度
                    radius = 5 + 15 * ((stop.Boardings - minBoardings) / (maxBoardings - minBoardings));
                    radius = Math.max(radius, 5);  // 保证最小半径为 5
                    fillColor = routeColor;  // 使用路线颜色
                    routeWeight = 2;  // 实心圈，边框宽度为 2
                }

                // 如果站点已存在，更新其样式
                if (stopMarkersMap.value[stopId]) {
                    const existingMarker = stopMarkersMap.value[stopId];
                    existingMarker.setLatLng([stop.Latitude, stop.Longitude]);  // 更新位置
                    existingMarker.setRadius(radius);  // 更新半径
                    existingMarker.setStyle({
                        fillColor: fillColor,
                        weight: routeWeight,
                        color: 'white'  // 边框颜色为白色
                    });
                    existingMarker.bindTooltip(`<b>${stop.Stop_Name}</b><br/>Boardings: ${stop.Boardings}`);
                } else {
                    // 创建新的站点
                    const marker = L.circleMarker([stop.Latitude, stop.Longitude], {
                        radius: radius,  // 设置半径
                        color: 'white',  // 边框颜色为白色
                        weight: routeWeight,  // 设置边框宽度
                        fill: true,
                        fillColor: fillColor,  // 设置填充颜色
                        fillOpacity: fillColor === 'none' ? 0 : 1  // 如果为空心圆，填充透明度为 0
                    }).bindTooltip(`<b>${stop.Stop_Name}</b><br/>Boardings: ${stop.Boardings}`).addTo(toRaw(currentLayerGroup.value));
                    marker.bringToFront();  // 确保新创建的标记在前面显示

                    // 缓存新创建的站点
                    stopMarkersMap.value[stopId] = marker;
                }

                // 处理线路部分
                if (previousStop) {
                    const routeKey = `${previousStop.Stop_Name}-${stop.Stop_Name}`; // 以起点和终点的标识符组成唯一的路线键
                    currentRoutes.add(routeKey); // 记录当前显示的线路

                    // 计算线路的粗细，基于载客量（Load）
                    let lineWeight = previousStop.Load !== 'NaN'
                        ? 2 + 30 * ((previousStop.Load - minLoad) / (maxLoad - minLoad))
                        : 2;
                    lineWeight = Math.max(2, lineWeight); // 保证最小线条粗细为 2

                    // 如果线路已存在，更新其样式
                    if (routePolylinesMap.value[routeKey]) {
                        const existingPolyline = routePolylinesMap.value[routeKey];
                        existingPolyline.setStyle({ weight: lineWeight, color: routeColor });  // 更新线路粗细和颜色
                    } else {
                        // 创建新的线路
                        const polyline = L.polyline([
                            [previousStop.Latitude, previousStop.Longitude],
                            [stop.Latitude, stop.Longitude]
                        ], {
                            color: routeColor,
                            weight: lineWeight,
                            opacity: 1
                        }).addTo(toRaw(currentLayerGroup.value)).bringToBack();  // 确保线路在后面显示

                        // 为线路绑定 Tooltip 显示载客量
                        polyline.bindTooltip(`Load: ${previousStop.Load}`, {
                            permanent: false,
                            direction: 'center'
                        });

                        // 缓存新创建的线路
                        routePolylinesMap.value[routeKey] = polyline;
                    }
                }

                previousStop = stop;  // 更新上一个站点
            });

            // 删除不再显示的站点
            for (const stopId in stopMarkersMap.value) {
                if (!currentStops.has(stopId)) {
                    const marker = stopMarkersMap.value[stopId];
                    toRaw(currentLayerGroup.value).removeLayer(marker);  // 从地图上移除
                    delete stopMarkersMap.value[stopId];  // 从缓存中删除
                }
            }

            // 删除不再显示的线路
            for (const routeKey in routePolylinesMap.value) {
                if (!currentRoutes.has(routeKey)) {
                    const polyline = routePolylinesMap.value[routeKey];
                    toRaw(currentLayerGroup.value).removeLayer(polyline);  // 从地图上移除
                    delete routePolylinesMap.value[routeKey];  // 从缓存中删除
                }
            }

            // 更新信息框内容
            const timeInfo = `<div>Time: ${String(hour).padStart(2, '0')}:${String(minute).padStart(2, '0')}</div>`;
            const routeInfo = `<div>Route: ${routeId}</div>`;
            map.value.routeInfoControl.showInfo(routeInfo, timeInfo);

        } catch (error) {
            console.error('Error updating bus stop data:', error);
        }
    };




    // 清除动画时的站点和线路清理逻辑
    const clearBusStopAnimation = () => {
        stopMarkers.value.forEach((marker) => {
            if (currentLayerGroup.value) {
                toRaw(currentLayerGroup.value).removeLayer(marker);
            }
        });
        stopMarkers.value = []; // 清空站点标记数组

        // 清除所有线路
        if (currentLayerGroup.value) {
            toRaw(currentLayerGroup.value).clearLayers();
        }
    };

    const switchView = (view) => {
      emit('switch-view', view);
      activeMenu.value = view;
    };

    watch(lineWeight, () => {
      applyAngleRange();
    });

    watch(colorMode, () => {
      toggleColorMode();
    });

    watch(colorOption, () => {
      handleColorChange();
    });

    // 观察 selectedHour 的变化，当它改变时，将 selectedMinute 重置为 0
    watch(selectedHour, () => {
        selectedMinute.value = 0;
        fetchPassengerFlowData();  // 当小时变化时，自动获取新的数据
    });

    watch([selectedHour, selectedMinute], () => {
      if (selectedStop.value === '2' && selectedBus.value) {
        displayStop(selectedBus.value);
      }
    });

    watch(selectedStop, (newValue) => {
      if (selectedBus.value) {
        if (newValue === '1') {
          displayRoute(selectedBus.value);
        } else if (newValue === '2') {
          displayStop(selectedBus.value);
        }
      }
    });

    onMounted(() => {
  // 定义 L.Popup 的动画行为（你已有的代码）
      L.Popup.prototype._animateZoom = function (e) {
        if (!this._map) return;
        var pos = toRaw(this._map)._latLngToNewLayerPoint(this._latlng, e.zoom, e.center),
          anchor = this._getAnchor();
        L.DomUtil.setPosition(this._container, pos.add(anchor));
      };

      // 初始化地图（你已有的代码）
      map.value = L.map('map').setView(initialState.center, initialState.zoom);
      currentLayerGroup.value = L.layerGroup().addTo(toRaw(map.value));
      mapInitialized.value = true;
      updateMapLayer();

      // 加载并应用颜色映射关系
      categories.value = tabsDataWithColors;
      categories.value.forEach((category) => {
        category.numbers.forEach((number, index) => {
          lineColors.value[number] = category.colors[index];
        });
      });

      // 检查时间开关状态，并根据不同情况加载数据（你已有的代码）
      if (timePeriodSwitch.value) {
        fetchDailyPassengerFlow(selectedDay.value);
      } else {
        fetchPassengerFlowRoutes();
      }

      const routeInfoControl = new RouteInfoControl();
      routeInfoControl.addTo(toRaw(map.value));
      routeInfoControl.hideInfo();
      map.value.routeInfoControl = routeInfoControl;
    });

    onBeforeUnmount(() => {
      mapInitialized.value = false;
      if (map.value) {
        map.value.off(); // 解绑所有事件
        map.value.remove(); // 清除地图
        map.value = null;
      }
      if (currentLayerGroup.value) {
        toRaw(currentLayerGroup.value).clearLayers(); // 在这里使用 toRaw
        currentLayerGroup.value = null;
      }
    });

    return {
      lineWeight,
      colorMode,
      reset,
      radio,
      handleRadioChange,
      angleRange,
      handleAngleChange,
      colorOption,
      handleColorChange,
      validateAngle,
      applyAngleRange,
      activeMenu,
      switchView,
      selectedStop,
      onSliderInput,
      onSliderChange,
      timePeriodSwitch,
      selectedDay,
      fetchDailyPassengerFlow,
      handleTimePeriodChange,
      categories,
      selectedCategory,
      selectCategory,
      selectedBus,
      selectBus,
      selectedHour,
      selectedMinute,
      fetchPassengerFlowData,
      handleStopChange,
      toggleBusStopAnimation,
      animate,
      lineColors,
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
  margin-bottom: 10px;
  width: 100%;
  display: flex;
  justify-content: center;
}

.knob-radio-container {
  border: 3px solid #9bbef8;
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

.category-container {
  display: flex;
  flex-direction: column;
  width: 100%;
  align-items: center;
}

.category-menu {
  display: grid;
  grid-template-columns: repeat(5, 1fr);
  gap: 8px;
  margin-top: 20px;
  font-size: 0.8em;
}

.category-menu button {
  padding: 5px;
  height: 30px;
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
  grid-template-columns: repeat(8, 1fr);
  gap: 5px;
  margin-top: 10px;
  width: 100%;
}

.bus-list button {
  color: white;
  height: 30px;
  border: none;
  background-color: #f0f8ff;
  cursor: pointer;
  text-align: center;
  line-height: 25px;
  border-radius: 3px;
  font-size: 0.9em;
  text-shadow: 1px 1px 3px black; /* 添加黑色文本阴影 */
  padding: 2px;
}

.bus-list button.bus-active {
  font-weight: bold;
  border: 2px solid;
  box-shadow: 0 0 0 2px black;
  text-shadow: 1px 1px 3px black; /* 选中时依然保持阴影 */
}

.selectedStop {
  margin-top: 20px;
  display: flex;
  justify-content: center;
}

.slider-long {
  width: 300px;
}

.animation-button-container {
  display: flex;
  justify-content: center; /* 居中 */
  margin-top: 20px; /* 与上面的按钮保持一定距离 */
}
</style>
