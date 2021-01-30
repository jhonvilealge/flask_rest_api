from flask import Blueprint
from ..services import student

# Create blueprint
bp_student = Blueprint('student', __name__)

# Create a student
@bp_student.route('/api/student', methods=['POST'])
def post_student():
    return student.post_student()

# Get all students
@bp_student.route('/api/student', methods=['GET'])
def get_students():
    return student.get_students()

# Get a single student
@bp_student.route('/api/student/<student_id>', methods=['GET'])
def get_student(student_id):
    return student.get_student(student_id)

# Update a student
@bp_student.route('/api/student/<student_id>', methods=['PUT'])
def update_student(student_id):
    return student.update_student(student_id)

# Delete a student
@bp_student.route('/api/student/<student_id>', methods=['DELETE'])
def delete_student(student_id):
    return student.delete_student(student_id)
