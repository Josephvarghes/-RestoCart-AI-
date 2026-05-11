import { useCart } from "../context/CartContext.jsx";
import { placeOrder } from "../api/api.js";
import { Trash2, Plus, Minus, ShoppingBag } from "lucide-react";
import toast from "react-hot-toast";

export default function Cart() {
  const { cart, updateQuantity, removeFromCart, clearCart } = useCart();

  const handleOrder = async () => {
    // Generate array of IDs based on quantity for the backend
    const ids = cart.flatMap(item => Array(item.quantity || 1).fill(item.id));
    
    const loadingToast = toast.loading("Processing your order...");
    
    try {
      await placeOrder({ product_ids: ids });
      clearCart();
      toast.success("Order placed successfully!", {
        id: loadingToast,
        duration: 4000,
      });
    } catch (error) {
      toast.error("Failed to place order. Please try again.", {
        id: loadingToast,
      });
    }
  };

  const subtotal = cart.reduce((sum, item) => sum + item.price * (item.quantity || 1), 0);
  const tax = subtotal * 0.05; // 5% tax example
  const total = subtotal + tax;

  if (cart.length === 0) {
    return (
      <div className="p-6 max-w-xl mx-auto text-center py-20">
        <ShoppingBag size={64} className="mx-auto text-slate-300 mb-4" />
        <h2 className="text-2xl font-bold text-slate-800 mb-2">Your cart is empty</h2>
        <p className="text-slate-500 mb-6">Looks like you haven't added anything yet.</p>
        <button 
          onClick={() => window.history.back()}
          className="bg-blue-600 hover:bg-blue-700 text-white px-6 py-2 rounded-xl transition-colors"
        >
          Browse Menu
        </button>
      </div>
    );
  }

  return (
    <div className="p-6 max-w-4xl mx-auto flex flex-col md:flex-row gap-8">
      {/* Cart Items List */}
      <div className="flex-1">
        <h1 className="text-2xl font-bold text-slate-900 mb-6 border-b pb-4">Your Order</h1>
        <div className="space-y-4">
          {cart.map((item) => (
            <div key={item.id} className="flex items-center gap-4 bg-white p-4 rounded-2xl border border-gray-100 shadow-sm">
              <img 
                src={item.image || `https://ui-avatars.com/api/?name=${encodeURIComponent(item.name)}&background=random&size=100`} 
                alt={item.name} 
                className="w-16 h-16 object-cover rounded-lg"
              />
              <div className="flex-1">
                <h3 className="font-semibold text-slate-800">{item.name}</h3>
                <p className="text-blue-600 font-medium">₹{item.price}</p>
              </div>
              
              {/* Quantity Controls */}
              <div className="flex items-center gap-3 bg-slate-50 p-1 rounded-lg">
                <button 
                  onClick={() => updateQuantity(item.id, -1)}
                  className="p-1 hover:bg-white rounded shadow-sm text-slate-600"
                >
                  <Minus size={16} />
                </button>
                <span className="w-4 text-center font-medium text-sm">{item.quantity || 1}</span>
                <button 
                  onClick={() => updateQuantity(item.id, 1)}
                  className="p-1 hover:bg-white rounded shadow-sm text-slate-600"
                >
                  <Plus size={16} />
                </button>
              </div>
              
              {/* Remove Item */}
              <button 
                onClick={() => removeFromCart(item.id)}
                className="p-2 text-red-500 hover:bg-red-50 rounded-lg transition-colors ml-2"
                title="Remove item"
              >
                <Trash2 size={20} />
              </button>
            </div>
          ))}
        </div>
      </div>

      {/* Order Summary */}
      <div className="w-full md:w-80 h-fit bg-white p-6 rounded-2xl border border-gray-100 shadow-sm sticky top-24">
        <h2 className="text-lg font-bold text-slate-900 mb-4 border-b pb-4">Order Summary</h2>
        
        <div className="space-y-3 mb-6 text-sm">
          <div className="flex justify-between text-slate-600">
            <span>Subtotal</span>
            <span>₹{subtotal.toFixed(2)}</span>
          </div>
          <div className="flex justify-between text-slate-600">
            <span>Taxes (5%)</span>
            <span>₹{tax.toFixed(2)}</span>
          </div>
          <div className="flex justify-between font-bold text-lg text-slate-900 pt-3 border-t">
            <span>Total</span>
            <span>₹{total.toFixed(2)}</span>
          </div>
        </div>
        
        <button
          className="w-full bg-blue-600 hover:bg-blue-700 text-white font-medium py-3 rounded-xl transition-all active:scale-[0.98] shadow-sm hover:shadow-md"
          onClick={handleOrder}
        >
          Place Order (₹{total.toFixed(2)})
        </button>
      </div>
    </div>
  );
}
