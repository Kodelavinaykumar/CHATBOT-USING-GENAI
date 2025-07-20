from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from transformers import pipeline

app = FastAPI()

# Enable CORS if frontend runs separately
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Initialize the text-generation pipeline
generator = pipeline("text-generation", model="gpt2")

# Request body structure
class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(chat_request: ChatRequest):
    user_message = chat_request.message
    response = generator(user_message, max_length=50, num_return_sequences=1, do_sample=True, temperature=0.7)
    bot_reply = response[0]["generated_text"]
    return {"reply": bot_reply.strip()}
