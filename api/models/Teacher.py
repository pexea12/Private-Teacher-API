from . import db
from geopy.geocoders import GoogleV3
from flask_login import current_user

geolocator = GoogleV3(timeout=5)

class Teacher(db.Model):
	__tablename__ = 'teachers'
	
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(80), nullable=False)
	email = db.Column(db.String(120), nullable=False)
	phone = db.Column(db.String(30), nullable=False)
	description = db.Column(db.Text)
	salary_per_hour = db.Column(db.Integer)
	job = db.Column(db.Text)
	work_place = db.Column(db.Text)
	level_to_teach = db.Column(db.Text)
	image = db.Column(db.String(120))
	location = db.Column(db.Text)
	location_lon = db.Column(db.String(30), nullable=False)
	location_lat = db.Column(db.String(30), nullable=False)
	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
	rating = db.Column(db.Float, default=0.0)
	rating_number = db.Column(db.Integer, default=0)
	subjects = db.Column(db.Text)
	
	def __init__(self, name, email, phone, description, salary_per_hour, job, work_place, level_to_teach, location, subjects, image=''):
		self.name = name
		self.email = email
		self.phone = phone
		self.description = description
		self.salary_per_hour = salary_per_hour
		self.job = job
		self.work_place = work_place
		self.level_to_teach = level_to_teach
		self.image = image if image != '' else '/static/default.jpg'
		self.user_id = current_user.id;
		
		location = geolocator.geocode(location)
		
		self.location = location.address
		self.location_lon = location.longitude
		self.location_lat = location.latitude
		
		self.subjects = subjects
		
	def __repr__(self):
		return '<Teacher %r>' % self.name