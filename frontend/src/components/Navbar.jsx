
import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";

export default function Navbar() {
  const { cart } = useCart();

  const totalItems = cart.length;
  const totalPrice = cart.reduce((sum, item) => sum + item.price, 0);

  return (
    <nav className="bg-gray-900 text-white p-4 flex justify-between items-center">
      <Link to="/" className="text-xl font-bold">RestoPulse Shop</Link>
      
      <div className="flex items-center gap-2">
        <span className="text-sm">
          Cart: {totalItems} item{totalItems !== 1 ? "s" : ""} – ₹{totalPrice.toFixed(2)}
        </span>
        <Link
          to="/cart"
          className="bg-blue-600 hover:bg-blue-700 px-3 py-1 rounded text-sm"
        >
          View Cart
        </Link>
      </div>
    </nav>
  );
}