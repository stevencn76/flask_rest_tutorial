from datetime import datetime

from sqlalchemy import Integer, String, TIMESTAMP
from sqlalchemy.orm import Mapped, mapped_column

from resources import db


class BookModel(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(255), nullable=False, unique=True)
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    publish_time: Mapped[datetime] = mapped_column(TIMESTAMP, nullable=False)

    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'author': self.author,
            'publish_time': self.publish_time.isoformat()
        }
