<script setup lang="ts">
import {computed} from "vue";
import {useRouter} from "vue-router";
import {onMounted} from "vue";
import {useCoreStore} from "stores/core-store";
import {storeToRefs} from "pinia";

onMounted(() => {
  console.log("mounted");
});

const router = useRouter();

const coreStore = useCoreStore();
const {data, authorsData} = storeToRefs(coreStore);

const sortedAuthors = computed(() => {
  return [...authorsData.value].sort((a, b) => {
    if (a.last_name < b.last_name) {
      return -1;
    }
    if (a.last_name > b.last_name) {
      return 1;
    }

    return 0;
  });
});

const findTexts = (author_id: string) => {
  return Object.entries(data.value[author_id]).map(([key, value]) => {
    return {title: value.title, id: key};
  });
};

const handlePoemClick = (poem_id: string, author_id: string) => {
  console.log(poem_id);
  router.push(`/poems/${author_id}/${poem_id}`);
};
</script>

<template>
  <q-list class="big_text">
    <q-expansion-item
      v-for="author in sortedAuthors"
      :key="author.author_id"
      expand-separator
      icon="perm_identity"
      label="Account settings"
      caption="John Doe">
      <template v-slot:header>
        <q-item-section>
          <q-item-label class="text-blue-8 cursor-pointer">
            {{ author.last_name }}, {{ author.first_name }}
          </q-item-label>
          <q-item-label caption lines="2">Some additional information about the author</q-item-label>
        </q-item-section>

        <q-item-section side center>
          <q-item-label caption>1623-1667</q-item-label>
        </q-item-section>
      </template>
      <q-card>
        <q-card-section>
          <div
            @click="handlePoemClick(poem.id, author.author_id)"
            class="text-body1 text-indigo-7 cursor-pointer q-ml-lg"
            v-for="(poem, index) in findTexts(author.author_id)"
            :key="poem.title">
            {{ index + 1 }}. {{ poem.title }}
          </div>
        </q-card-section>
      </q-card>
    </q-expansion-item>
  </q-list>
</template>

<style scoped lang="scss">
.big_text {
  font-size: 18px;
}
</style>
