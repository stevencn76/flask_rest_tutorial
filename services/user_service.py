from sqlalchemy import Select

from models.user_model import UserModel
from resources import db


class UserService:
    def login(self, username: str, password: str):
        query = Select(UserModel).where(UserModel.username == username)
        user_model = db.session.scalars(query).first()
        if user_model and user_model.password == password:
            return user_model
        else:
            return None
