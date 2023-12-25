from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:test@127.0.0.1/restful_db'
db = SQLAlchemy(app)


from resources import student_resource
from resources import book_resource
from resources import user_resource
from resources import attachment_resource
