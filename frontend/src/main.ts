import { createApp, inject } from "vue";
import "./style.css";
import App from "./App.vue";

import { createPinia } from "pinia";
import router from "./router";

import "virtual:windi.css";

const app = createApp(App).use(createPinia()).use(router).mount("#app");
