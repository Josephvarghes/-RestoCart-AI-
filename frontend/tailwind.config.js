// export default {
// content: ["/index.html", "./src/**/*.{js,jsx}"],
// theme: { extend: {} },
// plugins: [],
// };

// tailwind.config.js — Perfect for Vite + React 2025
/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",   // ← ഇതാണ് correct path!
  ],
  theme: {
    extend: {},
  },
  plugins: [],
}
