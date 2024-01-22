<script setup lang="ts">
import {ref} from 'vue'

const leftDrawerOpen = ref(false)
const rightDrawerOpen = ref(false)

const toggleRightDrawer = () => {
  rightDrawerOpen.value = !rightDrawerOpen.value
}

// const toggleLeftDrawer = () => {
//   leftDrawerOpen.value = !leftDrawerOpen.value
// }
</script>

<template>
  <q-layout view="hHh lpR fFf">
    <q-header elevated class="header text-white" height-hint="98">
      <q-toolbar>
        <!--        <q-btn dense flat round icon="menu" @click="toggleLeftDrawer" />-->

        <q-toolbar-title class="tw-text-xl"> Poetae Latini Regni Sveciae </q-toolbar-title>

        <!--        <q-btn dense flat round icon="menu" @click="toggleRightDrawer" />-->
      </q-toolbar>

      <q-tabs align="center" class="q-mt-lg">
        <q-route-tab to="/" label="Home" />
        <!--        <q-route-tab to="/search" label="Search" />-->
        <q-route-tab to="/library" label="Library" />
        <q-route-tab to="/about" label="About" />
      </q-tabs>
    </q-header>

    <!--    <q-drawer :show-if-above="false" v-model="leftDrawerOpen" side="left" bordered>-->
    <!--      &lt;!&ndash; drawer content &ndash;&gt;-->
    <!--    </q-drawer>-->

    <q-page-container>
      <router-view />
    </q-page-container>

    <q-footer elevated class="bg-grey-5 text-white">
      <q-toolbar>
        <q-toolbar-title>
          <div>University of Lund {{ new Date().getFullYear() }}</div>
        </q-toolbar-title>
      </q-toolbar>
    </q-footer>
  </q-layout>
</template>

<style lang="scss">
@import 'tailwindcss/base';
@import 'tailwindcss/components';
@import 'tailwindcss/utilities';

.bg-container {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-position: center;
  z-index: -1;
}

.q-header,
.q-drawer {
  background-color: rgba(255, 255, 255, 0.7);
}

.header {
  background-image: url('assets/books.jpg');
  background-size: cover;
  background-position: center;
  color: #fff;
  height: 150px;
}
</style>
