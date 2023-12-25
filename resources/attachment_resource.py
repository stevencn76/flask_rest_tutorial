from flask import send_file
from flask_restful import Resource, reqparse
from werkzeug.datastructures import FileStorage
from common import utils
from resources import api


class AttachmentListResource(Resource):
    def __init__(self):
        self.parser = reqparse.RequestParser()
        self.parser.add_argument("attachment", required=True, type=FileStorage, location="files",
                                 help="Please provide attachment file")

    def post(self):
        attachment_file = self.parser.parse_args().get("attachment")
        file_path = utils.get_attachment_path().joinpath(attachment_file.filename)
        attachment_file.save(file_path)

        return {'message': 'ok'}


class AttachmentResource(Resource):
    def get(self, filename):
        file_path = utils.get_attachment_path().joinpath(filename)
        return send_file(file_path)


api.add_resource(AttachmentListResource, '/attachments')
api.add_resource(AttachmentResource, '/attachments/<filename>')
