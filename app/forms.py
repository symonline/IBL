from flask_wtf import FlaskForm
from wtforms import SelectField, StringField, SubmitField, IntegerField
from wtforms.validators import DataRequired, Length


class SearchForm_logic(FlaskForm):

    info = ['For Name search: You can either enter your Last Name,\
             First Name, Other Name ,Full Name', 'Enter CSCS Account Number']
    info2 = 'Searched value is not allowed'
    criteria = SelectField('Select Name or Account Number:',
                           choices=[('name', 'NAME'),
                                    ('acno', 'ACCOUNT NUMBER')],
                           render_kw={"placeholder": "Start typing ..."})

    identifier = StringField('Type Name or Account Number here',
                             description=info,
                             validators=[DataRequired(),
                                         Length(min=2, max=35, message=info2)])
    
    identifier2 = SelectField('Select Company:',
                              choices=[('INTERNATIONAL BREWERIES PLC', 'INTERNATIONAL BREWERIES PLC'),
                                       ('lasaco', 'LASACO PLC'),
                                       ('ncr', 'NCR NIGERIA PLC'),
                                       ('nem', 'NEM INSURANCE PLC'),
                                       ('pharmadeko', 'PHARMA DEKO PLC'),
                                       ('interlinked', 'INTERLINKED TECHOLOGIES PLC')],
                              validators=[DataRequired(),
                                          Length(min=1, max=35, message=info2)],
                              render_kw={"placeholder": "Start typing ..."})
    
    search = SubmitField('Search')


class ConsentForm_logic(FlaskForm):
    accepted_unit = IntegerField('Shares Accepted', default='',
                                 validators=[DataRequired()])
    additional_unit = IntegerField('Additional Unit', validators=[])
    submit = SubmitField('Find')


class SearchFormCompany_logic(FlaskForm):

    info = ['For Name search: You can either enter your Last Name,\
             First Name, Other Name ,Full Name', 'Enter CSCS Account Number']
    info2 = 'Searched value is not allowed'
    Companies = ()
    criteria = SelectField('Select Company:',
                           choices=[('ibl', 'INTERNATIONAL BREWERIES PLC'),
                                    ('lasaco', 'LASACO'),
                                    ('ncr', 'NCR NIGERIA PLC'),
                                    ('nem', 'NEM INSURANCE PLC'),
                                    ('pharmadeko', 'PHARMA DEKO PLC'),
                                    ('interlinked', 'INTERLINKED TECHOLOGIES PLC')],
                           render_kw={"placeholder": "Start typing ..."})
    '''
    identifier = StringField('Type Name or Account ,Number here',
                             description=info,
                             validators=[DataRequired(),
                                         Length(min=1, max=35, message=info2)])
    search = SubmitField('Search')
    '''