from api import app, User, db
from flask import render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, current_user, login_required
import requests
import bcrypt

base_url = 'http://localhost:5000'

def errorsToList(form):
	errors = []
	for error in form.errors.values():
		errors.extend([e for e in error])
		
	return errors
	

from api.validateForm import LoginForm
@app.route('/', methods=['GET', 'POST'])
def home():
	if request.method == 'GET':
		return render_template('home.html', current_user=current_user)
	
	if request.method == 'POST':
		if current_user.is_authenticated:
			return redirect(url_for('home'))
		
		form = LoginForm(request.form)

		if form.validate_on_submit():
			print('Hello World')
			email = form.data['email']
			password = form.data['password']
	
			user = User.query.filter_by(email=email).first()
	
			if user is None:
				flash([u'Không tìm thấy email'], 'errors')
				return redirect(url_for('home'))
		
			if not bcrypt.checkpw(password.encode(), user.password):
				flash([u'Password không đúng! Mời bạn đăng nhập lại'], 'errors')
				return redirect(url_for('home'))
		
			login_user(user)
			
			flash([u'Đăng nhập thành công!'], 'info')
			return redirect(url_for('home'))

		flash([u'Vui lòng nhập lại thông tin đăng nhập'], 'errors')
		return redirect(url_for('home'))
		

from api.validateForm import UserForm
@app.route('/register', methods=['GET', 'POST'])
def register():
	if current_user.is_authenticated and not current_user.is_admin():
		return redirect(url_for('home'))
	
	if request.method == 'GET':
		return render_template('register.html', current_user=current_user)
		
	if request.method == 'POST':
		form = UserForm(request.form)
		
		values = form.data
		del(values['confirm'])
	
		if form.validate_on_submit():
			
			newUser = User(**values)
			
			try:
				db.session.add(newUser)
				db.session.commit()
			except:
				flash([u'Email đã được đăng ký'], 'errors')
				flash(values, 'fields')
				return redirect(url_for('register'))
			
			flash([u'Đăng ký thành công. Đăng nhập để tiếp tục'], 'info')
			return redirect(url_for('home'))
		
		flash(values, 'fields')
			
		flash(errorsToList(form), 'errors')
		
		return redirect(url_for('register'))

@app.route('/profile')
@login_required
def profile():
    return render_template('profile.html')
	
@app.route('/profile/edit')
@login_required
def profile_edit():
	return render_template('profile_edit.html')
	
@app.route('/logout')
@login_required
def profile_logout():
	logout_user()
	flash(['Đăng xuất thành công!'], 'info')
	return redirect(url_for('home'))
	
@app.route('/profile/teachers')
@login_required
def profile_teachers():
	return render_template('profile_teachers.html')
	
@app.route('/profile/students')
@login_required
def profile_students():
	return render_template('profile_students.html')	

