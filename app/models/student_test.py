from app import db, ma
import datetime

# StudentTest class/model
class StudentTest(db.Model):
    student_test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    student_id = db.Column(db.Integer, nullable=False)
    test_id = db.Column(db.Integer, nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, student_id, test_id):
        self.student_id = student_id
        self.test_id = test_id

# StudentTest schema
class StudentTestSchema(ma.Schema):
    class Meta:
        fields = ('student_test_id', 'student_id', 'test_id', 'created_on')

# Init schema
student_test_schema = StudentTestSchema()
students_tests_schema = StudentTestSchema(many=True)
