from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from resources import db


class UserModel(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(128), nullable=False, unique=True)
    password: Mapped[str] = mapped_column(String(128), nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username
        }
