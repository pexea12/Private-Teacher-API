from flask_wtf import Form
from wtforms import StringField, PasswordField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, Optional

class UserForm(Form):
	name = StringField('name', validators=[
		Length(max=80, message='max name length is 80 characters'),
		DataRequired(message='name is required')
	])
	email = StringField('email', [
		DataRequired(message='email is required'), 
		Email(message='email must be valid')
	])
	phone = StringField('phone', [
		Length(max=30, message='max phone length is 30 characters'),
		DataRequired(message='phone is required')
	])
	password = PasswordField('password', [
		DataRequired(message='password is required'),
		EqualTo('confirm', message='passwords must match')
	])
	confirm = PasswordField('confirm')
	image = StringField('image', [ Length(max=120) ])
	priviledge = StringField('priviledge', [
		DataRequired(message='priviledge is required')
	])
	
class UserUpdateForm(Form):
	name = StringField('name', validators=[
		Length(max=80, message='max name length is 80 characters'),
		Optional()
	])
	email = StringField('email', [
		Email(message='email must be valid'),
		Optional()
	])
	phone = StringField('phone', [
		Length(max=30, message='max phone length is 30 characters'),
		Optional()
	])
	image = StringField('image', [ 
		Length(max=120),
		Optional()
	])
	priviledge = StringField('priviledge', [ Optional() ])