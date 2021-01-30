from flask import Blueprint
from ..services import student_test

# Create blueprint
bp_student_test = Blueprint('student_test', __name__)

# Create a student/test
@bp_student_test.route('/api/student_test', methods=['POST'])
def post_student_test():
    return student_test.post_student_test()

# Get all students/tests
@bp_student_test.route('/api/student_test', methods=['GET'])
def get_students_tests():
    return student_test.get_students_tests()

# Get a single student/test
@bp_student_test.route('/api/student_test/<student_test_id>', methods=['GET'])
def get_student_test(student_test_id):
    return student_test.get_student_test(student_test_id)
