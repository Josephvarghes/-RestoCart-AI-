import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext.jsx";


export default function Navbar() {
const { cart } = useCart();
return (
<nav className="bg-gray-900 text-white p-4 flex justify-between">
<Link to="/" className="text-xl font-bold">RestoPulse Shop</Link>
<Link to="/cart">Cart ({cart.length})</Link>
</nav>
);
}
