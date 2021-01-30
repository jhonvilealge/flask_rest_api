from app import db
from flask import request, jsonify
from ..models.student_test import StudentTest, student_test_schema, students_tests_schema
from ..models.answers import Answers, answers_schema
from ..models.student import Student
from ..models.test import Test

# Create a student/test
def post_student_test():
    try:
        print('entrei')
        student_id = request.json['student_id']
        test_id = request.json['test_id']
        answers = request.json['answers']

        get_student_by_id = Student.query.get(student_id)
        get_test_by_id = Test.query.get(test_id)

        if not get_student_by_id and not get_test_by_id:
            return jsonify({'message': 'student and test not found', 'data': {}}), 404

        if not get_student_by_id:
            return jsonify({'message': 'student not found', 'data': {}}), 404
            
        if not get_test_by_id:
            return jsonify({'message': 'test not found', 'data': {}}), 404

        new_student_test = StudentTest(student_id, test_id)
        db.session.add(new_student_test)
        db.session.commit()
        result_student_test = student_test_schema.dump(new_student_test)

        result_student_answers = post_student_answers(answers, result_student_test['student_test_id'])
        if not result_student_answers:
            student_test = StudentTest.query.get(result_student_test['student_test_id'])
            if student_test:
                db.session.delete(student_test)
                db.session.commit()
            return jsonify({'message': 'unable to create student responses', 'data': {}}), 200

        result = {
            'student_test_id': result_student_test['student_test_id'],
            'student_id': result_student_test['student_id'],
            'test_id': result_student_test['test_id'],
            'answers': result_student_answers,
            'created_on': result_student_test['created_on']
        }
        return jsonify({'message': 'seccessfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

def post_student_answers(answers, student_test_id):
    try:
        for data in answers:
            new_student_answers = Answers(
                student_test_id,
                data['question'],
                data['answer']
            )
            db.session.add(new_student_answers)
        db.session.commit()
        return answers
    except:
        return None

# ---------------------------------------

# Get all students/tests
def get_students_tests():
    try:
        students_tests = students_tests_schema.dump(StudentTest.query.all())
        if not students_tests:
            return jsonify({'message': 'data not found', 'data': {}}), 404

        result = []
        
        for data in students_tests:
            student_answers = answers_schema.dump(Answers.query.filter(Answers.answers_id == data['student_test_id']).all())
            student_answers_json = []

            for field in student_answers:
                student_answers_json.append({
                    'question': field['question'],
                    'answer': field['answer']
                })

            result.append({
                'student_test_id': data['student_test_id'],
                'student_id': data['student_id'],
                'test_id': data['test_id'],
                'answers': student_answers_json,
                'created_on': data['created_on']
            })
        return jsonify({'message': 'successfully fetched', 'data': result}), 200
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# ---------------------------------------

# Get a single student/test
def get_student_test(student_test_id):
    try:
        student_test = student_test_schema.dump(StudentTest.query.get(student_test_id))
        student_answers = answers_schema.dump(Answers.query.filter(Answers.answers_id == student_test['student_test_id']).all())
        student_answers_json = []

        for field in student_answers:
            student_answers_json.append({
                'question': field['question'],
                'answer': field['answer']
            })

        result = {
            'student_test_id': student_test['student_test_id'],
            'student_id': student_test['student_id'],
            'test_id': student_test['test_id'],
            'answers': student_answers_json,
            'created_on': student_test['created_on']
        }
        return jsonify({'message': 'successfully fetched', 'data': result}), 200
    except:
        return jsonify({'message': 'data not found', 'data': {}}), 404
