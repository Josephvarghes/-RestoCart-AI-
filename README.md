# RestoCart AI

An intelligent e-commerce and restaurant management system built around a sophisticated **AI agent powered by Groq + LangChain RAG**.
Users can browse products, search, add to cart, place orders, and chat seamlessly with the AI assistant to manage restaurant operations.

> 🚫 **No authentication, payments, or user accounts** — focused entirely on demonstrating AI capabilities and agent workflows.
> ✅ **100% reproducible** with exact dependency versions.

---

## 🌟 Features

- 🛍️ **Product listing** with name, price, description (images via placeholder)
- 🔍 **Real-time search** (client-side + semantic backend fallback)
- 🛒 **Add to Cart** with live summary in navbar: `Cart: 2 items – ₹145.74`
- 📦 **Place Order**: sends product IDs to backend, saves to SQLite, clears cart
- 🤖 **AI Agent (Resto-Manager)**: A sophisticated assistant that manages the entire restaurant flow.
  - **Tool-Enabled**: Can check real-time inventory, monitor kitchen load, calculate bills (with tax), and process orders.
  - **Decision Logic**: Suggests alternatives when items are out of stock and warns about delays if the kitchen is busy.
  - **Powered by Groq + LangChain**: Uses **Llama-3.3-70b-versatile** for reasoning and decision-making.
  - **Memory Persistence**: Maintains chat history across sessions using SQLite.
  - Implements **Retrieval-Augmented Generation (RAG)** for accurate product information.

---

## 🛠️ Tech Stack

| Layer       | Technology |
|-------------|-----------|
| **Backend** | FastAPI, SQLAlchemy, SQLite (`restopulse.db`) |
| **AI**      | LangChain (Agents), Groq API (Llama-3.3-70b), ChromaDB, `all-MiniLM-L6-v2` |
| **Frontend**| React 18, Vite, Tailwind CSS |
| **State**   | React Context (Cart) |
| **APIs**    | REST (`/api/v1/products`, `/api/v1/orders`, `/api/v1/ai/chat`) |

---

## 🤖 Agent Automation

This project includes an **`.agents`** directory designed for AI assistants (like Antigravity) to handle project management, setup, and execution seamlessly.

- **/setup**: Automatically sets up the backend (uv sync) and frontend (npm install).
- **/run**: Launches both the FastAPI and Vite development servers.
- **/all**: One command to rule them all — setup and run everything.

> [!TIP]
> Use these workflows to maintain a consistent developer experience across environments.

---

## 🚀 Local Setup

### Prerequisites
- Python 3.9+
- [uv](https://github.com/astral-sh/uv) (Recommended for Python)
- Node.js 18+
- [Groq API Key](https://console.groq.com/keys)

---

### 🔧 Backend (FastAPI)

```bash
# 1. Clone & enter project
git clone https://github.com/Josephvarghes/-RestoCart-AI-.git
cd -RestoCart-AI-

# 2. Set up environment and install dependencies with uv
cd backend
uv sync

# 3. Configure environment
echo "GROQ_API_KEY=your_groq_api_key_here" > .env

# 4. (Optional) Verify AI Agent
uv run python verify_agent.py

# 5. Run server
uv run uvicorn main:app --reload --port 8000
```

---

### 🎨 Frontend (React + Vite)

```bash
# 1. Enter frontend directory
cd frontend

# 2. Install dependencies
npm install

# 3. Run development server
npm run dev
```
