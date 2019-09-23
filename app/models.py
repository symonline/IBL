from app import db


class Rights(db.Model):
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
        db.session.remove()
        return rec

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
    
    def __init__(self, sn, acno, name, email, cscs_account_no, \
                bvn, chn, agent_member_code, phone, address):
        self.id = id
        self.sn = sn
        self.acno = acno
        self.name = name
        self.email = email
        self.cscs_account_no = cscs_account_no
        self.bvn = bvn
        self.chn = chn
        self.agent_member_code = agent_member_code
        self.phone = phone
        self.address = address 

    @classmethod
    def get_shareholder(cls, value):
        rec=[]
        rec.append(cls.query.filter_by(acno = acc).all())
        return rec
    

    def __str__(self):
        return 'f{self.sn} ,f{self.acno}, f{self.name}'


class Investor(db.Model):
    __tablename__='investor'

    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    sn = db.Column(db.Integer, unique=True)
    acno = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(64), nullable =True)
    
    
    def __init__(self, sn, acno, name):
        self.id = id
        self.sn = sn
        self.acno = acno
        self.name = name
        

    @classmethod
    def get_shareholder(cls, value):
        rec=[]
        rec.append(cls.query.filter_by(acno = value).all())
        return rec
    

    def __str__(self):
        return 'Details(Account=%s, Name=%s)' % (self.acno, self.name)