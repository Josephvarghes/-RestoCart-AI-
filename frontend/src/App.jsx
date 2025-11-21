import { BrowserRouter, Routes, Route } from "react-router-dom";
import Home from "./pages/Home.jsx";
import Cart from "./pages/Cart.jsx";
import Navbar from "./components/Navbar.jsx";


export default function App() {
return (
<BrowserRouter>
<Navbar />
<Routes>
<Route path="/" element={<Home />} />
<Route path="/cart" element={<Cart />} />
</Routes>
</BrowserRouter>
);
} 
// export default function App() {
//   return (
//     <div className="min-h-screen bg-red-500 flex items-center justify-center">
//       <h1 className="text-6xl font-bold text-white">
//         TAILWIND WORKING!
//       </h1>
//     </div>
//   );
// }