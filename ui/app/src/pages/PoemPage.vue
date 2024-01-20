<script setup lang="ts">
import {useRoute} from 'vue-router'
import CenteredContainer from 'layouts/CenteredContainer.vue'
import {useCoreStore} from 'stores/core-store'
import {onMounted, ref} from 'vue'
import {Poem, PoemByLines, TextItem} from '../models'
import MetadataComponent from 'components/MetadataComponent.vue'
import TooltipComponent from 'components/TooltipComponent.vue'

const coreStore = useCoreStore()
const route = useRoute()
const poem = ref<Poem | null>(null)
const poem_id = ref<string | null>(null)
const author_id = ref<string | null>(null)

onMounted(() => {
  const _author_id = route.params.author_id.toString()
  const _poem_id = route.params.poem_id.toString()
  poem_id.value = _poem_id
  author_id.value = _author_id
  poem.value = coreStore.findPoem(_author_id, _poem_id)
})

const aggregatePoemTextByLine = () => {
  const lines: PoemByLines = {}
  if (poem.value) {
    poem.value.text.forEach((token: TextItem) => {
      if (token.line_number in lines) {
        lines[token.line_number].push(token)
      } else {
        lines[token.line_number] = [token]
      }
    })
  }
  return lines
}
</script>

<template>
  <CenteredContainer title_class="tw-text-green-500" v-if="poem" :title="poem.title" max-width="2000px">
    <div class="fit row wrap justify-evenly items-start content-start">
      <q-list dense>
        <q-item
          class="text-left"
          v-for="(line, index) in Object.entries(aggregatePoemTextByLine())"
          :key="`line_${index}`">
          <q-item-section class="text-body1">
            <table class="q-ml-lg">
              <tr>
                <td class="number_cell"
                  ><span class="text-grey-6"> {{ (index + 1) % 5 === 0 ? `${index + 1}` : ' ' }}</span></td
                >
                <td>
                  <p>
                    <span
                      v-for="(token, ind) in line[1]"
                      :key="`token_${ind}`"
                      class="cursor-pointer hover:tw-text-blue-700 tw-font-sans">
                      {{ token.token.trim() }}
                      <!--                    {{-->
                      <!--                      token.pos === 'PUNCT'-->
                      <!--                        ? `${token.token}`-->
                      <!--                        : ind === 0-->
                      <!--                        ? `${token.token}`-->
                      <!--                        : `${token.token}`-->
                      <!--                    }}-->
                      <q-tooltip> <TooltipComponent :token="token" /></q-tooltip>
                    </span>
                  </p>
                </td>
              </tr>
            </table>
          </q-item-section>
        </q-item>
      </q-list>
      <MetadataComponent :author_id="author_id" :poem_id="poem_id" />
    </div>
  </CenteredContainer>
</template>

<style scoped lang="scss">
.border {
  border: 1px solid green;
  padding: 10px;
  margin-bottom: 10px;
}

.number_cell {
  width: 40px;
  padding-right: 10px;
}
</style>
