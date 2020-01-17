rom flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired

class Pomo_Form(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    description = TextAreaField('Create a Pomo', validators=[DataRequired()])  
    submit = SubmitField('Submit')

class Update_Profile(FlaskForm):
    bio = TextAreaField('Add something about Yourself...', validators = [DataRequired()])
    submit = SubmitField('Submit')