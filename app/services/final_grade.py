from flask import jsonify
from ..models.answers import Answers, answers_schema
from ..models.student_test import StudentTest, students_tests_schema
from ..models.student import Student, student_schema
from ..models.template import Template, templates_schema

# Global variables
test_grade = 0
tests_grade = []

# Get all final grade by test
def get_final_grade_by_test(test_id):
    try:
        global test_grade
        global tests_grade

        result = []

        students_tests = students_tests_schema.dump(StudentTest.query.filter(StudentTest.test_id == test_id).all())
        if not students_tests:
            return jsonify({'message': 'test not found', 'data': {}}), 404

        for item in students_tests:
            student_tests = students_tests_schema.dump(StudentTest.query.filter(StudentTest.student_id == item['student_id']).all())
            if not student_tests:
                break

            for data in student_tests:
                answers = answers_schema.dump(Answers.query.filter(Answers.answers_id == data['student_test_id']).all())
                if not answers:
                    break

                template = templates_schema.dump(Template.query.filter(Template.template_id == data['test_id']).all())
                if not template:
                    break

                for answ in answers:
                    for temp in template:
                        if answ['question'] == temp['question']:
                            if answ['answer'] == temp['answer']:
                                test_grade += 1 * temp['weight']

                tests_grade.append({
                    'test_id': data['test_id'],
                    'test_grade': test_grade
                })

                test_grade = 0

            sum_tests_grade = 0
            qty_test = 0
            for test in tests_grade:
                # business rule
                sum_tests_grade += test['test_grade']
                qty_test += 1

            final_grade = sum_tests_grade / qty_test

            # business rule
            if final_grade == 0:
                final_grade = 1

            # business rule
            if final_grade == 10:
                final_grade = 9

            # business rule
            if final_grade > 7:
                status = 'aprovado'
            else:
                status = 'reprovado'

            student = student_schema.dump(Student.query.get(item['student_id']))

            result.append({
                'student_id': item['student_id'],
                'name': student['name'],
                'final_grade': final_grade,
                'status': status
            })

            tests_grade = []
        return jsonify({'message': 'successfully fetched', 'data': result}), 200
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# ---------------------------------------

# Get final grade by student
def get_final_grade_by_student(student_id):
    try:
        global test_grade
        global tests_grade

        result = []
        
        student_tests = students_tests_schema.dump(StudentTest.query.filter(StudentTest.student_id == student_id).all())        
        if not student_tests:
            return jsonify({'message': "student not found", 'data': {}}), 404

        for data in student_tests:
            answers = answers_schema.dump(Answers.query.filter(Answers.answers_id == data['student_test_id']).all())
            if not answers:
                return jsonify({'message': "answers not found", 'data': {}}), 404

            template = templates_schema.dump(Template.query.filter(Template.template_id == data['test_id']).all())
            if not template:
                return jsonify({'message': "test not found", 'data': {}}), 404

            for answ in answers:
                for temp in template:
                    if answ['question'] == temp['question']:
                        if answ['answer'] == temp['answer']:
                            test_grade += 1 * temp['weight']

            tests_grade.append({
                'test_id': data['test_id'],
                'test_grade': test_grade
            })

            test_grade = 0

        sum_tests_grade = 0
        qty_test = 0
        for test in tests_grade:
            # business rule
            sum_tests_grade += test['test_grade']
            qty_test += 1

        final_grade = sum_tests_grade / qty_test

        # business rule
        if final_grade == 0:
            final_grade = 1

        # business rule
        if final_grade == 10:
            final_grade = 9

        # business rule
        if final_grade > 7:
            status = 'aprovado'
        else:
            status = 'reprovado'

        student = student_schema.dump(Student.query.get(student_id))

        result.append({
            'student_id': student['student_id'],
            'name': student['name'],
            'final_grade': final_grade,
            'status': status
        })

        tests_grade = []
        return jsonify({'message': 'successfully fetched', 'data': result}), 200
    except:
        return jsonify({'message': 'server error', 'data': {}}), 404
