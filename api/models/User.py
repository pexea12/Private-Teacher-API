from . import db
import bcrypt

class User(db.Model):
	__tablename__ = 'users'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), unique=True, nullable=False)
	password = db.Column(db.String(120), nullable=False)
	phone = db.Column(db.String(30), nullable=False)
	image = db.Column(db.String(120))
	priviledge = db.Column(db.String(10), nullable=False)
	
	def __init__(self, name, email, password, phone, priviledge, image=''):
		self.name = name
		self.email = email
		self.password = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
		self.phone = phone
		self.priviledge = priviledge
		self.image = image if image != '' else '/static/default.jpg'
		
	def __repr__(self):
		return '<User %r>' % self.name