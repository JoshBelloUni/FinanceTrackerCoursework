from flask_wtf import FlaskForm
from wtforms import StringField, FloatField, IntegerField
from wtforms.validators import DataRequired, NumberRange, ValidationError

# function to validate if the data is only 2 decimal places
def validate_two_decimal_places(form, field):
    if field.data is not None:
        parts = str(field.data).split('.')
        if len(parts) > 1 and len(parts[1]) > 2:
            raise ValidationError('Only two decimal places are allowed.')

# classes to add things to the form which will add data to the databases
class ExpensesForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[
                                        DataRequired(),
                                        NumberRange(min=0.01, max=1000000.00, message="Invalid cost"),
                                        validate_two_decimal_places
                                          ])

class IncomesForm(FlaskForm):
    type = StringField('Type', validators=[DataRequired()])
    cost = FloatField('Cost', validators=[
                                        DataRequired(),
                                        NumberRange(min=0.01, max=1000000.00, message="Invalid cost"),
                                        validate_two_decimal_places
                                          ])

class GoalsForm(FlaskForm):
    goal = StringField('Goal')
    amount = FloatField('Amount', validators=[
                                            DataRequired(),
                                            NumberRange(min=0.01, max=100000000.00, message="Invalid amount for your goal",),
                                            validate_two_decimal_places
                                            ])
