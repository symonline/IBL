from flask import render_template, request, redirect, url_for
from app import app
from app.models import Rights, ShareHolder

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    '''
    if request.methods == 'POST':
        account = request.form['account_number']
        print (account.value)
        if account.value == '':
            return render_template('index.htm', message='Please enter required field')
    #if db.session.query(Rights).filter(Rights.id==account).count()==0:

    return render_template('success.html', account = account)
    '''
    accounts = [
        {
        'sn':1,
        'acno':2938475,
        'name': 'Oshoke Louis Cypiran Peter',
        'units': 300,
        'right_due': 25,
        'amount': 150
             },
         ]
    return render_template('result.html', accounts = accounts)

@app.route('/')
def show_account():
    investors = ShareHolder.get_account(int(request.form['account_number']))
    return render_template('show_all.html', investors = investors )

    