''' Create sample data '''

from api import db, User

db.create_all()

db.session.add(User(
	'Magnus Carlsen',
	'carlsen@gmail.com',
	'carlsen',
	'1234',
	'Admin'
))

db.session.add(User(
	'Veselin Topalov',
	'topalov@gmail.com',
	'topalov',
	'10001',
	'Member'
))

db.session.add(User(
	'Levon Aronian',
	'aronian@gmail.com',
	'aronian',
	'12345',
	'Admin'
))

db.session.add(User(
	'Vladimir Kramnik',
	'kramnik@gmail.com',
	'kramnik',
	'123456',
	'Member'
))

db.session.add(User(
	'Anish Giri',
	'giri@gmail.com',
	'giri',
	'1234567',
	'Member'
))

db.session.commit()