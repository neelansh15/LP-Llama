import { defineStore } from "pinia";

export const useStore = defineStore("web3store", {
  state: () => ({
    colors: {
      primary: "#059669",
      secondary: "#047857",
      tertiary: "#047857",
    },
  }),
});
