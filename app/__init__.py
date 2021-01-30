from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .models import *

# Init app
app = Flask(__name__)
app.config.from_object('config')

# Init sqlalchemy
db = SQLAlchemy(app)

# Init marshmallow
ma = Marshmallow(app)

# Migrate database
Migrate(app, db)

# Import blueprint final_grade
from .routes import final_grade
app.register_blueprint(final_grade.bp_final_grade)

# Import blueprint student_test
from .routes import student_test
app.register_blueprint(student_test.bp_student_test)

# Import blueprint student
from .routes import student
app.register_blueprint(student.bp_student)

# Import blueprint template
from .routes import test
app.register_blueprint(test.bp_test)
