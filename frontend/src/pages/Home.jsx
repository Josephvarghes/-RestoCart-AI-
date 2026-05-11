import { useEffect, useState } from "react";
import { getProducts } from "../api/api";
import ProductCard from "../components/ProductCard.jsx";
import SearchBar from "../components/SearchBar.jsx";
import { useCart } from "../context/CartContext.jsx";
import { SearchX } from "lucide-react";

export default function Home() {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState("");
  const [isLoading, setIsLoading] = useState(true);
  const { addToCart } = useCart();

  useEffect(() => {
    (async () => {
      try {
        const data = await getProducts();
        setProducts(data);
      } catch (error) {
        console.error("Failed to fetch products:", error);
      } finally {
        setIsLoading(false);
      }
    })();
  }, []);

  const filtered = products.filter((p) =>
    p.name.toLowerCase().includes(search.toLowerCase())
  );

  return (
    <div className="p-6 max-w-6xl mx-auto min-h-screen">
      <div className="mb-8 text-center">
        <h1 className="text-3xl font-bold text-slate-900 mb-2">Our Menu</h1>
        <p className="text-slate-500">Discover our delicious offerings</p>
      </div>
      
      <SearchBar value={search} onChange={setSearch} />
      
      {isLoading ? (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-6">
          {[1, 2, 3, 4, 5, 6].map((i) => (
            <div key={i} className="bg-white border border-gray-100 rounded-2xl p-4 shadow-sm animate-pulse">
              <div className="bg-slate-200 h-48 rounded-xl mb-4"></div>
              <div className="bg-slate-200 h-6 w-3/4 rounded mb-2"></div>
              <div className="bg-slate-200 h-4 w-full rounded mb-1"></div>
              <div className="bg-slate-200 h-4 w-2/3 rounded mb-4"></div>
              <div className="bg-slate-200 h-10 w-full rounded-xl mt-4"></div>
            </div>
          ))}
        </div>
      ) : filtered.length === 0 ? (
        <div className="flex flex-col items-center justify-center py-20 text-slate-500">
          <SearchX size={64} className="text-slate-300 mb-4" />
          <h2 className="text-xl font-semibold text-slate-700">No products found</h2>
          <p>We couldn't find any dishes matching "{search}"</p>
          <button 
            onClick={() => setSearch("")}
            className="mt-4 text-blue-600 hover:text-blue-700 font-medium"
          >
            Clear search
          </button>
        </div>
      ) : (
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-6">
          {filtered.map((product) => (
            <ProductCard
              key={product.id}
              product={product}
              onAdd={addToCart}
            />
          ))}
        </div>
      )}
    </div>
  );
}
