<script setup>
import { ref, onMounted } from "vue";
import axios from "axios";

const items = ref([]);
const next = ref("");
const previous = ref("");
const API_URL = "http://localhost:8000/api/";
const ROOT = "http://localhost:8000";

async function fetchPosts(url = API_URL) {
  try {
    const response = await axios.get(url);
    items.value = response.data.results;
    next.value = response.data.next;
    previous.value = response.data.previous;
  } catch (error) {
    console.error("Failed to fetch posts:", error);
  }
}
function goToPage(url) {
  if (url) fetchPosts(url);
}

onMounted(() => {
  fetchPosts();
});
</script>

<template>
  <div>
    <h2>Items</h2>
    <ul>
      <li v-for="item in items" :key="item.id">
        <a :href="item.URL">{{ item.title }}</a>
        <span>{{ item.date_of_publish }}</span>
      </li>
    </ul>
  </div>
  <div class="pagination-controls">
    <button @click="goToPage(previous)" :disabled="!previous">Previous</button>
    <button @click="goToPage(next)" :disabled="!next">Next</button>
  </div>
</template>

<style scoped></style>
