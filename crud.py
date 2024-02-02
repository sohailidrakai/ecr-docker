from sqlalchemy.orm import Session
from models import User

def get_users(db: Session):
    return db.query(User).all()

def create_user(db: Session, user):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user):
    db_user = db.query(User).filter(User.id == user_id).first()
    db_user.name = user.name
    db_user.email = user.email
    db.commit()
    db.refresh(db_user)
    return db_user
