import { defineStore } from "pinia";

export const useStore = defineStore("web3store", {
  state: () => ({
    address: null as string | null,
  }),
});
