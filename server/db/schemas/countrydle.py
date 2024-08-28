from datetime import datetime
from typing import List

from pydantic import BaseModel

from db.schemas.user import UserDisplay
from db.schemas.country import CountryDisplay


class QuestionBase(BaseModel):
    question: str


class QuestionCreate(QuestionBase):
    answer: str
    user_id: int
    day_id: int
    explanation: str
    context: str

    class Config:
        from_attributes = True


class QuestionDisplay(BaseModel):
    id: int
    question: str
    answer: str
    user_id: int
    day_id: int
    asked_at: datetime

    class Config:
        from_attributes = True


class FullQuestionDisplay(QuestionDisplay):
    explanation: str

    class Config:
        from_attributes = True


# Guess Schema
class GuessBase(BaseModel):
    guess: str


class GuessCreate(GuessBase):
    day_id: int
    user_id: int
    response: str


class GuessDisplay(GuessBase):
    id: int
    response: str
    guessed_at: datetime

    class Config:
        from_attributes = True


class UserHistory(BaseModel):
    user: UserDisplay
    questions: List[QuestionDisplay]
    guesses: List[GuessDisplay]

    class Config:
        from_attributes = True


class FullUserHistory(BaseModel):
    user: UserDisplay
    questions: List[FullQuestionDisplay]
    guesses: List[GuessDisplay]

    class Config:
        from_attributes = True


class CountrydleState(BaseModel):
    user: UserDisplay
    questions_history: List[QuestionDisplay]
    guess_history: List[GuessDisplay]
    remaining_questions: int
    remaining_guesses: int
    is_game_over: bool
    won: bool
    date: str


class CountrydleEndState(BaseModel):
    user: UserDisplay
    country: CountryDisplay
    questions_history: List[FullQuestionDisplay]
    guess_history: List[GuessDisplay]
    remaining_questions: int
    remaining_guesses: int
    is_game_over: bool
    won: bool
    date: str
