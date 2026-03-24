---
description: Run the backend and frontend servers
---

# Run Project Workflow

This workflow runs both the FastAPI backend and the Vite frontend.

### 1. Run Backend
1. Change directory to backend: `cd backend`
2. Activate virtual environment (Windows): `.\venv\Scripts\Activate.ps1`
3. Start the FastAPI server: `uvicorn main:app --reload --port 8000`

### 2. Run Frontend
1. Change directory to frontend: `cd frontend`
2. Start the Vite development server: `npm run dev`

> [!NOTE]
> Ensure you have configured the `GROQ_API_KEY` in `backend/.env`.
