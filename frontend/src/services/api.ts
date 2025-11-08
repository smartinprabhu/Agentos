import axios from "axios";

const apiClient = axios.create({
  baseURL: "http://localhost:8000",
});

export const register = (data: any) => {
  return apiClient.post("/auth/register", data);
};

export const login = (data: any) => {
  return apiClient.post("/auth/login", data);
};
