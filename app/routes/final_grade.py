from flask import Blueprint
from ..services import final_grade

# Create blueprint
bp_final_grade = Blueprint('final_grade', __name__)

# Get all final grade by test
@bp_final_grade.route('/api/final_grade_by_test/<test_id>', methods=['GET'])
def get_final_grade_by_test(test_id):
    return final_grade.get_final_grade_by_test(test_id)

# Get final grade by student
@bp_final_grade.route('/api/final_grade_by_student/<student_id>', methods=['GET'])
def get_final_grade_by_student(student_id):
    return final_grade.get_final_grade_by_student(student_id)
