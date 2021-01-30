from app.models.answers import Answers
from app.models.student_test import StudentTest, student_test_schema
from app import db
from flask import request, jsonify
from ..models.test import Test, test_schema, tests_schema
from ..models.template import Template, templates_schema

# Create a test
def post_test():
    try:
        name = request.json['name']
        description = request.json['description']
        teacher = request.json['teacher']
        template = request.json['template']

        new_test = Test(name, description, teacher)
        db.session.add(new_test)
        db.session.commit()

        result_test = test_schema.dump(new_test)
        result_template = post_template(template, result_test['test_id'])
        
        if not result_template:
            test = Test.query.get(result_test['test_id'])
            if test:
                db.session.delete(test)
                db.session.commit()
            return jsonify({'message': 'unable to create test', 'data': {}}), 200

        result = {
            'test_id': result_test['test_id'],
            'name': result_test['name'],
            'description': result_test['description'],
            'teacher': result_test['teacher'],
            'template': result_template,
            'created_on': result_test['created_on']
        }
        return jsonify({'message': 'seccessfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'server error', 'data': {}}), 

def post_template(template, test_id):
    try:
        for data in template:
            # business rule
            if data['weight'] < 1:
                return None

            new_template = Template(
                test_id,
                data['question'],
                data['answer'],
                data['weight']
            )
            db.session.add(new_template)
        db.session.commit()
        return template
    except:
        return None

# ---------------------------------------

# Get all tests
def get_tests():
    try:
        tests = tests_schema.dump(Test.query.all())
        if not tests:
            return jsonify({'message': 'data not found', 'data': {}}), 404
        
        result = []
        
        for data in tests:
            template = templates_schema.dump(Template.query.filter(Template.template_id == data['test_id']).all())
            template_json = []

            for field in template:
                template_json.append({
                    'question': field['question'],
                    'answer': field['answer'],
                    'weight': field['weight']
                })

            result.append({
                'test_id': data['test_id'],
                'name': data['name'],
                'description': data['description'],
                'teacher': data['teacher'],
                'template': template_json,
                'created_on': data['created_on']
            })
        return jsonify({'message': 'successfully fetched', 'data': result}), 200
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# ---------------------------------------

# Get a single test
def get_test(test_id):
    try:
        test = test_schema.dump(Test.query.get(test_id))
        if not test:
            return jsonify({'message': 'test not found', 'data': {}}), 404
        
        template = templates_schema.dump(Template.query.filter(Template.template_id == test['test_id']).all())
        template_json = []

        for field in template:
            template_json.append({
                'question': field['question'],
                'answer': field['answer'],
                'weight': field['weight']
            })

        result = {
            'test_id': test['test_id'],
            'name': test['name'],
            'description': test['description'],
            'teacher': test['teacher'],
            'template': template_json,
            'created_on': test['created_on']
        }
        return jsonify({'message': 'successfully fetched', 'data': result}), 200
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# ---------------------------------------

# Delete a test
def delete_test(test_id):
    try:
        test = Test.query.get(test_id)
        if not test:
            return jsonify({'message': "test not found", 'data': {}}), 404

        # Delete template for this test
        delete_template(test_id)

        # Delete all students for this test
        delete_student_tests(test_id)
    
        db.session.delete(test)
        db.session.commit()
        result = test_schema.dump(test)
        return jsonify({'message': 'successfully deleted', 'data': result}), 200
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# Delete template for this test
def delete_template(test_id):
    try:
        template = Template.query.filter(Template.template_id == test_id).all()
        for data in template:
            db.session.delete(data)
            
        db.session.commit()
        return {}
    except:
        return None

# Delete all students for this test
def delete_student_tests(test_id):
    try:
        student_tests = StudentTest.query.filter(StudentTest.test_id == test_id).all()
        for test in student_tests:
            data_tests = student_test_schema.dump(test)
            answers = Answers.query.filter(Answers.answers_id == data_tests['student_test_id']).all()
            for answer in answers:
                db.session.delete(answer)
                
            db.session.delete(test)
            
        db.session.commit()
        return {}
    except:
        return None
