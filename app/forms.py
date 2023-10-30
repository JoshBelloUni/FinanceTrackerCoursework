from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired

class ExpensesForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])

class IncomesForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[DataRequired()])

class GoalsForm(FlaskForm):
    goal = StringField('Goal', validators=[DataRequired()])
    amount = FloatField('Amount', validators=[DataRequired()])
