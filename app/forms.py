from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,SubmitField
from wtforms.validators import DataRequired


class SearchForm_logic(FlaskForm):
    criteria = SelectField('Criteria', choices=[('1', 'BVN'), ('2', 'ACCOUNT NO'), ('3', 'CHN')])
    identifier = StringField('Identifier', validators=[DataRequired()])
    search = SubmitField('Search')
     

class ConsentForm_logic(FlaskForm):
    accepted_right = StringField('Accepted_right', alidators=[DataRequired()])
    find = SubmitField('Find')
    