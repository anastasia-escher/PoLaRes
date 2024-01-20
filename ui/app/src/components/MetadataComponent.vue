<script setup lang="ts">
import {useCoreStore} from 'stores/core-store'
import {MetadataItem, Author} from 'src/models'
import {ref, onMounted, computed} from 'vue'

const props = defineProps({
  poem_id: {
    type: String,

    required: true,
  },
  author_id: {
    type: String,
    required: true,
  },
})

const coreStore = useCoreStore()

onMounted(() => {
  const _author = coreStore.findAuthor(props.author_id)
  if (_author) {
    author.value = _author
  }
  const _metadata = coreStore.findMetadata(props.poem_id)
  if (_metadata) {
    poemMetadata.value = _metadata
  }
})
const poemMetadata = ref<MetadataItem | null>(null)
const author = ref<Author | null>(null)

const metadataFields = computed(() => {
  if (!poemMetadata.value || !author.value) return []

  return [
    {
      icon: 'person',
      label: 'author',
      value: `${author.value.first_name} ${author.value.last_name}`,
    },
    {
      icon: 'calendar_today',
      label: 'year',
      value: poemMetadata.value.date,
    },
    {
      icon: 'history_edu',
      label: 'metre',
      value: poemMetadata.value.metre,
    },
    {
      icon: 'draw',
      label: 'genres',
      value: poemMetadata.value.genres,
    },
    {
      icon: 'portrait',
      label: 'associated person',
      value: poemMetadata.value.associated_person,
      url: poemMetadata.value.associated_person_url,
    },
    {
      icon: 'menu_book',
      label: 'text source',
      value: poemMetadata.value.text_source,
      url: poemMetadata.value.text_source_url,
    },
  ]
})
</script>

<template>
  <div class="tw-mt-20 tw-mb-6 p-6 tw-border-l-2 tw-border-green-500">
    <div class="q-pa-md" style="max-width: 500px">
      <q-list v-if="metadataFields.length">
        <q-item v-for="(field, index) in metadataFields" :key="index" v-ripple>
          <q-item-section avatar>
            <q-icon color="secondary" :name="field.icon"></q-icon>
          </q-item-section>
          <q-item-section>
            <a v-if="field.url" :href="field.url" target="_blank" class="text-blue-6 cursor-pointer">
              {{ field.value }}
            </a>
            <template v-else>{{ field.value }}</template>
          </q-item-section>
          <q-item-section caption side>{{ field.label }}</q-item-section>
        </q-item>
      </q-list>
    </div>
  </div>
</template>

<style scoped lang="scss"></style>
