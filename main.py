
import os
from fastapi import FastAPI, Depends, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from auth import create_token, verify_token
import google.generativeai as genai
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse

load_dotenv()
genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

app = FastAPI()  # ✅ This must come first!
app.mount("/static", StaticFiles(directory="static", html=True), name="static")

chat_history = {}


class LoginRequest(BaseModel):
    username: str
    password: str

class ChatRequest(BaseModel):
    message: str

@app.post("/login")
def login(request: LoginRequest):
    if request.username == "admin" and request.password == "password":
        token = create_token({"sub": request.username})
        return {"access_token": token}
    raise HTTPException(status_code=401, detail="Invalid credentials")



@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("static/index.html", "r", encoding="utf-8") as f:  # ✅ fix here
        return f.read()


@app.post("/chat")
def chat(req: ChatRequest, user=Depends(verify_token)):
    username = user['sub']
    model = genai.GenerativeModel("gemini-2.0-flash")

    history = chat_history.get(username, [])
    prompt = "\n".join([f"User: {msg['user']}\nBot: {msg['bot']}" for msg in history])
    prompt += f"\nUser: {req.message}\nBot:"

    print("Prompt sent to Gemini:\n", prompt)  # For debugging

    try:
        response = model.generate_content(prompt)
        answer = response.text.strip() if response.text else "⚠️ Empty response"
    except Exception as e:
        print("Gemini error:", e)
        raise HTTPException(status_code=500, detail=f"Gemini Error: {str(e)}")

    history.append({"user": req.message, "bot": answer})
    chat_history[username] = history

    return {"response": answer}


@app.post("/chat/stream")
def chat_stream(req: ChatRequest, user=Depends(verify_token)):
    username = user['sub']
    model = genai.GenerativeModel("gemini-2.0-flash")

    history = chat_history.get(username, [])
    prompt = "\n".join([f"User: {msg['user']}\nBot: {msg['bot']}" for msg in history])
    prompt += f"\nUser: {req.message}\nBot:"

    def stream_response():
        bot_response = ""
        for chunk in model.generate_content_stream(prompt):
            text = chunk.text
            bot_response += text
            yield text
        history.append({"user": req.message, "bot": bot_response.strip()})
        chat_history[username] = history

    return StreamingResponse(stream_response(), media_type="text/plain")
