<script setup>
import { ref, onMounted, computed } from "vue";
import axios from "axios";
import jsonData from "../../wired_data.json";

const items = ref([]);

items.value = jsonData;

const uniqueSortedItems = computed(() => {
  const uniqueItems = new Map();

  items.value.forEach((item) => {
    if (!uniqueItems.has(item.title)) {
      uniqueItems.set(item.title, item);
    }
  });

  return Array.from(uniqueItems.values()).sort((a, b) => {
    const dateA = new Date(a.date_of_publish);
    const dateB = new Date(b.date_of_publish);
    return dateB - dateA;
  });
});
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
      <li v-for="item in uniqueSortedItems" :key="item.title">
        <a :href="item.URL">{{ item.title }}</a>
        <span>{{ item.date_of_publish }}</span>
      </li>
    </ul>
  </div>
</template>

<style scoped></style>
