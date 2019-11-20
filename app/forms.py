from flask_wtf import FlaskForm
from wtforms import SelectField, StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired, Length


class SearchForm_logic(FlaskForm):
    criteria = SelectField('Select Name or Account Number:',  choices=[('name', 'NAME'),('acno', 'ACCOUNT NUMBER')], 
    render_kw={"placeholder":"Start typing ..."})

    identifier = StringField('Type Name or Account Number here',description=['For Name search: You can either enter your Last Name, \
    First Name, Other Name , Full Name','Enter CSCS Account Number'], 
    validators=[DataRequired(), Length(min=1,max=35,message='Search value is not permitted')])
    search = SubmitField('Search')
     

class ConsentForm_logic(FlaskForm):
    accepted_unit = IntegerField('Shares Accepted', default='',validators=[DataRequired()])
    additional_unit = IntegerField('Additional Unit', validators=[])
    submit = SubmitField('Find')
    