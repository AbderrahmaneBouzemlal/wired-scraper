import { fileURLToPath, URL } from "node:url";
import { defineConfig } from "vite";
import vue from "@vitejs/plugin-vue";
import vueDevTools from "vite-plugin-vue-devtools";

export default defineConfig({
  base: "/",
  plugins: [vue(), vueDevTools()],
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
  build: {
    outDir: "dist",
    assetsDir: "assets",
  },
  server: {
    proxy: {
      "/api": {
        target: "https://web-scrapper-production-916c.up.railway.app",
        changeOrigin: true,
        secure: true,
      },
    },
  },
});
