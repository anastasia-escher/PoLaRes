<script setup lang="ts">
import TokenDialog from 'components/TokenDialog.vue'
import {TextItem} from 'src/models'
import {ref} from 'vue'
import {useCoreStore} from 'stores/core-store'
import {useRouter} from 'vue-router'

const coreStore = useCoreStore()
const router = useRouter()

const props = defineProps({
  searchResults: {
    type: Array,
    required: true,
  },
})

const columns = [
  {
    name: 'author',
    field: 'authorId',
    required: true,
    label: 'Author',
    align: 'left',
    sortable: true,
  },
  {name: 'title', align: 'left', label: 'Title', field: 'title', sortable: true},
  {name: 'context', label: 'Text', field: 'context', sortable: false, align: 'left'},
]

const handleTitleClick = (author_id: string, poem_id: string) => {
  console.log(poem_id)
  router.push(`library/poems/${author_id}/${poem_id}`)
}

const getAuthorFullName = (authorId: string) => {
  const author = coreStore.findAuthor(authorId)
  if (author) {
    return `${author.last_name} ${author.first_name}`
  }
}

const handleTokenClick = (token: TextItem) => {
  selectedToken.value = token
  tokenDialogOpen.value = true
}

const tokenDialogOpen = ref<boolean>(false)
const selectedToken = ref<TextItem | null>(null)
</script>

<template>
  <q-table
    flat
    bordered
    title="Results"
    :rows="props.searchResults"
    :columns="columns"
    row-key="context"
    class="tw-text-gray-500 tw-text-lg">
    <template v-slot:body-cell-author="props">
      <q-td :props="props">
        <div>
          <a @click="handleTitleClick(props.row.authorId, props.row.poemId)">{{
            getAuthorFullName(props.value)
          }}</a>
        </div>
      </q-td>
    </template>
    <template v-slot:body-cell-title="props">
      <q-td :props="props">
        <div>
          <a
            class="cursor-pointer text-blue-8"
            @click="handleTitleClick(props.row.authorId, props.row.poemId)"
            >{{ props.value }}</a
          >
        </div>
      </q-td>
    </template>
    <template v-slot:body-cell-context="props">
      <q-td :props="props">
        <div
          class="tw-text-gray-900 tw-text-lg"
          v-for="(line, index) in Object.entries(props.value)"
          :key="props.row.title + index">
          <span
            :class="token.highlight ? 'tw-text-red-700' : ''"
            class="tw-text-green-900 cursor-pointer tw-font-sans"
            @click="handleTokenClick(token)"
            v-for="(token, tokenInd) in line[1]"
            :key="token + tokenInd + props.row.title">
            {{
              token.pos === 'PUNCT' ? `${token.token}` : tokenInd === 0 ? `${token.token}` : ` ${token.token}`
            }}</span
          >
        </div>
      </q-td>
      <q-dialog v-model="tokenDialogOpen" persistent>
        <TokenDialog :token="selectedToken" />
      </q-dialog>
    </template>
  </q-table>
</template>

<style scoped lang="scss"></style>
