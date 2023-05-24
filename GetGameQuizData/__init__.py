from fastapi.middleware.cors import CORSMiddleware
import requests
from app.models import QuizOptions, QuizQandASearchResults
import azure.functions as func
from app import app  # Main API application


@app.post("/GetQuestions", response_model=QuizQandASearchResults)
async def generate_questions(params: QuizOptions):
    questions = await get_questions(params)
    return {"results": questions} 


async def get_questions(params: QuizOptions):
    url = f"https://the-trivia-api.com/api/questions?categories={params.category}&limit={params.amount}&difficulty={params.difficulty}"
    response = requests.get(url)
    questions = response.json()
    return questions 


@app.get("/GetAllCategories")
async def generate_categories():
    categories = await get_categories()
    return categories


async def get_categories():
    url = "https://the-trivia-api.com/api/categories"
    response = requests.get(url)
    categories = response.json()
    return categories 

async def main(req: func.HttpRequest, context: func.Context) -> func.HttpResponse:
    return await func.AsgiMiddleware(app).handle_async(req, context)
