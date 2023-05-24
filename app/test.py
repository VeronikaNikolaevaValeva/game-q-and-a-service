from fastapi.testclient import TestClient
from app.models import QuizOptions, QuizQandASearchResults
from app.main import app

client = TestClient(app)

def test_get_questions():
    parameters = QuizOptions(category="History", difficulty="easy", amount=1)
    response = client.post("/GetQuestions", parameters.json())
    assert response.status_code == 200
    # assert response.json() == {"id": 1,  "name": "Item One"}

def test_get_all_categories():
    response = client.get("/GetAllCategories")
    assert response.status_code == 200
    # assert response.json() == {"id": 1, "name": "Item One"}