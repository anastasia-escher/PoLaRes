<script setup lang="ts">
import {TextItem} from 'src/models'
import {PropType, defineProps} from 'vue'

const props = defineProps({
  token: {
    type: Object as PropType<TextItem>,
    required: true,
  },
})

const deleteBrackets = (str: string) => {
  return str.replace(/[{()}]/g, '')
}
</script>

<template>
  <div v-if="props.token" class="tooltip">
    <h5 class="text-blue-2">Predicted form (accuracy ca. 70%)</h5>
    <p><span class="text-bold">Lemma: </span> {{ props.token.lemma }}</p>
    <p><span class="text-bold">Part of speach: </span> {{ props.token.pos }}</p>
    <p class="text-bold">Morphosyntactic features: </p>
    <p v-for="item in props.token.morphosyntactic_features.split(',')" :key="item">{{
      deleteBrackets(item)
    }}</p>
  </div>
</template>

<style scoped lang="scss">
.tooltip {
  font-size: 1.1rem;
}
</style>
