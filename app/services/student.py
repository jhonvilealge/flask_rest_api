from app.models.answers import Answers
from app.models.student_test import StudentTest, student_test_schema
from app import db
from flask import request, jsonify
from ..models.student import Student, student_schema, students_schema

# Create a student
def post_student():
    try:
        name = request.json['name']
        cpf = request.json['cpf']
        course = request.json['course']
        email = request.json['email']
        phone = request.json['phone']

        # business rule
        students = students_schema.dump(Student.query.all())
        if len(students) >= 100:
            return jsonify({'message': 'student limit exceeded', 'data': students}), 200
        
        # Filter student by cpf
        student = student_by_cpf(cpf)
        if student:
            return jsonify({'message': 'student already exists', 'data': {}}), 200
        
        new_student = Student(name, cpf, course, email, phone)
    
        db.session.add(new_student)
        db.session.commit()
        result = student_schema.dump(new_student)
        return jsonify({'message': 'seccessfully registered', 'data': result}), 201
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# Filter student by cpf
def student_by_cpf(cpf):
    try:
        return Student.query.filter(Student.cpf == cpf).one()
    except:
        return None

# ---------------------------------------

# Get all students
def get_students():
    students = students_schema.dump(Student.query.all())
    if students:
        return jsonify({'message': 'successfully fetched', 'data': students}), 200
    return jsonify({'message': 'data not found', 'data': {}}), 404

# ---------------------------------------

# Get a single student
def get_student(student_id):
    student = student_schema.dump(Student.query.get(student_id))
    if student:
        return jsonify({'message': 'successfully fetched', 'data': student}), 200
    return jsonify({'message': "student not found", 'data': {}}), 404

# ---------------------------------------

# Update a student
def update_student(student_id):
    try:
        name = request.json['name']
        cpf = request.json['cpf']
        course = request.json['course']
        email = request.json['email']
        phone = request.json['phone']

        student = Student.query.get(student_id)
        if not student:
            return jsonify({'message': "student not found", 'data': {}}), 404
        
        student.name = name
        student.cpf = cpf
        student.course = course
        student.email = email
        student.phone = phone
        db.session.commit()
        result = student_schema.dump(student)
        return jsonify({'message': 'successfully updated', 'data': result}), 201
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# ---------------------------------------

# Delete a student
def delete_student(student_id):
    try:
        student = Student.query.get(student_id)
        if not student:
            return jsonify({'message': "student not found", 'data': {}}), 404

        # Delete all tests for this student
        delete_student_tests(student_id)
    
        db.session.delete(student)
        db.session.commit()
        result = student_schema.dump(student)
        return jsonify({'message': 'successfully deleted', 'data': result}), 200
    except:
        return jsonify({'message': 'server error', 'data': {}}), 500

# Delete all tests for this student
def delete_student_tests(student_id):
    try:
        student_tests = StudentTest.query.filter(StudentTest.student_id == student_id).all()
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
