from flask import render_template, request, redirect, url_for, flash
from app import app, db
# from flask_login import login_user
from app.models import ShareHolder, Right
from app.forms import SearchForm_logic, ConsentForm_logic

@app.route('/')
@app.route('/index')
def index():
    info='WELCOME TO THE IBL RIGHT OFFER TEST PAGE'
    
    return render_template('index.html', title='HOME', info = info)
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
        account_number=sform.identifier.data
        sharehohlder = ShareHolder.get_shareholder_by_acno(account_number)
        if sharehohlder is None:
            flash ("Share Holder Number is either wrong of Don't exist")
            return redirect(url_for('search'))
        flash('Right info requested for shareholder: {}, Identifier: {}'.format(sform.criteria.data, sform.identifier.data))
        right=Right
        return render_template('index.html', title='HOME', sharehohlder = sharehohlder)
    # holders_detail=ShareHolder.get_shareholder_by_acno(request.form['?'])
    return render_template('search.html', title='Find Right',sform = sform)

'''
@app.route('/result',methods=['GET', 'POST'])
def result():
    holders_detail=ShareHolder.get_shareholder_by_acno(request.form['?'])
    return render_template('index.html', holders_detail = holders_detail)

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