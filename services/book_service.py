from sqlalchemy import Select, asc

from models.book_model import BookModel
from resources import db


class BookService:
    def get_book_by_id(self, book_id: int):
        return db.session.get(BookModel, book_id)

    def get_all_books(self):
        query = Select(BookModel).order_by(asc(BookModel.name))
        return db.session.scalars(query).all()

    def get_book_by_name(self, book_name: str):
        query = Select(BookModel).where(BookModel.name == book_name)
        return db.session.scalars(query).all()

    def create_book(self, book_model: BookModel):
        exist_books = self.get_book_by_name(book_model.name)
        if exist_books:
            raise Exception(f'Book exists with name "{book_model.name}"')

        db.session.add(book_model)
        db.session.commit()

        return book_model

    def update_book(self, book_model: BookModel):
        exist_book = self.get_book_by_id(book_model.id)
        if not exist_book:
            raise Exception(f'Book not found with id: {book_model.id}')

        if book_model.name:
            exist_book.name = book_model.name
        if book_model.author:
            exist_book.author = book_model.author
        if book_model.publish_time:
            exist_book.publish_time = book_model.publish_time

        db.session.commit()

        return exist_book
