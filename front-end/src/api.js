import axios from "axios";

const api = axios.create({
  baseURL: "http://localhost:8000/api/",
  withCredentials: false, // if using sessions/cookies
});

export default api;
