import pandas as pd


csvfile='/home/symonline/projects/ibl-rights/app/static/export.csv'

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
     holder = HoldersRight(id = int(row['ID']), names = row['NAME'], acno = int(row['ACCOUNT_NUMBER']), \
     fname = row['FIRST_NAME'], oname = row['OTHER_NAME'], lname = row['LAST_NAME'],address = row['ADDRESS'],\
     holdings = int(row['TOTAL_HOLDING']), right_due=int(row['RIGHTS_DUE']), unit_price = float(row['UNIT_PRICE']),amount = float(row['RIGHT_AMOUNT']))