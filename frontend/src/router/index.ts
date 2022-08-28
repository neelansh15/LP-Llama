import { createRouter, createWebHistory } from "vue-router";

const routes = [
  {
    path: "/",
    component: () => import("../pages/index.vue"),
  },
  {
    path: "/:chainId/:exchange/:lpAddress",
    component: () => import("../pages/_lpAddress.vue"),
  },
  {
    path: "/exchanges",
    component: () => import("../pages/exchange/index.vue"),
  },
  {
    path: "/:chainId/:exchange",
    component: () => import("../pages/exchange/_exchange.vue"),
  },
  {
    path: "/chains",
    component: () => import("../pages/chains/index.vue"),
  },
];

const router = createRouter({
  routes,
  history: createWebHistory(),
});

export default router;
