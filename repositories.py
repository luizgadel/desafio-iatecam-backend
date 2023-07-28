from sqlalchemy.orm import Session
from models import User, Product, Category

class UserRepository:
    @staticmethod
    def find_all(db: Session) -> list[User]:
        return db.query(User).all()
    
    @staticmethod
    def save(db: Session, user: User) -> User:
        if user.id:
            db.merge(user)
        else:
            db.add(user)
        db.commit()
        return user

    @staticmethod
    def find_by_id(db: Session, id: int) -> User:
        return db.query(User).filter(User.id == id).first()

    @staticmethod
    def exists_by_id(db: Session, id: int) -> bool:
        return db.query(User).filter(User.id == id).first() is not None

    @staticmethod
    def delete_by_id(db: Session, id: int) -> None:
        user = db.query(User).filter(User.id == id).first()
        if user is not None:
            db.delete(user)
            db.commit()

    @staticmethod
    def authenticate(db: Session, user: User) -> User:
        return db.query(User).filter(User.email == user.email).filter(User.password == user.password).first()

class ProductRepository:
    @staticmethod
    def find_all(db: Session) -> list[Product]:
        return db.query(Product).all()

    @staticmethod
    def save(db: Session, product: Product) -> Product:
        if product.id:
            db.merge(product)
        else:
            db.add(product)
        db.commit()
        return product

class CategoryRepository:
    @staticmethod
    def find_all(db: Session) -> list[Category]:
        return db.query(Category).all()

    @staticmethod
    def save(db: Session, category: Category) -> Category:
        if category.id:
            db.merge(category)
        else:
            db.add(category)
        db.commit()
        return category

    @staticmethod
    def find_by_id(db: Session, id: int) -> Category:
        return db.query(Category).filter(Category.id == id).first()