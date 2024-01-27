import {defineStore} from 'pinia'
import {ref} from 'vue'
import {Root, Author, MetadataItem} from '../models'
import text_data from 'src/data/text_data.json'
import meta from 'src/data/metadata.json'
import forms from 'src/data/forms.json'
import {authors} from '../data/corpus_data'
import {TextItem} from '../models'

export const useCoreStore = defineStore('core', () => {
  const data = ref<Root>(text_data as Root)
  const metadata = ref<MetadataItem[]>(meta as MetadataItem[])
  const authorsData = ref<Author[]>(authors)
  const formsData = ref<{[key: string]: string}>(forms)

  const findPoem = (authorId: string, poemId: string) => {
    return data.value[authorId][poemId]
  }

  const findMetadata = (poemId: string) => {
    return metadata.value.find(item => item.text_id === poemId)
  }

  const findAuthor = (authorId: string) => {
    return authorsData.value.find(item => item.author_id === authorId)
  }

  const findForm = (token: string) => {
    const formsRaw = formsData.value[token]
    if (formsRaw) {
      return formsRaw.split(';')
    }
  }

  return {
    data,
    authorsData,
    metadata,
    formsData,
    findPoem,
    findMetadata,
    findAuthor,
    findForm,
  }
})
