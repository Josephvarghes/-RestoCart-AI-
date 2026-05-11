import { BrowserRouter, Routes, Route } from "react-router-dom";
import { Toaster } from "react-hot-toast";
import Home from "./pages/Home.jsx";
import Cart from "./pages/Cart.jsx";
import Navbar from "./components/Navbar.jsx";
import ChatWidget from "./pages/ChatWidget";

export default function App() {
  return (
    <BrowserRouter>
      <Toaster position="bottom-center" />
      <Navbar />
      <div className="pt-16 pb-24"> {/* Add padding for fixed navbar and chat widget */}
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/cart" element={<Cart />} />
        </Routes>
      </div>
      <ChatWidget />
    </BrowserRouter>
  );
}
