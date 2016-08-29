from api import app, db, login_manager, User
from flask import jsonify, request
import bcrypt
from flask_login import login_user, logout_user, current_user, login_required
from flask_login import AnonymousUserMixin as Anonymous

# Helper function
def selectParams():
	''' Select necessary params from request.args '''
	params = {}
	list = ['id', 'name', 'image', 'phone', 'email', 'priviledge']
	
	for name in list:
		if name in request.args:
			params[name] = request.args[name]
	return params


@app.route('/api/get_id')
def getid():
	return jsonify({'id':current_user.id})


@login_manager.user_loader
def load_user(id):
	return User.query.get(id)
	
from .validateForm import LoginForm

# /api/login/
@app.route('/api/login', methods=['POST'])
def login():
	if current_user.is_authenticated:
		return jsonify({ "msg": "you have already logged in" })
		
	form = LoginForm(request.form)

	if form.validate_on_submit():
		email = form.data['email']
		password = form.data['password']
		
		user = User.query.filter_by(email=email).first()
		
		if user is None:
			return jsonify({ "msg": "user not found" })
			
		if not bcrypt.checkpw(password.encode(), user.password):
			return jsonify({ "msg": "password not matched" })
			
		login_user(user)
		return jsonify({
			"msg": "login successfully",
			"email": user.email,
			"name": user.name,
			"url": "/api/users?id=" + str(user.id)
		})
	
	return jsonify({
		"msg": "login failed"
	});

# /api/logout
@app.route('/api/logout', methods=['GET'])
@login_required
def logout():
	logout_user()
	return jsonify({ "msg": "logout successfully" })
	
# /api/users/
@app.route('/api/users', methods=['GET'])
@login_required
def get_users():
	if not current_user.is_admin():
		return jsonify({ "msg": "member is not allowed to access" })
		
	# Take the params
	limit = request.args.get('limit', 20)
	
	params = selectParams()
	
	select = (
		User.id,
		User.name,
		User.image,
		User.phone,
		User.email,
		User.priviledge
	)
	
	users = User.query.filter_by(**params).with_entities(*select)
	
	if limit is not None:
		users = users.limit(limit)
		
	users = users.all()

	if users is None or len(users) == 0:
		return jsonify({ "msg": "No user found" })
	
	results = []
	for user in users:
		result = {}
		
		result['id'] = user[0]
		result['name'] = user[1]
		result['image'] = user[2]
		result['phone'] = user[3]
		result['email'] = user[4]
		result['priviledge'] = user[5]
		
		results.append(result)
		
	return jsonify(results)

# /api/users/<int:user_id>
@app.route('/api/users/<int:user_id>', methods=['GET'])
@login_required
def get_user_by_id(user_id):
	if not current_user.is_admin() and current_user.id != user_id:
		return jsonify({ "msg": "you are not allowed to access" })
		
	user = User.query.get(user_id)
	result = user.__dict__
	
	del result['_sa_instance_state']
	del result['password']
	
	return jsonify(result)

from .validateForm import UserForm
import bcrypt, urllib
	
# /api/users/add/
@app.route('/api/users/add', methods=['GET', 'POST'])
def post_users():
	if request.method == 'GET':
		return jsonify({ 'msg': 'This URL is only for POST request' })
	
	if not isinstance(current_user, Anonymous) and not current_user.is_admin():
		return jsonify({ "msg": "You are not allowed to add user" })
		
	# Process with POST data sent from HTML form
	form = UserForm(request.form)
	
	if form.validate_on_submit():
		name = form.name.data
		email = form.email.data
		password = form.password.data
		image = form.image.data
		phone = form.phone.data
		priviledge = form.priviledge.data
	
		newMember = User(name, email, password, phone, priviledge, image)
		
		try:
			db.session.add(newMember)
			db.session.commit()
		except:
			return jsonify({ "msg": "can't add to database" })
		
		return jsonify({
			"msg": "Successfully added to database",
			"user": "/api/users?email=" + urllib.parse.quote_plus(email),
			"all_users": "/api/users?limit=10"
		})
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

from .validateForm import UserUpdateForm
	
# /api/users/update/
@app.route('/api/users/update/<int:user_id>', methods=['PUT', 'GET'])
@login_required
def put_users(user_id):
	if request.method == 'GET':
		return jsonify({ 'msg': 'This URL is only for PUT request' })

	if not current_user.is_admin() and user_id != current_user.id:
		return jsonify({ "msg": "you are not allowed to update this user" })
		
	updateUser = User.query.get(user_id)
	
	if updateUser is None:
		return jsonify({ "msg": "user not found" })
	
	form = UserUpdateForm(request.form)
	
	if form.validate_on_submit():
		for value in form.data:
			if form.data[value] != '':
				if value == 'password':
					password = bcrypt.hashpw(form.data['password'], bcrypt.gensalt())
					setattr(user, value, password)
				else: 
					setattr(user, value, form.data[value])
    
		db.session.commit()
	
		result = user.__dict__
		
		del user['_sa_instance_state']
		del user['password']
		
		return jsonify({ 
			"msg": "updated successfully", 
			"result": result,
			"url": '/api/users/' + str(user.id)
		})
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

	
# /api/users/delete/<int:user_id>
@app.route('/api/users/delete/<int:user_id>', methods=['DELETE', 'GET'])
@login_required
def delete_users(user_id):
	if request.method == 'GET':
		return jsonify({ 'msg': 'This URL is only for DELETE request' })

	if not current_user.is_admin():
		return jsonify({ "msg": "you are not allowed to delete this user" })
	
	user = User.query.get(user_id)
	
	if user is None:
		return jsonify({ "msg": "user not found" })
	try:
		db.session.delete(user)
		db.session.commit()
	except:
		return jsonify({ "msg": "Can't delete" })
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_users": "/api/users?limit=10"
	})
