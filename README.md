🏥 Multi-RAG Medical Hospital Assistant

🚀 A production-grade AI system that answers medical & hospital-related queries using Multi-RAG (Retrieval-Augmented Generation) architecture.

✨ Features

🔀 Multi-RAG Routing

DB-based retrieval

Vector search (FAISS)

Real-time web search (SerpAPI)

🧠 Semantic Search

Powered by Sentence Transformers

⚡ Fast Retrieval

FAISS vector similarity search

🌐 Live Data Integration

Real-time hospital info via SerpAPI

🤖 AI-Powered Answers

OpenAI LLM generates accurate responses

🎨 Modern UI

Built with Streamlit (clean hospital dashboard)

⚙️ Backend API

FastAPI for high-performance serving

🏗️ Architecture

User Query
   ↓
Query Router  →  (DB / FAISS / Web)
   ↓
Context Retrieval
   ↓
LLM (OpenAI)
   ↓
Final Answer

📁 Project Structure

Multi_RAG/
│
├── app/
│   ├── main.py        # FastAPI backend
│   ├── ui.py          # Streamlit frontend
│
├── rag/
│   ├── router.py
│   ├── db_retriever.py
│   ├── vector_store.py
│   ├── serpapi_retriever.py
│   ├── llm.py
│
├── data/
│   └── hospitals.csv
│
├── .env
├── requirements.txt
└── README.md


⚙️ Tech Stack

🐍 Python

⚡ FastAPI

🎨 Streamlit

🔎 FAISS

🧠 Sentence Transformers

🤖 OpenAI API

🌐 SerpAPI


🔐 Environment Variables

Create a .env file:

OPENAI_API_KEY=your_openai_key
SERPAPI_KEY=your_serpapi_key


📦 Installation
git clone https://github.com/your-username/multi-rag-medical-assistant.git
cd multi-rag-medical-assistant

python -m venv venv
venv\Scripts\activate   # Windows

pip install -r requirements.txt

▶️ Run the Application

1️⃣ Start FastAPI Backend
uvicorn app.main:app --reload

👉 Runs at:
http://127.0.0.1:8000/docs


2️⃣ Start Streamlit UI
streamlit run app/ui.py


🔍 Sample Queries

“Best hospital near Bangalore”

“ICU rules in hospitals”

“Cardiology hospital in Chennai”

“Emergency admission policy”

🧠 How It Works
Query Type	Route
Hospital info	DB
General medical knowledge	FAISS
Real-time search	Web (SerpAPI)

📸 UI Preview

Clean, modern hospital assistant dashboard with:

Query input

Route detection

AI-generated answer



🛠️ Troubleshooting
❌ Backend not connecting
uvicorn app.main:app --reload
❌ SerpAPI error

Check:

SERPAPI_KEY
❌ OpenAI error

Check:

OPENAI_API_KEY


💡 Author

Kumar K


🔥 Built with passion for AI & real-world impact
