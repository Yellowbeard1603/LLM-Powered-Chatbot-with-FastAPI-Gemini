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

```

---

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

---

## 💬 API Endpoints

### 🔑 POST `/login`

Authenticate user and receive a JWT token.

**Request:**

```json
{
  "username": "admin",
  "password": "password"
}
```

**Response:**

```json
{
  "access_token": "<JWT_TOKEN>"
}
```

To access and test the API endpoints, visit http://localhost:8000/docs. Copy the access_token, click the Authorize button at the top right of the page, and paste the token there to authenticate and interact with the secured endpoints.

### 💬 POST `/chat`

Send a message to the chatbot. Requires a valid JWT token in headers.

**Request:**

```json
{
  "message": "what is the captial city of france ?"
}
```

**Response:**

```json
{
  "response": "Paris"
}
```
---

## 🐳 Run with Docker

Ensure that Docker Desktop is running in the background before proceeding.

### 1. Build the Docker image

```bash
docker build -t chatbot .
```

### 2. Create a `.env` file

Make sure you have a `.env` file in the root of your project with your Gemini API key:

```
GEMINI_API_KEY=your_google_genai_key
```

You can also use the provided `.env.example` as a template.

### 3. Run the Docker container

If this is your first time running the container, use the following command:

```bash
docker run --env-file .env -p 8000:8000 chatbot
```

If you've already built and run the container before, you can simply start it again directly from Docker Desktop without using the command line.


### 4. Open the app in your browser

```
http://localhost:8000
```

Now you can interact with the chatbot just like you would when running locally.

### 5. Access the API docs (Swagger UI)

```
http://localhost:8000/docs
```

Copy the `access_token`, click the **Authorize** button at the top right of the page, and paste the token there to authenticate and access the protected endpoints.


