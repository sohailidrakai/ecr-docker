from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import crud, models
from database import SessionLocal, engine
from pydantic import BaseModel

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

class UserBase(BaseModel):
    name: str
    email: str

@app.get("/users/", response_model=list[UserBase])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db)
    return users

@app.post("/users/", response_model=UserBase)
def create_user(user: UserBase, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.put("/users/{user_id}", response_model=UserBase)
def update_user(user_id: int, user: UserBase, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user=user)
