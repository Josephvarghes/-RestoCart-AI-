# RestoCart AI

A simplified e-commerce demo built for the **RestoPulse Junior Fullstack Engineer** assignment.
Users can browse products, search, add to cart, place dummy orders, and ask an AI assistant questions about products—powered by **Groq + LangChain**.

> ⚠️ **No authentication, payments, or user accounts** — as per assignment constraints.

---

## ✨ Features

- 🛍️ Product listing with name, price, description, and image (placeholder)
- 🔍 Real-time search by product name
- 🛒 Frontend cart management
- 📦 Dummy order placement (saved to SQLite)
- 🤖 AI chatbot using **Groq LLM** + **RAG over product data**

---

## 🛠️ Tech Stack

- **Backend**: FastAPI (Python)
- **Frontend**: React + Tailwind CSS
- **Database**: SQLite
- **AI**: LangChain + Groq API (Free Tier)
- **Deployment**: Local dev only (no auth or production deploy required)

---

## 🚀 Local Setup

### Prerequisites
- Python 3.9+
- Node.js 18+
- [Groq API Key](https://console.groq.com/keys)

### Backend

```bash
# 1. Clone & enter project
git clone https://github.com/Josephvarghes/-RestoCart-AI-.git
cd backend

# 2. Set up Python environment
python -m venv venv
source venv/bin/activate  # Linux/macOS
# venv\Scripts\activate   # Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Add your Groq key
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 5. Run server
uvicorn main:app --reload --port 8000
