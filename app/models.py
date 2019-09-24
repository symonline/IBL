from app import db
from datetime import datetime


class Right(db.Model):
    __tablename__='right'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    acno = db.Column(db.Integer, index=True, unique=True)
    right_date=db.Column(db.Integer)
    right_applied=db.Column(db.Integer)
    additional_right_applied= db.Column(db.Integer)
    unit_held = db.Column(db.Integer)
    right_due = db.Column(db.Integer)
    amount = db.Column(db.Float)
    additional_apply = db.Column(db.Integer)
    additional_price = db.Column(db.Integer)
    balance = db.Column(db.Integer)
    company = db.Column(db.String(140))
    
    def __init__(self, acno, right_date, right_applied, additional_right_applied, unit_held, right_due, amount, \
                 additional_apply, additional_price, balance, company ):
        self.id = id
        self.acno = acno
        self.right_date = right_date 
        self.right_applied = right_applied
        self.additional_right_applied = additional_right_applied
        self.unit_held=unit_held
        self.right_due = right_due
        self.amount = amount
        self.additional_apply = additional_apply
        self.additional_price = additional_price
        self.balance = balance
        self.company = company

    
    @classmethod
    def get_account(cls, acc):
        rec=[]
        rec.append(cls.query.filter_by(acno = acc).all())
        return rec

    @classmethod
    def update_right(cls, acc):
        return db.session.remove()
        

    def __repr__(self):
        return 'Share Holder Name: f{self.name}'

class ShareHolder(db.Model):
    __tablename__='share_holder'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True, nullable=True)
    sn = db.Column(db.Integer, unique=True)
    acno = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(64), nullable =True)
    bvn = db.Column(db.Integer, index=True, nullable=True)
    chn = db.Column(db.Integer, index=True, nullable=True)
    agent_member_code = db.Column(db.String(140), nullable=True)
    phone = db.Column(db.Integer, nullable=True)
    email = db.Column(db.String(64), nullable=True)
    cscs_account_no = db.Column(db.Integer, index=True, nullable=True)
    address=db.Column(db.String(300), nullable=True)

    
    #def __init__(self, *args ,**kwargs):
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)
    ''' sn, acno, name, email, cscs_account_no, 
        bvn, chn, agent_member_code, phone, address):
        self.sn = kwargs[sn]
        self.acno = kwargs[acno]
        self.name = kwargs[name]
        self.email =  kwargs[email] 
        self.cscs_account_no = kwargs[cscs_account_no] 
        self.bvn = kwargs[bvn]
        self.chn = chn
        self.agent_member_code = agent_member_code
        self.phone = phone
        self.address = address 
    '''

    @classmethod
    def get_shareholder(cls, value):
        rec=[]
        rec.append(cls.query.filter_by(acno = value).all())
        return rec
    @classmethod
    def get_shareholder(cls, value):
        return cls.query.filter_by(acno = value).all()

    @classmethod
    def find_by_any(cls):
        if cls.signal == 'chn':
            return cls.query.filter_by(chn = cls.item).first()
        elif cls.signal == 'bvn':
            return cls.query.filter_by(bvn = cls.item).first()
        elif cls.signal == 'acno':
            return cls.query.filter_by(acno = cls.item).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update_shareholder(self, obj, value):
        # obj=cls.query.filter_by(bvn=bvn_value).first()
        obj.amount = value

    def __repr__(self):
        return f'SN:{self.sn} ACCOUNT: {self.acno} Nmes:{self.name}'


class Investor(db.Model):
    signal = ''
    item = ''

    __tablename__='investor'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    sn = db.Column(db.Integer, unique=True)
    acno = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(64), nullable =True)
    
    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)

    @classmethod
    def get_shareholder(cls, value):
        return cls.query.filter_by(acno = value).all()

    @classmethod
    def find_by_any(cls):
        if cls.signal == 'chn':
            return cls.query.filter_by(chn = cls.item).first()
        elif cls.signal == 'bvn':
            return cls.query.filter_by(bvn = cls.item).first()
        elif cls.signal == 'acno':
            return cls.query.filter_by(acno = cls.item).first()

    @classmethod
    def find_all(cls):
        return cls.query.all()

    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()

    def update_shareholder(self, obj, value):
        # obj=cls.query.filter_by(bvn=bvn_value).first()
        obj.amount = value

    def __repr__(self):
        return f'[self.acno, self.name]'