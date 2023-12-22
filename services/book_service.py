from models.book_model import BookModel
from resources import db


class BookService:
    def get_book_by_id(self, book_id: int):
        return db.session.get(BookModel, book_id)
