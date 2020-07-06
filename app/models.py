from app import db
from datetime import datetime
import itertools
import operator
from functools import reduce
# import pdb

class ShareHolder(db.Model):
    item=''
    signal=''
    criteria='' 
    value=''
    __deleted_share_holders__=[]
    __updated_share_holders__=[]
    __created_share_holders__=[]

    __tablename__='share_holder'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    sn = db.Column(db.Integer, unique=True, nullable=True)
    acno = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(300), nullable = False)
    bvn = db.Column(db.Integer, index=True, nullable=True)
    chn = db.Column(db.Integer, index=True, nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(64), nullable=True)
    cscs_account_no = db.Column(db.Integer, index=True, nullable=True)
    address = db.Column(db.String(300), nullable=True)
    agent_member_code = db.Column(db.String(20), nullable=True)
    timestamp = db.Column(db.String(20), default=datetime.utcnow(), index=True, nullable=True )
    rightowned = db.relationship('Right', backref='investor' , lazy='dynamic')

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    @classmethod
    # To Help with the search for shareholder specifically by their
    # "registrars account number" (note: "reg_no" is just a search- 
    # argument which should be provided by you(developer) 
    # from either your Form or thereabout )
    def get_shareholder_by_name(cls, sname): # whwre reg_no is an existing shareholder registrars account no
        if sname:
            #return cls.query.filter_by(name = sname).all()
            
            return cls.query.filter(cls.name.like( sname )).first()

    @classmethod
    # To Help with the search for shareholder specifically by their
    # "registrars account number" (note: "reg_no" is just a search- 
    # argument which should be provided by you(developer) 
    # from either your Form or thereabout )
    def get_shareholder_by_acno(cls, ac_no): # whwre reg_no is an existing shareholder registrars account no
        if ac_no:
            return cls.query.filter_by(acno = ac_no).first()
            # return cls.query.filter(cls.name.like("%" + value + "%")).all()
    
    @classmethod
    def get_shareholder_by_value(cls, choice, value): # whwre reg_no is an existing shareholder registrars account no
        if value :
            if choice=='name':
                return cls.query.filter_by(name = value).first()
            elif choice=='acno':
                return cls.query.filter_by(acno = value).first()
            elif choice=='sn':
                return cls.query.filter_by(sn = value).first()
            else:
                return False
            # return cls.query.filter(cls.name.like("%" + value + "%")).all()
    
    @classmethod
    def get_shareholder_by_name_(cls, value): # whwre reg_no is an existing shareholder registrars account no
        if value :
            first_name = cls.query.filter(cls.first.like("%" + value + "%")).all()
            if first_name :
                return first_name
            second_name = cls.query.filter(cls.second.like("%" + value + "%")).all()
            if second_name:
                return second_name
            other_name = cls.query.filter(cls.other.like("%" + value + "%")).all()
            if  other_name:
                return  other_name
            # return cls.query.filter(cls.name.like("%" + value + "%")).all()

    @classmethod
    def right_info(cls, reg_acc_no):# this should return a list of right owned by this account
        u=cls.get_shareholder_by_acno(reg_acc_no)
        return u.rightowned

    @classmethod
    def create_new(cls,reg_acc_no, obj=0): # Where obj is a ShareHolder and reg_acc_no is shareholder registrars account no
        if not obj : # Ensure SHAREHOLDER Object/obj and Registrars account no don't exist before creation(integrity)
            if  reg_acc_no is False: 
                db.session.add(obj)
                db.session.commit()
                cls.__created_share_holders__.append(obj) # Add newly created SHAREHOLDER to Global variable
                return True
            else:
                return False
        else:
            return False
        
    
    @classmethod
    # Help to retrieve all shareholder's record
    def get_all_shareholder(cls):
        return cls.query.all()

    #(To be used to create new Share Holder's record
    # in our database
    # Note: an instance object must be created first in your function
    # before calling this method e.g investor = ShareHolder(sn="?", acno="?",name="?")
    # befor calling investor.save_shareholder())
    def save_shareholder(self):
        db.session.add(self)
        db.session.commit()

    #(To be used to delete existing Share Holder's record
    # in our database
    # Note: an instance object must be created first in your function
    # before calling this method e.g holder = ShareHolder.get_shareholder_by_acno(reg_no=324)
    # befor calling investor.delete_shareholder(holder))
    @classmethod
    def delete_shareholder(cls, obj): # Where obj is a ShareHolder
        if obj: 
            cls.__deleted_share_holders__.append(obj)
            db.session.delete(obj)
            db.session.commit()
            return True
        else:
            return False

    '''
    @classmethod
    def update_shareholder(cls, obj, value):
        # obj=cls.query.filter_by(chn=value).first()
        if obj:
            cls.__updated_share_holders__.append(obj)
            obj.amount = value
            db.session.commit()
            return True
        else:
            return False
    '''

    def update_shareholder(self,value): # parse in argument from your form via view-function
        if value:
            self.holder = value
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def clear_data(cls):
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print ('Clear table %s' % table)
            db.session.execute(table.delete())
        db.session.commit() 

    def __repr__(self):
        return f'<SN:{self.sn} ACCOUNT: {self.acno} Nmes:{self.name}>'


