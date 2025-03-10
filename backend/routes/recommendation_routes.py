from fastapi import APIRouter
from backend.services.recommendation_service import get_llama_recommendation
from pydantic import BaseModel

router = APIRouter()

class RecommendationRequest(BaseModel):
    user_interest: str

@router.get("/")
def read_root():
    return {"message": "Welcome to the BakedBot Recommendation System!"}

@router.post("/recommend/")
def get_recommendation(req: RecommendationRequest):
    user_interest = req.user_interest
    recommendation = get_llama_recommendation(user_interest)
    return {"recommendation": recommendation}
