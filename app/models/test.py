from app import db, ma
import datetime

# Test class/model
class Test(db.Model):
    test_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(100), nullable=False)
    teacher = db.Column(db.String(50), nullable=False)
    created_on = db.Column(db.DateTime, default=datetime.datetime.now())

    def __init__(self, name, description, teacher):
        self.name = name
        self.description = description
        self.teacher = teacher

# Test schema
class TestSchema(ma.Schema):
    class Meta:
        fields = ('test_id', 'name', 'description', 'teacher', 'created_on')

# Init schema
test_schema = TestSchema()
tests_schema = TestSchema(many=True)
