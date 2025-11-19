export default function SearchBar({ value, onChange }) {
return (
<input
type="text"
placeholder="Search products..."
className="border p-2 rounded w-full mb-4"
value={value}
onChange={(e) => onChange(e.target.value)}
/>
);
}