import axios from "axios";
const API_BASE = import.meta.env.VITE_API_BASE || "http://localhost:8000";

export const api = axios.create({
  baseURL: API_BASE,
});

export async function getTransactions(){
  const res = await api.get("/transactions/");
  return res.data;
}

export async function ingestTransaction(tx){
  return (await api.post("/transactions/", tx)).data;
}
