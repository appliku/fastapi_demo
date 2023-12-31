import os

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from starlette.responses import HTMLResponse

app = FastAPI()

DATABASE_URL = os.environ['DATABASE_URL']
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, index=True)
    message = Column(String, index=True)


# Create the table in the database
Base.metadata.create_all(bind=engine)


class MessageIn(BaseModel):
    name: str
    email: str
    message: str


@app.post("/messages/", response_model=MessageIn)
def create_message(message: MessageIn):
    db_message = Message(**message.model_dump())
    db = SessionLocal()
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    db.close()
    return db_message


@app.get("/healthcheck/", response_model=str)
def healthcheck():
    return "OK"


if __name__ == "__main__":
    try:
        port = os.environ.get("PORT", "5000")
        port = int(port)
    except ValueError:
        port = 5000
    uvicorn.run("main:app", host='0.0.0.0', port=port, log_level="info")
