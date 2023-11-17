# forms.py
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, Length

class TaskForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)]),
    des = StringField('Title', validators=[DataRequired(), Length(min=2, max=50)])
    submit = SubmitField('Submit')
