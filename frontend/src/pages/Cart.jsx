import { useCart } from "../context/CartContext.jsx";
import { placeOrder } from "../api/api.js";


export default function Cart() {
const { cart, clearCart } = useCart();


const handleOrder = async () => {
const ids = cart.map((c) => c.id);
await placeOrder({ product_ids: ids });
clearCart();
alert("Order placed!");
};


return (
<div className="p-6 max-w-xl mx-auto">
<h1 className="text-2xl font-bold mb-4">Your Cart</h1>
{cart.map((item) => (
<div key={item.id} className="border p-2 mb-2 rounded">
{item.name} - ₹{item.price}
</div>
))}
<button
className="bg-green-600 text-white px-4 py-2 rounded mt-4"
onClick={handleOrder}
>
Place Order
</button>
</div>
);
}