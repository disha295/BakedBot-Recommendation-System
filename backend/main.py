from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from backend.routes.recommendation_routes import router as recommendation_router

app = FastAPI()

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

# Include the recommendation routes
app.include_router(recommendation_router, prefix="/api")
