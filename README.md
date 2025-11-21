# RestoCart AI – RestoPulse Assignment

A simplified e-commerce demo built for the **RestoPulse Junior Fullstack Engineer** selection process.  
Users can browse products, search, add to cart, place dummy orders, and chat with an **AI assistant powered by Groq + LangChain RAG**.

> 🚫 **No authentication, payments, or user accounts** — as per assignment constraints.  
> ✅ **100% reproducible** with exact dependency versions.

---

## 🌟 Features

- 🛍️ **Product listing** with name, price, description (images via placeholder)
- 🔍 **Real-time search** (client-side + semantic backend fallback)
- 🛒 **Add to Cart** with live summary in navbar: `Cart: 2 items – ₹145.74`
- 📦 **Place Order**: sends product IDs to backend, saves to SQLite, clears cart
- 🤖 **AI Chatbot**: answers questions using **real product data only** (no hallucination)
  - Powered by **Groq LPU** (ultra-fast LLM inference)
  - Uses **ChromaDB + sentence-transformers** for semantic retrieval
  - Implements **Retrieval-Augmented Generation (RAG)**

---

## 🛠️ Tech Stack

| Layer       | Technology |
|-------------|-----------|
| **Backend** | FastAPI, SQLAlchemy, SQLite (`restopulse.db`) |
| **AI**      | LangChain, Groq API, ChromaDB, `all-MiniLM-L6-v2` embeddings |
| **Frontend**| React 18, Vite, Tailwind CSS |
| **State**   | React Context (Cart) |
| **APIs**    | REST (`/api/v1/products`, `/api/v1/orders`, `/api/v1/ai/chat`) |

---

## 🚀 Local Setup

### Prerequisites
- Python 3.9+
- Node.js 18+
- [Groq API Key](https://console.groq.com/keys)

---

### 🔧 Backend (FastAPI)

```bash
# 1. Clone & enter project
git clone https://github.com/Josephvarghes/-RestoCart-AI-.git
cd restocart-ai

# 2. Set up Python environment
python -m venv resto
source resto/bin/activate  # Linux/macOS
# resto\Scripts\Activate.ps1  # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Configure environment
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 5. Run server
uvicorn main:app --reload --port 8000