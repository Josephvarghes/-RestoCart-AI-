export default function ProductCard({ product, onAdd }) {
return (
<div className="border rounded p-4 shadow hover:shadow-lg transition">
<h3 className="text-lg font-bold">{product.name}</h3>
<p className="text-gray-600 py-2">{product.description}</p>
<p className="font-semibold mb-2">₹{product.price}</p>
<button
className="bg-blue-600 text-white px-4 py-2 rounded"
onClick={() => onAdd(product)}
>
Add to Cart
</button>
</div>
);
}
