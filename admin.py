# import pandas as pd



csvfile='/home/symonline/projects/ibl-rights/app/static/export.csv'
'''
df = pd.read_csv(csvfile, \
    index_col='ACCOUNT_NUMBER', \
    header = 0, \
    names = ['ID','NAME','ACCOUNT_NUMBER','FIRST_NAME','OTHER NAME','LAST_NAME','ADDRESS','TOTAL HOLDING', 'RIGHTS_DUE' , 'UNIT_PRICE','COMP' , 'BVN' ,'CHN','PHONE' ,'EMAIL' ,'CSCS_NO','AMOUNT'])


for holder in df:
    holder = HoldersRight(id=holder['ID'],names=holder['NAME'],acno=holder['ACCOUNT_NUMBER'],\
    fname=holder['FIRST_NAME'],oname=holder['OTHER NAME'],lname=holder['LAST_NAME'],\
    address=holder['ADDRESS'],holdings=holder['TOTAL HOLDING'],right_due=holder['RIGHTS_DUE'],\
    unit_price=holder['UNIT_PRICE'],amount=holder['AMOUNT'])

    db.session.add(holder)
    db.session.commit()
'''
'''
# purge all data from holders_right table
def purge_table_data(obj, table_obj):
    holders = obj.query.all()
    for holder in holders:
       table_obj.session.delete(holder)
       table_obj.session.commit()
    return "Table purging complete"

import csv
csvfile='/home/symonline/projects/ibl-rights/app/static/export.csv'
df=csv.DictReader(open(csvfile))
val=None
#
for row in df:
     holder = HoldersRight(id = row['ID'], names = row['NAME'], acno = ['ACCOUNT_NUMBER'], \
     fname = row['FIRST_NAME'], oname = row['OTHER_NAME'], lname = row['LAST_NAME'],address = row['ADDRESS'],\
     holdings = row['TOTAL_HOLDING'], right_due=row['RIGHTS_DUE'], unit_price = float(row['UNIT_PRICE']),amount = float(row['RIGHT_AMOUNT']))
'''

def amend(obj,db,list):
    for account in list:
        h=obj.get_shareholder_by_acno(account)
        if h.acno==1706:
            h.names='JEGEDE TIAMIYU TESTER1'
            h.fname='TEST1'
            db.session.commit()
        elif h.acno==1728:
            h.names='OJEI TEST4'
            h.fname='TEST4'
            db.session.commit()
        else:
            h.names='UZOUKWU TEST5'
            h.fname='TEST5'
            db.session.commit()

def remove_account(obj,db,search_list): # as in add_account(HoldersRight, db, list1)
    deleted_account=[]
    for account in search_list:
        holder = obj.get_shareholder_by_acno(account) # assuming account number is unique
        if holder:
            db.session.delete(holder)
            db.session.commit()
            deleted_account.append(account)
        else:
            print(f'Account:{account} - Dont Exist in the Database')
            continue
    print('List of account deleted below:-')
    print(deleted_account)

def add_account(obj, db, new_list): # as in add_account(HoldersRight, db, list2)
    deleted_account=[]
    added_account=[]
    for account in new_list:
        holder_account = obj.get_shareholder_by_acno(account[1])
        if holder_account is True:
            print(f'Account: {account} already exist - SKIPPED - - -')
            continue
        else:
            investor = obj(names = account[0], \
                       acno =int(account[1]), \
                       holdings = int(account[2]), \
                       right_due = int(account[3]),\
                       unit_price = float(account[4]),\
                       amount = float(account[5]) \
                            )
            db.session.add(investor)
            db.session.commit()
            print(f'{account[1]}:YES')  # mock
            added_account.append(account[1])
    print('List of newly added investors ...')
    print(added_account)
        
