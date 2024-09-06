<template>
  <div id="app">
    <component :is="currentViewComponent" @switch-view="switchView" />
  </div>
</template>

<script>
import RoutesView from './components/RoutesView.vue';
import PassengerFlowView from './components/PassengerFlowView.vue';

export default {
  name: 'App',
  components: {
    RoutesView,
    PassengerFlowView,
  },
  data() {
    return {
      currentView: 'routes', // 默认显示RoutesView
    };
  },
  computed: {
    currentViewComponent() {
      // 根据currentView动态返回组件
      return this.currentView === 'routes' ? 'RoutesView' : 'PassengerFlowView';
    },
  },
  methods: {
    switchView(view) {
      // 切换视图方法
      this.currentView = view;
    },
  },
};
</script>

<style>
html, body, #app {
  height: 100%;
  margin: 0;
  overflow: hidden;
}

#app {
  display: flex;
  flex-direction: column;
}
</style>