from fastapi import FastAPI, status, Depends, HTTPException
from sqlalchemy.orm import Session
import models
from models import User, Product, Category
from repositories import UserRepository, ProductRepository, CategoryRepository
from schemas import UserRequest, UserResponse, AuthenticateRequest, CategoryRequest, CategoryResponse, ProductRequest, ProductResponse
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
    
@app.get("/api/category")
def find_all_category(db: Session = Depends(get_db)):
    categorys = CategoryRepository.find_all(db)
    return [CategoryResponse.from_orm(category) for category in categorys]

@app.post("/api/category", response_model=CategoryResponse, status_code=status.HTTP_201_CREATED)
def create_category(request: CategoryRequest, db: Session = Depends(get_db)):
    category = CategoryRepository.save(db, Category(**request.dict()))
    return CategoryResponse.from_orm(category)
    
@app.get("/api/product")
def find_all_product(db: Session = Depends(get_db)):
    products = ProductRepository.find_all(db)
    return [ProductResponse.from_orm(product) for product in products]

@app.post("/api/product", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
def create_product(request: ProductRequest, db: Session = Depends(get_db)):
    product = ProductRepository.save(db, Product(**request.dict()))
    return ProductResponse.from_orm(product)