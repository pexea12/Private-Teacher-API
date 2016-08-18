from api import app, db, User
from flask import jsonify, request

def selectParams():
	''' Select necessary params from request.args '''
	params = {}
	list = ['id', 'name', 'image', 'phone', 'email', 'priviledge']
	
	for name in list:
		if name in request.args:
			params[name] = request.args[name]
	return params
	
# /api/users/
@app.route('/api/users', methods=['GET'])
def get_users():

	# Take the params
	limit = request.args.get('limit', None)
	
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

from .validateForm import UserForm
import bcrypt, urllib
	
# /api/users/add/
@app.route('/api/users/add', methods=['GET', 'POST'])
def post_users():
	if request.method == 'GET':
		return jsonify({ 'msg': 'This URL is only for POST request' })
	
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
			"all_user": "/api/users?limit=10"
		})
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

from .validateForm import UserUpdateForm
	
# /api/users/update/
@app.route('/api/users/update', methods=['PUT', 'GET'])
def put_users():
	if request.method == 'GET':
		return jsonify({ 'msg': 'This URL is only for PUT request' })

	params = selectParams()
	
	if len(params) == 0:
		return jsonify({ "msg": "no record to update" })
		
	updateUsers = User.query.filter_by(**params).all()
	
	form = UserUpdateForm(request.form)
	
	if form.validate_on_submit():
		for user in updateUsers:
			for name in form.data:
				if form.data[name] != '':
					if name == 'password':
						password = bcrypt.hashpw(form.data['password'], bcrypt.gensalt())
						setattr(user, name, password)
					else: 
						setattr(user, name, form.data[name])
    
		db.session.commit()
	
		results = []
		for user in updateUsers:
			result = {}
			
			result['id'] = user.id
			result['name'] = user.name
			result['image'] = user.image
			result['phone'] = user.phone
			result['email'] = user.email
			result['priviledge'] = user.priviledge
			
			results.append(result)
		
		return jsonify({ "msg": "updated successfully", "results": results })
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

	
# /api/users/delete/
@app.route('/api/users/delete', methods=['DELETE', 'GET'])
def delete_users():
	if request.method == 'GET':
		return jsonify({ 'msg': 'This URL is only for DELETE request' })

	params = selectParams()
	
	deleteUsers = User.query.filter_by(**params).all()
	
	try:
		for user in deleteUsers:
			db.session.delete(user)
		db.session.commit()
	except:
		return { "msg": "Can't delete" }
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_user": "/api/users?limit=10"
	})