from flask import render_template, request, redirect, url_for, flash, session
from app import app, db
# from flask_login import login_user
from app.models import ShareHolder, Right, HoldersRight
from app.forms import SearchForm_logic, ConsentForm_logic
import pandas as pd

@app.route('/')
@app.route('/index')
def index():
    info='WELCOME TO THE IBL UNCLAIMED DIVIDEND PAGE'
    
    return redirect(url_for('search'))
    #return render_template('search.html', title='HOME', info = info)
   
@app.route('/search', methods=['GET', 'POST'])
def search():
    # load the form object with arguments from form.py
    sform = SearchForm_logic()
    
    # check whether the form validation passes all conditions 
    if sform.validate_on_submit():
        # load the the account number/ name /etc from the form class (form.py)
        sholder_name = sform.identifier.data.upper()
        company_name = sform.identifier2.data.upper()
        schoice = sform.criteria.data
        page = request.args.get('page', 1, type = int)
        # load the Shareholder model db method/function by passing form(name/acc_no/etc) agument
        #shareholders = ShareHolder.get_shareholder_by_value(schoice,sholder_name)
        shareholders = HoldersRight.get_holder_by_value(schoice,
                                                        sholder_name,
                                                        company_name)
        if not shareholders:
            # display a not succefull message and return the user back to the Search page
            flash ("ShareHolder Number or Name / company is either wrong or Don't exist")
            return redirect(url_for('search'))
        # display a successful message from validation on the base template
        flash(f'Right info requested for Shareholder: {sform.criteria.data}, Identifier: { sform.identifier.data}, Identifier2: { sform.identifier2.data}')
        # get the equivallent rights details
        # on the assumption that a shareholder to a right (one to one relationship)
        # name=session[shareholders]:
        # right = Right.get_right_by_acno(shareholders.acno)
        # send the Shareholder bio details with his/her Right detail
        # to be displayed / rendered on the result.html page
        return render_template ('result.html', 
                        title='HOME', 
                        shareholders = shareholders, company=company_name
                        )
    # Always return the search page if validation fail
    return render_template('search.html', title='UNCLAIMED', sform = sform)


@app.route('/acceptance', methods=['GET', 'POST'])
def acceptance():
    #if request.method == 'GET'
    #report_list=[]
    if request.method == 'POST':
        acno_list = request.form.getlist('option')
        #for acno in acno_list:
        rholder = HoldersRight.get_shareholder_by_acno(acno_list) #  (session.get('ACNO'))
        #report_list.append(rholder.names)#session['NAMES']=rholder.names
        #  session['DIVIDEND_BATCH']=rholder.bvn #f"{rholder.holdings:,.0f}"
        #  session['COMPANY']=rholder.company #f"{rholder.right_due:,.0f}"
        #  session['ACCOUNT_NUM']= rholder.acno  #f"{rholder.unit_price:,.2f}"
        #  session['AMOUNT']=f"{rholder.amount:,.2f}"
        #rholder
        return render_template('report.html', holders = rholder)

    #request.method =='GET' and session.get('RIGHT_APPLIED'):
    return render_template ('result.html')

@app.route('/convert2pdf', methods=['GET', 'POST'])
def convert2pdf():
    # convert to pdf and clear session
    pass


@app.route('/holders_right/<string:holder>')
def holder_right(holder):
    page = request.args.get('page', 1, type=int)
    rights = HoldersRight.get_holder_by_holder(holder, page)
    return render_template('listing.html', rights = rights , holder = holder)