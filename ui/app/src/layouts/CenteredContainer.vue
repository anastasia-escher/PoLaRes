<script setup lang="ts">
const props = defineProps({
  title: {
    type: String,
    required: false,
  },
  maxWidth: {
    type: String,
    required: false,
  },
  title_class: {
    type: String,
    required: false,
  },
})
</script>

<template>
  <q-page class="tw-flex-center">
    <section class="tw-py-16 md:tw-py-16 tw-bg-white centered">
      <div class="tw-container tw-px-4 tw-mx-auto centered">
        <h4
          :class="props.title_class"
          v-if="props.title"
          class="text-center tw-mb-4 tw-text-xl md:tw-text-2xl tw-leading-tight tw-text-darkCoolGray-900 tw-font-bold tw-tracking-tighter">
          {{ props.title }}
        </h4>
        <div class="q-pa-md centered additional"><slot name="additional_info"></slot></div>
        <div class="q-pa-md centered" :style="{maxWidth: props.maxWidth}">
          <slot></slot>
        </div>
      </div>
    </section>
  </q-page>
</template>

<style scoped lang="scss">
.centered {
  margin: 0 auto;
}

.additional {
  width: 70%;
}
</style>
