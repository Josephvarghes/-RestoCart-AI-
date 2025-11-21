import { useEffect, useState } from "react";
import { getProducts } from "../api/api";
import ProductCard from "../components/ProductCard.jsx";
import SearchBar from "../components/SearchBar.jsx";
import { useCart } from "../context/CartContext.jsx";


export default function Home() {
const [products, setProducts] = useState([]);
const [search, setSearch] = useState("");
const { addToCart } = useCart();


useEffect(() => {
(async () => {
const data = await getProducts();
setProducts(data);
})();
}, []);


const filtered = products.filter((p) =>
p.name.toLowerCase().includes(search.toLowerCase())
);


return (
<div className="p-6 max-w-6xl mx-auto">
<SearchBar value={search} onChange={setSearch} />
<div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
{filtered.map((product) => (
<ProductCard
key={product.id}
product={product}
onAdd={addToCart}
/>
))}
</div>
</div>
);
}
