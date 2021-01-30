from app import db, ma

# Template class/model
class Template(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    template_id = db.Column(db.Integer, nullable=False)
    question = db.Column(db.Integer, nullable=False)
    answer = db.Column(db.String(1), nullable=False)
    weight = db.Column(db.Integer, nullable=False)

    def __init__(self, template_id, question, answer, weight):
        self.template_id = template_id
        self.question = question
        self.answer = answer
        self.weight = weight

# Template schema
class TemplateSchema(ma.Schema):
    class Meta:
        fields = ('id', 'template_id', 'question', 'answer', 'weight')

# Init schema
template_schema = TemplateSchema()
templates_schema = TemplateSchema(many=True)
