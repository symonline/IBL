from app import db
from datetime import datetime
# import pdb

class ShareHolder(db.Model):
    item=''
    signal=''
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
    timestamp = db.Column(db.DateTime, default=datetime.utcnow(), index=True )
    rightowned = db.relationship('Right', backref='investor' , lazy='dynamic')

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    
    @classmethod
    # To Help with the search for shareholder specifically by their
    # "registrars account number" (note: "reg_no" is just a search- 
    # argument which should be provided by you(developer) 
    # from either your Form or thereabout )
    def get_shareholder_by_acno(cls, reg_acc_no): # whwre reg_no is an existing shareholder registrars account no
        if reg_acc_no:
            return cls.query.filter_by(acno = reg_acc_no).first()
        else:
            return 0
    
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
    def get_shareholder_by(cls): # search by seti
        if cls.signal == 'chn':
            return cls.query.filter_by(chn = cls.item).first()
        elif cls.signal == 'bvn':
            return cls.query.filter_by(bvn = cls.item).first()
        elif cls.signal == 'acno':
            return cls.query.filter_by(acno = cls.item).first()
    
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
    right_date=db.Column(db.DateTime)
    right_applied=db.Column(db.Integer, nullable=True)
    additional_right_applied= db.Column(db.Integer, nullable=True)
    additional_apply = db.Column(db.Integer, nullable=True)
    additional_price = db.Column(db.Integer, nullable=True)
    balance = db.Column(db.Integer, nullable=True)
    timestamp =db.Column(db.DateTime, default = datetime.utcnow(), index=True)
    

    
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