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
    sform = SearchForm_logic()
    if sform.validate_on_submit():
        sholder_name = sform.identifier.data
        shareholders = ShareHolder.get_shareholder_by_name(sholder_name)
        if not shareholders:
            flash ("Share Holder Number is either wrong or Doesn't exist")
            return redirect(url_for('search'))
        flash('Right info requested for shareholder: {}, Identifier: {}'.format(sform.criteria.data, sform.identifier.data))
        for r in shareholders:
            right = Right.get_right_by_acno(r.acno)
            return render_template ('result.html', title='HOME', shareholders = shareholders, right = right )
    # holders_detail=ShareHolder.get_shareholder_by_acno(request.form['?'])
    return render_template('search.html', title='Find Right',sform = sform)


@app.route('/print', methods=['POST','GET'])
def print():
    if request.method =='GET':
        return redirect(url_for('search'))
    elif request.method =='POST':
        sn=request.form['sn']
        acno =request.form['accountno']
        name =request.form['name']
        unit_held =request.form['unit_held']
        right_due =  request.form['right_due']
        amount = request.form['amount']

        return render_template('ibl_report.html', sn=sn ,acno = acno ,name=name, unit_held=unit_held, \
                        right_due=right_due,amount=amount)
'''
@app.route('/result',methods=['GET', 'POST'])
def consent():
    criteria = ['acno','bvn','chn']
    form_args = request.form['?']
    item = Right(item=form_args)
    if  criteria['acno'] == request.form['?']:
        holders_right=Right.get_right_by(request.form['?']) # when acno is parsed
        return render_template('result.html', holders_detail = holders_right )
   
    elif criteria['bvn'] == request.form['?']:
        holders_right=Right.get_right_by(request.form['?']) # when bvn is parsed
        return render_template('result.html', holders_detail = holders_right )

    elif criteria['chn'] == request.form['?']:
        holders_right=Right.get_right_by(request.form['?']) # when chn is parsed
        return render_template('result.html', holders_detail = holders_right )
    else: 
        return url_for('consent')


'''