class Right(db.Model):

    item = ''
    signal = ''
    __deleted_right__ = []
    __updated_right__ = []
    __created_right__ = []

    __tablename__='right'


    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    acno = db.Column(db.Integer, index=True, unique=True)
    unit_held = db.Column(db.Integer, nullable=True)
    right_due = db.Column(db.Integer, nullable=True)
    holder= db.Column(db.Integer, db.ForeignKey('share_holder.id'))
    amount = db.Column(db.Float(), nullable=True)
    company = db.Column(db.String(140), nullable=True)
    right_date = db.Column(db.String(14))
    right_applied = db.Column(db.Integer, nullable=True)
    additional_right_applied = db.Column(db.Integer, nullable=True)
    additional_apply = db.Column(db.Integer, nullable=True)
    additional_price = db.Column(db.Integer, nullable=True)
    balance = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.String(20), default = datetime.utcnow(), index=True)
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
   
    @classmethod
    def get_right_by_acno(cls, reg_acc_no): # where reg_acc_no is an existing shareholder registrars account no
        if reg_acc_no :
            return cls.query.filter_by(acno = reg_acc_no).first()
        else:
            return 0

    @classmethod
    def get_all_right(cls, value):
        return cls.query.filter_by(acno = value).all()
 
    def update_additional_right(self,value): # parse in argument from your form via view-function
        if value:
            self.additional_apply = value
            db.session.commit()
            return True
        else:
            return False

    def update_right_applied(self,value): # parse in argument from your form via view-function
        if value:
            self.right_applied = value
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def update_right_r(cls, obj, value):
        # obj=cls.query.filter_by(chn=value).first()
        if obj:
            cls.__updated_share_holders__.append(obj)
            obj.additional_apply = value
            db.session.commit()
            return True
        else:
            return False

    @classmethod
    def get_right_by(cls):
        if cls.signal == 'chn':
            return cls.query.filter_by(chn = cls.item).all()
        elif cls.signal == 'bvn':
            return cls.query.filter_by(bvn = cls.item).all()
        elif cls.signal == 'acno':
            return cls.query.filter_by(acno = cls.item).all()

   
    @classmethod
    def get_all_right(cls):
        return cls.query.all()

    def save_right(self):
        db.session.add(self)
        db.session.commit()

    def delete_right(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def __clear_data__(cls):
        meta = db.metadata
        for table in reversed(meta.sorted_tables):
            print ('Clear table %s' % table)
            db.session.execute(table.delete())
        db.session.commit()
        
    def __repr__(self):
        return f'<Share Holder Name: {self.name}>'

class SearchOption(db.Model):

    __tablename__='search_option'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    code = db.Column(db.String(7), index=True, unique=False)
    display_name = db.Column(db.String(15), index=True, nullable=False)

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def add_new(cls):
        pass

    def remove_existing(cls):
        pass
    
    def update_existing(cls):
        pass 

    def __repr__(self):
        return f'<Search_Option Code: {self.code}, Search_Option Display Name: {self.name}>'

class HoldersRight(db.Model):

    item = ''
    signal = ''
    __deleted_right__ = []
    __updated_right__ = []
    __created_right__ = []

    __tablename__='holders_right'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    names = db.Column(db.String(500), nullable = True)
    acno = db.Column(db.Integer, index=True, nullable = False)
    fname = db.Column(db.String(150), nullable = True,index=True)
    oname = db.Column(db.String(150), nullable = True,index=True)
    lname = db.Column(db.String(150), nullable = True,index=True)
    address = db.Column(db.String(700), nullable = True)
    holdings = db.Column(db.Integer, nullable=True)
    right_due = db.Column(db.Integer, nullable=True)
    unit_price = db.Column(db.Float(), nullable=True)
    company = db.Column(db.String(140), nullable=True)
    bvn = db.Column(db.Integer, index=True, nullable=True)
    chn = db.Column(db.Integer, index=True, nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(64), nullable=True)
    cscs_account_no = db.Column(db.Integer, index=True, nullable=True)
    amount = db.Column(db.Float(), nullable=True)
    '''
    right_date = db.Column(db.String(14))
    right_applied = db.Column(db.Integer, nullable=True)
    additional_right_applied = db.Column(db.Integer, nullable=True)
    additional_apply = db.Column(db.Integer, nullable=True)
    additional_price = db.Column(db.Integer, nullable=True)
    balance = db.Column(db.Integer, nullable=True)
    timestamp = db.Column(db.String(20), default = datetime.utcnow(), index=True)
    '''
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def get_shareholder_by_acno(cls, account_number_list): # where reg_no is an existing shareholder registrars account no
        if account_number_list:
            share_holders = cls.query.filter(cls.acno.in_(account_number_list)).all()
            #acc = cls.query.filter_by(acno = account).all()#.first()
        return share_holders

    @classmethod
    def get_holder_by_value(cls, choice, value, company): # where reg_no is an existing shareholder registrars account no
        # all_acno=[]
        if choice =='name'.lstrip():# and len(value)>2 :
            val = value.split()
            all_names = list(itertools.chain([], []))
            select_names = list(itertools.chain([], []))
            # return cls.query.filter(cls.fname.like("%" + value + "%")).all()
            #for name in val: 
            #fn = cls.query.filter_by(fname = name).all()# paginate(page=pages, per_page=10)
            fn = cls.query.filter(cls.names.like("%"+ value +"%")).filter(cls.company==company).order_by(cls.names).all()
            #fn = fn.query.filter(cls.company=company)
            #on = cls.query.filter(cls.oname.like("%"+ name + "%")).all()
            #ln = cls.query.filter_by(lname = name).all()# paginate(page=pages, per_page=10)
            #ln = cls.query.filter(cls.lname.like("%"+ name + "%")).all()
            
            #all_names.append(list(itertools.chain(fn, on, ln)))
            all_names.append(list(itertools.chain(fn)))
            #all_names.append(all_names)
            my_list = list(set(reduce(operator.iconcat,all_names)))
                
            return my_list

        #if isinstance((int(value)),int) and len(value)>2:
        return (cls.query.filter_by(acno = value).filter(cls.company==company).all())
        # return all_acno
    
    @classmethod
    def get_holder_by_holder(cls, value, pages): # where reg_no is an existing shareholder registrars account no
        # return cls.query.filter(cls.fname.like("%" + value + "%")).all()
        fn = cls.query.filter(cls.fname.like("%" + value + "%")).paginate(page=pages, per_page=10)
        if fn:
            return fn
        on = cls.query.filter(cls.oname.like("%" + value + "%")).paginate(page=pages, per_page=10)
        if on:
            return on
        ln = cls.query.filter(cls.lname.like("%" + value + "%")).paginate(page=pages, per_page=10)
        if ln:
            return ln
            # return cls.query.filter(cls.name.like("%" + value + "%")).all()

class Company(db.Model):
    
    item = ''
    signal = ''
    __deleted_right__ = []

    __tablename__='companies'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    company = db.Column(db.String(150), nullable = True)
    share_holder = db.Column(db.String(150), nullable = True,index=True)
    dividend = db.Column(db.String(150), nullable = True,index=True)

    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

class Dividend(db.Model):
    
    item = ''
    signal = ''
    __deleted_right__ = []
    __updated_right__ = []
    __created_right__ = []

    __tablename__='dividends'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    acno = db.Column(db.Integer, index=True)
    company = db.Column(db.String(200), nullable = True,index=True)
    pay_no = db.Column(db.String(20), nullable=True)
    net_amount = db.Column(db.Float, nullable =False)
    name = db.Column(db.String(500), nullable=False)
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

            # return cls.query.filter(cls.name.like("%" + value + "%")).all()