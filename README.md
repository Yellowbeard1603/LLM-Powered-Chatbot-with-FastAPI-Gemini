# 🤖 LLM-Powered Chatbot with FastAPI + Gemini

This project is a secure, JWT-authenticated chatbot powered by Google's Gemini LLM. It allows users to log in, send questions, and receive AI-generated responses through a clean web interface. The backend is built with FastAPI, and the entire app is containerized with Docker for easy deployment.

---

## 🚀 Features

- 🔐 Secure login with JWT authentication  
- 🤖 Chat with a Gemini-powered LLM  
- 🧠 Per-user chat history retained in memory  
- 🎨 Responsive frontend built in HTML + CSS  
- ⚙️ Served fully through FastAPI  
- 🔑 `.env` support for API keys  
- 🐳 Docker-ready for instant deployment  

---

## 🧰 Technologies Used

- FastAPI  
- Google Generative AI (Gemini Pro / Flash)  
- JWT via `python-jose`  
- HTML + CSS (frontend)  
- Docker (containerization)  
- Python 3.10+  

---

## 📁 Project Structure

```
.
├── main.py              # FastAPI app with endpoints
├── auth.py              # JWT token creation and verification
├── static/
│   └── index.html       # Frontend UI served at root
├── test_main.py         # Basic unit tests for login
├── requirements.txt     # Python dependencies
├── Dockerfile           # Docker configuration
├── .env                 # Contains your Gemini API key (excluded from Git)
├── .env.example         # Template for required environment variables
└── README.md            # Project documentation


---

```

## ⚙️ How to Run Locally (Without Docker)

### 1. Clone the repository

```bash
git clone https://github.com/your-username/chatbot.git
cd chatbot
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a .env file

```bash
GEMINI_API_KEY=your_google_genai_key
```

### 5. Run the app

```bash
uvicorn main:app --reload
```

### 6. Now open the browser and visit:

```bash
http://localhost:8000
```

### 7. Login Credentials

| Username | Password   |
| -------- | ---------- |
| `admin`  | `password` |







