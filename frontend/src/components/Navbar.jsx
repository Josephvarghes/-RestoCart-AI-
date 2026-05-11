import { Link } from "react-router-dom";
import { useCart } from "../context/CartContext";
import { ShoppingCart } from "lucide-react";

export default function Navbar() {
  const { cart } = useCart();

  const totalItems = cart.reduce((sum, item) => sum + (item.quantity || 1), 0);
  const totalPrice = cart.reduce((sum, item) => sum + item.price * (item.quantity || 1), 0);

  return (
    <nav className="fixed top-0 w-full z-50 bg-white/80 backdrop-blur-md border-b border-gray-200 text-slate-800 p-4 transition-all shadow-sm">
      <div className="max-w-6xl mx-auto flex justify-between items-center">
        <Link to="/" className="text-xl font-bold tracking-tight text-blue-600">
          RestoPulse
        </Link>

        <div className="flex items-center gap-4">
          <span className="text-sm font-medium hidden sm:block">
            ₹{totalPrice.toFixed(2)}
          </span>
          <Link
            to="/cart"
            className="relative flex items-center justify-center bg-blue-600 hover:bg-blue-700 text-white p-2 rounded-full transition-transform hover:scale-105 active:scale-95"
          >
            <ShoppingCart size={20} />
            {totalItems > 0 && (
              <span className="absolute -top-1 -right-1 bg-red-500 text-white text-[10px] font-bold w-4 h-4 flex items-center justify-center rounded-full">
                {totalItems}
              </span>
            )}
          </Link>
        </div>
      </div>
    </nav>
  );
}
