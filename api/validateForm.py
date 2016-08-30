from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField, TextField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class UserForm(Form):
	name = StringField('name', validators=[
		Length(max=80),
		DataRequired()
	])
	email = StringField('email', [
		DataRequired(), 
		Email()
	])
	phone = StringField('phone', [
		Length(max=30),
		DataRequired()
	])
	password = PasswordField('password', [
		DataRequired(),
		EqualTo('confirm', 'Password must match')
	])
	confirm = PasswordField('confirm')
	image = StringField('image', [ Length(max=120) ])
	priviledge = StringField('priviledge')
	
class UserUpdateForm(Form):
	name = StringField('name', validators=[
		Length(max=80),
		Optional()
	])
	password = PasswordField('password', [
		DataRequired(),
		EqualTo('confirm', 'Password must match')
	])
	confirm = PasswordField('confirm')
	email = StringField('email', [
		Email(),
		Optional()
	])
	phone = StringField('phone', [
		Length(max=30),
		Optional()
	])
	image = StringField('image', [ 
		Length(max=120),
		Optional()
	])
	priviledge = StringField('priviledge', [ Optional() ])
	
class StudentForm(Form):
	name = StringField('name', [
		DataRequired(),
		Length(max=80)
	])
	email = StringField('email', [
		DataRequired(),
		Length(max=120)
	])
	phone = StringField('phone', [
		DataRequired(),
		Length(max=30)
	])
	description = TextField('description')
	price_per_hour = IntegerField('price_per_hour')
	school = TextField('school')
	level = TextField('level')
	image = StringField('image', [
		Length(max=120)
	])
	location = TextField('location')
	subjects = TextField('subjects')
	
class StudentUpdateForm(Form):
	name = StringField('name', [
		Optional(),
		Length(max=80)
	])
	email = StringField('email', [
		Optional(),
		Length(max=120)
	])
	phone = StringField('phone', [
		Optional(),
		Length(max=30)
	])
	description = TextField('description')
	price_per_hour = IntegerField('price_per_hour')
	school = TextField('school')
	level = TextField('level')
	image = StringField('image', [
		Length(max=120)
	])
	location = TextField('location')
	subjects = TextField('subjects')

class TeacherForm(Form):
	name = StringField('name', [
		DataRequired(),
		Length(max=80)
	])
	email = StringField('email', [
		DataRequired(),
		Length(max=120)
	])
	phone = StringField('phone', [
		DataRequired(),
		Length(max=30)
	])
	description = TextField('description')
	salary_per_hour = IntegerField('salary_per_hour')
	job = TextField('school')
	work_place = TextField('work_place')
	level_to_teach = TextField('level')
	image = StringField('image', [
		Length(max=120)
	])
	location = TextField('location')
	subjects = TextField('subjects')
	
class TeacherUpdateForm(Form):
	name = StringField('name', [
		Optional(),
		Length(max=80)
	])
	email = StringField('email', [
		Optional(),
		Length(max=120)
	])
	phone = StringField('phone', [
		Optional(),
		Length(max=30)
	])
	description = TextField('description')
	salary = IntegerField('salary_per_hour')
	job = TextField('school')
	work_place = TextField('work_place')
	level_to_teach = TextField('level')
	image = StringField('image', [
		Optional(),
		Length(max=120)
	])
	location = TextField('location')
	subjects = TextField('subjects')
	
class LoginForm(Form):
	email = StringField('email', [
		DataRequired(), 
		Email()
	])
	password = PasswordField('password', [ DataRequired() ])