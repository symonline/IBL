from flask import render_template, request, redirect, url_for, flash,session
from app import app, db
# from flask_login import login_user
from app.models import ShareHolder, Right
from app.forms import SearchForm_logic, ConsentForm_logic

@app.route('/')
@app.route('/index')
def index():
    info='WELCOME TO THE IBL RIGHT OFFER TEST PAGE'
    
    return redirect(url_for('search'))
    #return render_template('search.html', title='HOME', info = info)
    '''
        if request.methods == 'POST':
            account = request.form['account_number']
            print (account.value)
            if account.value == '':
                return render_template('index.htm', message='Please enter required field')
        #if db.session.query(Rights).filter(Rights.id==account).count()==0:

        return render_template('success.html', account = account)
    '''
@app.route('/search', methods=['GET', 'POST'])
def search():
    # load the form object with arguments from form.py
    sform = SearchForm_logic()
    # check whether the form validation passes all conditions 
    if sform.validate_on_submit():
        # load the the account number/ name /etc from the form class (form.py)
        sholder_name = sform.identifier.data
        schoice = sform.criteria.data
        # load the Shareholder model db method/function by passing form(name/acc_no/etc) agument
        shareholders = ShareHolder.get_shareholder_by_value(schoice,sholder_name)
        if not shareholders:
            # display a not succefull message and return the user back to the Search page
            flash ("Share Holder Number is either wrong or Don't exist")
            return redirect(url_for('search'))
        # display a successful message from validation on the base template
        flash(f'Right info requested for Shareholder: {sform.criteria.data}, Identifier: { sform.identifier.data}')
        # get the equivallent rights details
        # on the assumption that a shareholder to a right (one to one relationship)
        # name=session[shareholders]:
        right = Right.get_right_by_acno(shareholders.acno)
        # send the Shareholder bio details with his/her Right detail
        # to be displayed / rendered on the result.html page
        session['ACNO'] = shareholders.acno
        session['NAME'] = shareholders.name
        session['SN'] = shareholders.sn
        session['RACNO'] = right.acno
        session['RIGHT_DUE'] = right.right_due
        session['UNIT_HELD'] = right.unit_held
        session['COMP'] = right.company
        session['RDATE'] = right.right_date
        session['RIGHT_APPLIED'] = right.right_applied
        session['ADDITIONAL'] = right.additional_apply
        session['AMOUNT'] = right.amount
        return render_template ('result.html', 
                        title='HOME', 
                        acno = session.get('ACNO'), 
                        racno = session.get('RACNO'),
                        name = session.get('NAME'),
                        sn = session.get('SN'),
                        right_due = session.get('RIGHT_DUE'),
                        unit_held = session.get('UNIT_HELD'),
                        right_applied = session.get('RIGHT_APPLIED'),
                        additional = session.get('ADDITIONAL'),
                        amount = session.get('AMOUNT')
                        )
    # Always return the search page if validation fail
    return render_template('search.html', title='Find Right', sform = sform)


@app.route('/acceptance', methods=['GET','POST'])
def acceptance():
    #if request.method == 'GET'
    if request.method =='POST':
        '''
        unit_applied = session.get('RIGHT_APPLIED')
        unit_due = session.get('RIGHT_DUE')
        addition = session.get('ADDITIONAL_RIGHT')
        '''
        session['RIGHT_APPLIED'] = request.form.get('applied',type=int)
        session['ADDITIONAL'] = request.form.get('additional',type=int)

        consent = session.get('RIGHT_APPLIED')
        added = session.get('ADDITIONAL')
        if not (consent) :
            flash ("Consent field can not be empty ")
            session['SUBMITTED']=False
            return render_template ('result.html')
        consent_check = isinstance(consent, int)
        added_check = isinstance(added, int)

        if not consent_check: #or added_check :
            flash ("Applied Unit field must be numeric ")
            session['SUBMITTED']=False
            return render_template ('result.html')
        
        if not added_check: #or added_check :
            flash ("Additional Unit field must be numeric ")
            consent=0
            session['ADDITIONAL']=0
            #session['SUBMITTED']=False
            #return render_template ('result.html')

        if not (consent or added):
            session['RIGHT_APPLIED']=0
            session['ADDITIONAL']=0

        # Some RULES before for right is accepted
        if int(consent) > int(session.get('RIGHT_DUE')) :
            flash ("Unit Applied for Can not be Greater than Unit Entitled!")
            session['SUBMITTED']=False
            return render_template ('result.html')

        elif int(consent) != int(session.get('RIGHT_DUE')) and int(added) :
            flash ("Additional Unit is not Allowed while Entitled Right Has Not Been Fully Accepted!")
            session['SUBMITTED']=False
            return render_template ('result.html')   

        account = int(session.get('ACNO'))
        rights=Right.get_right_by_acno(account)
        
        rights.update_right_applied(consent)
        rights.update_additional_right(added) 
        flash ("Consent Information has been is saved")
        session['SUBMITTED']=True
        return render_template('ibl_report.html', 
                        right_applied=int(consent), 
                        additional_right_applied = int(added))

    #request.method =='GET' and session.get('RIGHT_APPLIED'):
    return render_template ('result.html')

@app.route('/convert2pdf',methods=['GET', 'POST'])
def convert2pdf():
    # convert to pdf and clear session
    pass