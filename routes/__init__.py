from flask import Flask


app = Flask(__name__)


from routes import student_api
