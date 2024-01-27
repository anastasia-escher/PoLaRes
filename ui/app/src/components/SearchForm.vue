<script setup lang="ts">
import {ref} from 'vue'
import {useCoreStore} from 'stores/core-store'
import {storeToRefs} from 'pinia'
import {TextItem} from '../models'
import {useQuasar} from 'quasar'

const $q = useQuasar()

import ResultsTable from 'components/ResultsTable.vue'
const coreStore = useCoreStore()
const {data} = storeToRefs(coreStore)

const query = ref<string>('')
const lemmaQuery = ref<string>('')

const searchResults = ref<any>([])

const searchHasGivenNoResults = ref<boolean>(false)

const getContextIfMatch = (textArray: TextItem[], query: string, type: 'full' | 'lemma') => {
  let queryTokens = query.split(' ').map(token => token.toLowerCase())
  let matchedIndex = -1

  if (type === 'lemma') {
    for (let i = 0; i < textArray.length; i++) {
      if (textArray[i].lemma.toLowerCase() === lemmaQuery.value) {
        let matchFound = true
        if (matchFound) {
          matchedIndex = i
          break
        }
      }
    }
  } else {
    for (let i = 0; i < textArray.length; i++) {
      if (textArray[i].token.toLowerCase() === queryTokens[0]) {
        let matchFound = true
        for (let j = 1; j < queryTokens.length; j++) {
          if (textArray[i + j].token.toLowerCase() !== queryTokens[j]) {
            matchFound = false
            break
          }
        }

        if (matchFound) {
          matchedIndex = i
          break
        }
      }
    }
  }
  if (matchedIndex == -1) {
    return null
  }

  // get context lines

  const indicesToHighlight = Array.from(Array(queryTokens.length).keys()).map(index => matchedIndex + index)

  const _textArray = textArray.map((token, index) => {
    return {...token, highlight: indicesToHighlight.includes(index)}
  })

  let startLine = Math.max(1, parseInt(_textArray[matchedIndex].line_number) - 2)
  let endLine = parseInt(_textArray[matchedIndex + queryTokens.length - 1].line_number) + 2

  let context = _textArray.filter(token => {
    let line_number = parseInt(token.line_number)
    return line_number >= startLine && line_number <= endLine
  })

  return aggregateResultByLines(context)
}

const searchInData = (query: string, type: 'full' | 'lemma') => {
  console.log('searching in data')
  const _results = []

  for (const authorId in data.value) {
    for (const poemId in data.value[authorId]) {
      const poem = data.value[authorId][poemId]
      const context = getContextIfMatch(poem.text, query, type)
      if (context) {
        _results.push({
          authorId: authorId,
          poemId: poemId,
          title: poem.title,
          context: context,
        })
      }
    }
  }

  searchResults.value = _results
  if (_results.length === 0) {
    $q.notify({
      message: 'No results found',
      color: 'warning',
      position: 'center',
      icon: 'report_problem',
    })
  }
}

const handleSubmit = (type: 'lemma' | 'full') => {
  searchInData(query.value, type)
}

const aggregateResultByLines = (tokens: TextItem[]) => {
  const lines: any = {}
  for (let i = 0; i < tokens.length; i++) {
    const token = tokens[i]

    if (token.line_number in lines) {
      lines[token.line_number].push(token)
    } else {
      lines[token.line_number] = [token]
    }
  }
  return lines
}
</script>

<template>
  <section class="tw-relative tw-pb-52">
    <img
      class="tw-absolute tw-bottom-0 tw-left-0 tw-w-full tw-h-full tw-object-cover"
      src="../assets/bg.jpg"
      alt="" />
    <div class="tw-relative tw-container tw-px-4 tw-mx-auto">
      <div
        class="tw-max-w-md tw-mx-auto md:tw-max-w-none tw-py-16 tw-px-6 sm:tw-px-12 md:tw-px-24 tw-bg-white tw-rounded-md tw-shadow">
        <div class="tw-flex tw-flex-wrap tw--mx-4">
          <!--    _________________________      NOTES  ___________________________             -->

          <div class="tw-w-full lg:tw-w-1/3 tw-px-2 tw-mb-4 lg:tw-mb-0">
            <div class="tw-max-w-xxl">
              <span class="tw-text-sm tw-font-semibold tw-uppercase tw-text-gray-700">
                Note on orthography
              </span>

              <div class="tw--mx-2">
                <div class="tw-px-2 tw-mb-8 sm:tw-mb-0">
                  <p class="tw-text-sm tw-leading-6 tw-text-gray-500">
                    Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt
                    ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                    ullamco laboris nisi ut aliquip ex ea commodo consequat.
                  </p>
                </div>
              </div>
            </div>
          </div>
          <!--     ______________________      END NOTES ____________________________   -->

          <!--     ___________________      FORM   ____________________________    -->
          <div class="tw-w-full lg:tw-w-1/2 tw-px-4">
            <div>
              <h4 class="ftw-ont-heading tw-text-lg tw-font-medium tw-mb-4">Full text search</h4>
              <form>
                <div class="tw-mb-4 tw-flex tw-flex-row">
                  <input
                    v-model="query"
                    class="tw-block tw-w-full tw-p-4 tw-font-heading tw-text-gray-800 tw-placeholder-gray-400 tw-bg-gray-50 tw-rounded tw-outline-none"
                    type="text"
                    placeholder="Type a word or a phrase" />

                  <q-icon
                    @click="handleSubmit('full')"
                    class="q-ml-md cursor-pointer"
                    size="lg"
                    color="secondary"
                    name="forward"></q-icon>
                </div>
              </form>
              <form>
                <h4 class="ftw-ont-heading tw-text-lg tw-font-medium tw-mb-4">Search by lemma</h4>
                <div class="tw-mb-4 tw-flex tw-flex-row">
                  <input
                    v-model="lemmaQuery"
                    class="tw-block tw-w-full tw-p-4 tw-font-heading tw-text-gray-800 tw-placeholder-gray-400 tw-bg-gray-50 tw-rounded tw-outline-none"
                    type="text"
                    placeholder="Type the initial for of a word" />

                  <q-icon
                    @click="handleSubmit('lemma')"
                    class="q-ml-md cursor-pointer"
                    size="lg"
                    color="secondary"
                    name="forward"></q-icon>
                </div>
              </form>
            </div>

            <!-- _________________________      END FORM  ___________________________             -->
          </div>
        </div>
      </div>

      <br />
      <br />
    </div>
    <div class="tw-relative tw-container tw-px-4 tw-mx-auto" v-if="searchResults.length > 0">
      <ResultsTable :search-results="searchResults" />

      <!--          {{ searchResults }}-->
    </div>
  </section>
</template>
<style scoped lang="scss">
.border {
  border: 1px solid green;
  padding: 10px;
  margin-bottom: 10px;
}
</style>
