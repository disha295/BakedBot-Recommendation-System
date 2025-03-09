from fastapi import FastAPI
from pydantic import BaseModel
import requests

# Initialize FastAPI app
app = FastAPI()

# Define a model for the recommendation request
class RecommendationRequest(BaseModel):
    user_interest: str

# Ollama (LLaMA) API endpoint
OLLAMA_API_URL = "http://localhost:11434/v1/chat/completions"  # Adjust if needed
headers = {
    "Content-Type": "application/json",
}

# Function to call the Ollama API for LLaMA3 recommendations
def get_llama_recommendation(user_interest: str):
    # Prepare data to send to Ollama API
    data = {
        "model": "llama",  # Use LLaMA model
        "messages": [{"role": "user", "content": user_interest}],
        "temperature": 0.7,
        "max_tokens": 150,
    }

    # Send the request to Ollama API
    response = requests.post(OLLAMA_API_URL, headers=headers, json=data)

    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        return f"Error: {response.status_code}, {response.text}"

# Default route to test if the server is working
@app.get("/")
def read_root():
    return {"message": "Welcome to the BakedBot Recommendation System!"}

# POST route to get recommendations based on user interest
@app.post("/recommend/")
def get_recommendation(req: RecommendationRequest):
    user_interest = req.user_interest
    recommendation = get_llama_recommendation(user_interest)
    return {"recommendation": recommendation}
