import toast from 'react-hot-toast';
import { Plus } from 'lucide-react';

export default function ProductCard({ product, onAdd }) {
  const handleAdd = () => {
    onAdd(product);
    toast.success(`Added ${product.name} to cart!`, {
      style: {
        borderRadius: '10px',
        background: '#333',
        color: '#fff',
      },
      iconTheme: {
        primary: '#4ade80',
        secondary: '#fff',
      },
    });
  };

  // Generate a placeholder image based on the product name if one doesn't exist
  const imageUrl = product.image || `https://ui-avatars.com/api/?name=${encodeURIComponent(product.name)}&background=random&size=400`;

  return (
    <div className="group flex flex-col bg-white border border-gray-100 rounded-2xl overflow-hidden shadow-sm hover:shadow-xl transition-all duration-300">
      <div className="relative h-48 overflow-hidden bg-gray-100">
        <img 
          src={imageUrl} 
          alt={product.name} 
          className="w-full h-full object-cover transform group-hover:scale-105 transition-transform duration-500"
        />
      </div>
      
      <div className="p-5 flex flex-col flex-grow">
        <div className="flex justify-between items-start mb-2">
          <h3 className="text-lg font-bold text-slate-800 line-clamp-1">{product.name}</h3>
          <span className="font-semibold text-blue-600 bg-blue-50 px-2 py-1 rounded-md text-sm">
            ₹{product.price}
          </span>
        </div>
        
        <p className="text-gray-500 text-sm mb-4 line-clamp-2 flex-grow">
          {product.description}
        </p>
        
        <button
          className="mt-auto flex items-center justify-center gap-2 w-full bg-slate-900 hover:bg-blue-600 text-white font-medium py-2.5 rounded-xl transition-colors active:scale-[0.98]"
          onClick={handleAdd}
        >
          <Plus size={18} />
          Add to Cart
        </button>
      </div>
    </div>
  );
}
