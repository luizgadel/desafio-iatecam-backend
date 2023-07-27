from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from models import User
from repositories import UserRepository
from schemas import UserRequest, UserResponse, AuthenticateRequest
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:4200"],
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True
)

def get_db():
    try: 
        db = SessionLocal()
        yield db
    finally:
        db.close()

@app.get("/api/user")
def find_all_user(db: Session = Depends(get_db)):
    users = UserRepository.find_all(db)
    return [UserResponse.from_orm(user) for user in users]
    

@app.post("/api/user", response_model=UserResponse, status_code=status.HTTP_201_CREATED)
def create_user(request: UserRequest, db: Session = Depends(get_db)):
    user = UserRepository.save(db, User(**request.dict()))
    return UserResponse.from_orm(user)

@app.post("/api/authenticate", response_model=UserResponse)
def authenticate(request: AuthenticateRequest, db: Session = Depends(get_db)):
    user = UserRepository.authenticate(db, User(**request.dict()))
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Email ou senha incorretos."
        )
    return UserResponse.from_orm(user)
    
