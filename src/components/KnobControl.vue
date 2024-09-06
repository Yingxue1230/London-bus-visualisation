<template>
  <div
    class="knob-container"
    @mousedown="startDrag"
    @touchstart="startDrag"
    :style="{ width: size + 'px', height: size + 'px' }"
  >
    <svg :width="size" :height="size" viewBox="0 0 100 100">
      <circle
        class="knob-background"
        cx="50"
        cy="50"
        r="45"
        :stroke-width="strokeWidth"
      />
      <path
        class="knob-range"
        :d="rangePath"
        :stroke-width="strokeWidth"
      />
      <circle
        class="knob-handle"
        :cx="handleMin.x"
        :cy="handleMin.y"
        r="5"
        @mousedown="startDragMin"
        @touchstart="startDragMin"
      />
      <circle
        class="knob-handle"
        :cx="handleMax.x"
        :cy="handleMax.y"
        r="5"
        @mousedown="startDragMax"
        @touchstart="startDragMax"
      />
    </svg>
  </div>
</template>

<script>
export default {
  name: "KnobControl",
  props: {
    modelValue: {
      type: Array,
      required: true
    },
    min: {
      type: Number,
      default: 0
    },
    max: {
      type: Number,
      default: 360
    },
    step: {
      type: Number,
      default: 1
    },
    size: {
      type: Number,
      default: 100
    },
    strokeWidth: {
      type: Number,
      default: 5
    }
  },
  computed: {
    handleMin() {
      return this.calculateHandlePosition(this.modelValue[0]);
    },
    handleMax() {
      return this.calculateHandlePosition(this.modelValue[1]);
    },
    rangePath() {
      const start = this.calculateHandlePosition(this.modelValue[0]);
      const end = this.calculateHandlePosition(this.modelValue[1]);

      const largeArcFlag = (this.modelValue[1] - this.modelValue[0] + 360) % 360 <= 180 ? "0" : "1";
      return `M ${start.x} ${start.y} A 45 45 0 ${largeArcFlag} 1 ${end.x} ${end.y}`;
    }
  },
  methods: {
    calculateHandlePosition(angle) {
      const rad = (angle - 90) * (Math.PI / 180);
      return {
        x: 50 + 45 * Math.cos(rad),
        y: 50 + 45 * Math.sin(rad)
      };
    },
    startDrag(event) {
      event.preventDefault();
      document.addEventListener("mousemove", this.onDrag);
      document.addEventListener("mouseup", this.stopDrag);
      document.addEventListener("touchmove", this.onDrag);
      document.addEventListener("touchend", this.stopDrag);
      this.onDrag(event);
    },
    startDragMin(event) {
      this.draggingMin = true;
      this.startDrag(event);
    },
    startDragMax(event) {
      this.draggingMax = true;
      this.startDrag(event);
    },
    onDrag(event) {
      const rect = this.$el.getBoundingClientRect();
      const centerX = rect.left + rect.width / 2;
      const centerY = rect.top + rect.height / 2;
      const clientX = event.touches ? event.touches[0].clientX : event.clientX;
      const clientY = event.touches ? event.touches[0].clientY : event.clientY;
      const deltaX = clientX - centerX;
      const deltaY = clientY - centerY;
      let angle = Math.atan2(deltaY, deltaX) * (180 / Math.PI) + 90;
      if (angle < 0) angle += 360;

      const valueRange = this.max - this.min;
      const stepValue = Math.round((angle / 360) * valueRange / this.step) * this.step + this.min;

      if (this.draggingMin) {
        this.$emit("update:modelValue", [stepValue, this.modelValue[1]]);
      } else if (this.draggingMax) {
        this.$emit("update:modelValue", [this.modelValue[0], stepValue]);
      }
    },
    stopDrag() {
      this.draggingMin = false;
      this.draggingMax = false;
      document.removeEventListener("mousemove", this.onDrag);
      document.removeEventListener("mouseup", this.stopDrag);
      document.removeEventListener("touchmove", this.onDrag);
      document.removeEventListener("touchend", this.stopDrag);
      this.$emit('change', this.modelValue);
    }
  },
  data() {
    return {
      draggingMin: false,
      draggingMax: false
    };
  }
};
</script>

<style scoped>
.knob-container {
  display: inline-block;
  position: relative;
  user-select: none;
  touch-action: none;
}

.knob-background {
  fill: none;
  stroke: #ccc;
}

.knob-range {
  fill: none;
  stroke: #5a9cf8;
}

.knob-handle {
  fill: #5a9cf8;
  stroke: none;
  cursor: pointer;
}
</style>
