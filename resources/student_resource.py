from flask_restful import Resource
from resources import api


class StudentResource(Resource):
    def get(self, student_id: int):
        if student_id == 1:
            return {'id': student_id, 'name': 'Jack', 'gender': 'male'}
        else:
            return {'error': f'Student not found for id: {student_id}'}, 404

    def put(self, student_id: int):
        return {'id': student_id, 'name': 'Mary', 'gender': 'female'}


api.add_resource(StudentResource, '/students/<int:student_id>')
