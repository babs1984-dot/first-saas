from pydantic import BaseModel


class TextPayload(BaseModel):
    text: str


class CircularPayload(BaseModel):
    topic: str
    tone: str
    circular_type: str


class UserRegister(BaseModel):
    username: str
    password: str


class UserLogin(BaseModel):
    username: str
    password: str
