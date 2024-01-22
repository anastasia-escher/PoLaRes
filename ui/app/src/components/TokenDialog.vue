<script setup lang="ts">
import {TextItem} from 'src/models'
import {PropType, defineProps} from 'vue'
import {useCoreStore} from 'stores/core-store'

const coreStore = useCoreStore()

const props = defineProps({
  token: {
    type: Object as PropType<TextItem>,
    required: true,
  },
})

const deleteBrackets = (str: string) => {
  return str.replace(/[{(\[\])}]/g, '')
}
</script>

<template>
  <q-card flat bordered class="my-card">
    <q-card-section class="row items-center q-pb-none">
      <div class="text-h6 tw-text-green-500"
        >Morphological analysis: <b>{{ props.token.token }}</b></div
      >
      <q-space></q-space>
      <q-btn icon="close" flat round dense v-close-popup></q-btn>
    </q-card-section>

    <q-card-section class="q-pt-none"> </q-card-section>
    <q-list class="rounded-borders">
      <q-expansion-item
        expand-separator
        icon="computer"
        label="All possible interpretations"
        caption="(accuracy ca. 90%)">
        <q-card class="q-ml-lg">
          <q-card-section v-if="props.token">
            <div v-for="form in coreStore.findForm(props.token.token.trim().toLowerCase())" :key="form">
              <p v-html="form"></p>
            </div>
          </q-card-section>
        </q-card>
      </q-expansion-item>
      <q-separator inset></q-separator>
      <q-expansion-item
        icon="help_outline"
        label="Predicted form"
        caption="(not proofread, accuracy ca. 70%)">
        <q-card class="q-ml-lg">
          <q-card-section>
            <div v-if="props.token">
              <p><span class="text-bold">Lemma: </span> {{ props.token.lemma }}</p>
              <p><span class="text-bold">Part of speach: </span> {{ props.token.pos }}</p>
              <p class="text-bold">Morphosyntactic features: </p>
              <p v-for="item in props.token.morphosyntactic_features.split(',')" :key="item">{{
                deleteBrackets(item)
              }}</p>
            </div>
          </q-card-section>
        </q-card>
      </q-expansion-item>
    </q-list>
  </q-card>
</template>

<style scoped lang="scss">
.my-card {
  width: 40%;
  padding: 10px;
  padding-bottom: 20px;
}
</style>
