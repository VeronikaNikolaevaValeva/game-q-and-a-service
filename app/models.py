from pydantic import BaseModel
from typing import Optional, Sequence

class QuizOptions(BaseModel):
    category: str
    difficulty: str
    amount: str

class QuizQandA(BaseModel):
    category: str
    id: str
    correctAnswer: str
    incorrectAnswers: Optional[Sequence[str]] = None
    question: str
    tags: Optional[Sequence[str]] = None
    type: str
    difficulty: Optional[str] = None
    regions: Optional[Sequence[str]] = None
    isNiche: bool

class QuizQandASearchResults(BaseModel):
    results: Sequence[QuizQandA]

