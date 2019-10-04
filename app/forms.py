from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,SubmitField
from wtforms.validators import DataRequired


class SearchForm_logic(FlaskForm):
    criteria = SelectField('Criteria', choices=[('name', 'NAME'),('acno', 'Account Number'),('sn', 'Serial Number')], render_kw={"placeholder":"Start typing ..."})
    identifier = StringField('Identifier', validators=[DataRequired()])
    search = SubmitField('Search')
     

class ConsentForm_logic(FlaskForm):
    accepted_unit = StringField('Shares Accepted', validators=[])
    additional_unit = StringField('Additional Unit', validators=[])
    submit = SubmitField('submit')
    