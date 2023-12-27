from datetime import datetime

from flask import request, Response
from flask_apispec import MethodResource, doc
from flask_restful import Resource

from common.api_tools import token_required
from models.book_model import BookModel
from resources import app, api, docs
from services.book_service import BookService


class BookResource(MethodResource, Resource):
    @doc(description="Get a book's information", tags=['Book Requests'])
    def get(self, book_id: int):
        book_model = BookService().get_book_by_id(book_id)
        if book_model:
            return book_model.serialize()
        else:
            return {'error': f'Book not found for id: {book_id}'}, 404

    @doc(description="Update a book's information", tags=['Book Requests'])
    @token_required()
    def put(self, book_id: int):
        try:
            request_json = request.json
            if request_json:
                name = request_json.get('name', None)
                author = request_json.get('author', None)
                publish_time_str = request_json.get('publish_time', None)
                publish_time = datetime.fromisoformat(publish_time_str) if publish_time_str else None

                book_model = BookModel(id=book_id, name=name, author=author, publish_time=publish_time)
                book_model = BookService().update_book(book_model)

                return book_model.serialize()
            else:
                return {'error': 'Please provide book info as a json'}, 400
        except Exception as error:
            return {'error': f'{error}'}, 400


class BookListResource(Resource):
    def get(self):
        book_list = BookService().get_all_books()
        return [book_model.serialize() for book_model in book_list]

    @token_required()
    def post(self):
        try:
            request_json = request.json
            if request_json:
                name = request_json.get('name', None)
                author = request_json.get('author', None)
                publish_time = datetime.fromisoformat(request_json.get('publish_time', None))

                book_model = BookModel(name=name, author=author, publish_time=publish_time)
                BookService().create_book(book_model)

                return book_model.serialize()
            else:
                return {'error': 'Please provide book info as a json'}, 400
        except Exception as error:
            return {'error': f'{error}'}, 400


api.add_resource(BookResource, '/books/<int:book_id>')
api.add_resource(BookListResource, '/books')

docs.register(BookResource)


@app.route('/swagger.yaml')
def generate_swagger_yaml():
    yaml_doc = docs.spec.to_yaml()
    return Response(yaml_doc, mimetype="text/yaml")

