
import { createContext, useContext, useState } from "react";


const CartContext = createContext();


export function CartProvider({ children }) {
const [cart, setCart] = useState([]);


const addToCart = (product) => setCart([...cart, product]);
const clearCart = () => setCart([]); 


return (
<CartContext.Provider value={{ cart, addToCart, clearCart }}>
{children}
</CartContext.Provider>
); 
}; 

export const useCart = () => {
  const context = useContext(CartContext);
  if (!context) {
    throw new Error("useCart must be used within CartProvider");
  }
  return context;
};