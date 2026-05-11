import axios from "axios";


const API_BASE = "http://localhost:8000/api/v1";


export const getProducts = async () => {
const res = await axios.get(`${API_BASE}/products/`);
return res.data;
};


export const placeOrder = async (data) => {
  const res = await axios.post(`${API_BASE}/orders/`, data);
  return res.data;
};
