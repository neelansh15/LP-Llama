import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("../pages/index.vue"),
  },
  {
    path: "/pool/:chainId/:lpAddress",
    component: () => import("../pages/_lpAddress.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
