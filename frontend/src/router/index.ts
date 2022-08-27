import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("../pages/index.vue"),
  },
  {
    path: "/:chainId/pool/:lpAddress",
    component: () => import("../pages/_lpAddress.vue"),
  },
  {
    path: "/exchange",
    component: () => import("../pages/exchange/index.vue"),
  },
  {
    path: "/:chainId/exchange/:exchange",
    component: () => import("../pages/exchange/_exchange.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
