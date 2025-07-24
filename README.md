# ai_agent

# to run (Backend FastAPI)
cd backend
pip install -r requirements.txt
export OPENAI_API_KEY
uvicorn main:app --reload --port 8000

# (Frontend React)
cd frontend
npm install
npm start

Frontend runs on `http://localhost:3000` and sends chat requests to backend at `http://localhost:8000/chat`

# Deploying at
Use **Render** or **Azure App Service** for FastAPI


Chat History is saved to `backend/chat_history.json`