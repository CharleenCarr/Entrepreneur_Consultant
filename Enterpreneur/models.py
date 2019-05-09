from datetime import datetime
from base import db

# This class is created for user login account
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    role = db.Column(db.String(25), nullable=False)
    username = db.Column(db.String(15), unique=True, nullable=False)
    email = db.Column(db.String(25), unique=True, nullable=False)
    first_name = db.Column(db.String(25))
    last_name = db.Column(db.String(25))
    phone_type  = db.Column(db.String(15))
    phone_num  = db.Column(db.String(15))
    notes  = db.Column(db.String(225))
    # created_by  = db.Column(db.String(15))
    # created_date  = db.Column(db.DateTime(), nullable=False, default= datetime.today())
    # updated_by  = db.Column(db.String(15))
    # updated_date  = db.Column(db.DateTime(), onupdate=datetime.utcnow)
    # last_login = db.Column(db.DateTime(), default=datetime.utcnow)
    # lockout = db.Column(Boolean, default=0)

    def __init__(self,
                role,
                username,
                email,
                first_name=None,
                last_name=None,
                phone_type=None,
                phone_num=None,
                notes=None
                # created_by=None,
                # created_date=None,
                # updated_by=None,
                # updated_date=None,
                # last_login=None,
                # lockout=None
                ):   
        self.role = role
        self.username = username
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.phone_type = phone_type
        self.phone_num = phone_num
        self.notes = notes
        # self.created_by = created_by
        # self.created_date = created_date
        # self.updated_by = updated_by
        # self.updated_date = updated_date
        # self.last_login = last_login
        # self.lockout = lockout

    def __repr__(self):
        return '<User %r>' % (self.username)

  
# This class is created to store all the colum name in the app
class Meta_Col(db.Model):
    __tablename__ = 'Meta_Columns'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=True)
    category = db.Column(db.String(25))
    sub_cat = db.Column(db.String(15))
    origin_name = db.Column(db.String(50))
    re_name = db.Column(db.String(50))
    desc  = db.Column(db.String(255))
    notes  = db.Column(db.String(225))
#     created_by  = db.Column(db.String(15))
#     created_date  = db.Column(db.DateTime, default=datetime.now().strftime("%m-%d-%Y %I:%M:%S") )
#     updated_by  = db.Column(db.String(15))
#     updated_date  = db.Column(db.DateTime(), onupdate=datetime.now().strftime("%m-%d-%Y %I:%M:%S") )

    def __init__(self, 
                category,
                sub_cat,
                origin_name,
                re_name,
                desc,
                notes
#                 created_by,
#                 created_date,
#                 updated_by,
#                 updated_date
                ):

        self.category = category
        self.sub_cat = sub_cat
        self.origin_name = origin_name
        self.re_name = re_name
        self.desc = desc
        self.notes = notes
#         self.created_by = created_by
#         self.created_date = created_date
#         self.updated_by = updated_by
#         self.updated_date = updated_date
        
    
    def __repr__(self):
        return '<Meta_Col %r>' % (self.re_name)