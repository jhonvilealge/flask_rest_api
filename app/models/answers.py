from app import db, ma

# Answers class/model
class Answers(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    answers_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.String(1), nullable=False)

    def __init__(self, answers_id, question, answer):
        self.answers_id = answers_id
        self.question = question
        self.answer = answer

# Answers schema
class AnswersSchema(ma.Schema):
    class Meta:
        fields = ('id', 'answers_id', 'question', 'answer')

# Init schema
answer_schema = AnswersSchema()
answers_schema = AnswersSchema(many=True)
