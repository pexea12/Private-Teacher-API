from . import db
from geopy.geocoders import GoogleV3
from flask_login import current_user

geolocator = GoogleV3(timeout=5)

class Student(db.Model):
	__tablename__ = 'students'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	phone = db.Column(db.String(30), nullable=False)
	description = db.Column(db.Text)
	price_per_hour = db.Column(db.Integer)
	school = db.Column(db.Text)
	level = db.Column(db.Text)
	image = db.Column(db.String(120))
	location = db.Column(db.Text)
	location_lon = db.Column(db.String(30), nullable=False)
	location_lat = db.Column(db.String(30), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	
	subjects = db.Column(db.Text)
	
	def __init__(self, name, email, phone, description, price_per_hour, school, level, user_id, location, subjects, image=''):
		self.name = name
		self.email = email
		self.phone = phone
		self.description = description
		self.price_per_hour = price_per_hour
		self.school = school
		self.level = level
		self.user_id = current_user.id
		self.image = image if image != '' else '/static/default.jpg'
		
		location = geolocator.geocode(location)
		
		self.location = location.address
		self.location_lon = location.longitude
		self.location_lat = location.latitude
		
		self.subjects = subjects
		
	def __repr__(self):
		return '<Student %r>' % self.name