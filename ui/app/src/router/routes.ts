import {RouteRecordRaw} from 'vue-router'

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      {path: '', component: () => import('pages/IndexPage.vue')},
      {path: '/search', component: () => import('pages/SearchPage.vue')},
      {path: '/library', component: () => import('pages/LibraryPage.vue')},
      {path: '/about', component: () => import('pages/AboutPage.vue')},
      {path: '/library/poems/:author_id/:poem_id', component: () => import('pages/PoemPage.vue')},
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
]

export default routes
