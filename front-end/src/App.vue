<script setup>
import { ref, onMounted } from "vue";
import jsonData from "../../wired_data.json";

import axios from "axios";

const items = ref([]);

items.value = jsonData;
// const next = ref("");
// const previous = ref("");
// const API_URL = import.meta.env.VITE_API_URL || "http://localhost:8000/api/";

// async function fetchPosts(url = API_URL) {
//   try {
//     const response = await axios.get(url);
//     items.value = response.data.results;
//     next.value = response.data.next;
//     previous.value = response.data.previous;
//   } catch (error) {
//     console.error("Failed to fetch posts:", error);
//     if (!response.data.results) {
//         items.value = jsonData
//       }
//     }
//   }
// function goToPage(url) {
//   if (url) fetchPosts(url);
// }

// onMounted(() => {
//   fetchPosts();
// });
</script>

<template>
  <div>
    <h2>Items</h2>
    <ul>
      <li v-for="item in items" :key="item.index">
        <a :href="item.URL">{{ item.title }}</a>
        <span>{{ item.date_of_publish }}</span>
      </li>
    </ul>
  </div>
</template>

<style scoped></style>
