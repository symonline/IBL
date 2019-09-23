from app import db


class Rights(db.Model):
    __tablename__='ibl-rights'
    id = db.Column(db.Integer, primary_key=True, index=True, unique=True)
    sn = db.Column(db.Integer, unique=True)
    acno = db.Column(db.Integer, index=True, unique=True)
    name = db.Column(db.String(140))
    bvn = db.Column(db.Integer, index=True, unique=True)
    chn = db.Column(db.Integer, index=True, unique=True)
    right_date=
    right_applied=
    
    unit_held = db.Column(db.Integer)
    right_due = db.Column(db.Integer)
    amount = db.Column(db.Float)
    additional_apply = db.Column(db.Integer)
    additional_price = db.Column(db.Integer)
    balance = db.Column(db.Integer, unique=True)
    
    def __init__(self, sn, acno, name, unit_held, right_due,amount):
        self.sn = sn
        self.acno = acno
        self.name = name 
        self.unit_held = unit_held 
        self.right_due = right_due
        self.amount = amount
    
    @classmethod
    def get_account(cls, acc):
        rec=[]
        rec.append(cls.query.filter_by(acno = acc).all())
        return rec

    def __str__(self):
        return 'f{self.sn} ,f{self.acno}, f{self.name}'


