from app import db, ma
import datetime

# Student class/model
class Student(db.Model):
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    cpf = db.Column(db.String(15), unique=True, nullable=False)
    course = db.Column(db.String(30), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    phone = db.Column(db.String(15), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, name, cpf, course, email, phone):
        self.name = name
        self.cpf = cpf
        self.course = course
        self.email = email
        self.phone = phone

# Student schema
class StudentSchema(ma.Schema):
    class Meta:
        fields = ('student_id', 'name', 'cpf', 'course','email', 'phone', 'created_on')

# Init schema
student_schema = StudentSchema()
students_schema = StudentSchema(many=True)
