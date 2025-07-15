import { fileURLToPath, URL } from "node:url";

import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";

const API_BASE_URL =
  process.env.NODE_ENV === "production"
    ? "https://web-scrapper-production-916c.up.railway.app/api/"
    : "http://localhost:8000/api";

export default defineConfig({
  base: process.env.NODE_ENV === "production" ? "/wired-scraper/" : "/",
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
});
