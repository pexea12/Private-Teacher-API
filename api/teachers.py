from api import app, db, Teacher
from flask import jsonify, request
from flask_login import current_user, login_required

def selectParams():
	''' Select necessary params from request.args '''
	params = {}
	list = ['id', 'name', 'email', 'phone', 'description', 'salary_per_hour', 'job', 'work_place', 'level_to_teach', 'user_id', 'image', 'location', 'rating', 'rating_number', 'subjects' ]
	
	for name in list:
		if name in request.args:
			params[name] = request.args[name]
	return params
	
# Get list of all teachers: /api/teachers/list
@app.route('/api/teachers/list', methods = ['GET'])
def get_all_teachers():
	teachers = Teacher.query
	
	limit = request.args.get('limit', 20)
	params = selectParams()
		
	teachers = teachers.filter_by(**params)
	
	if limit is not None:
		teachers = teachers.limit(limit)
	
	teachers = teachers.all()
	
	if len(teachers) == 0:
		return jsonify({ "msg": "no teacher found" })
	
	results = [ teacher.__dict__ for teacher in teachers ]
	for result in results:
		del(result['_sa_instance_state'])
		
	return jsonify(results)

# Get a teacher by id: /api/teacher/<int:teacher_id>
@app.route('/api/teachers/<int:teacher_id>', methods = ['GET'])
def get_a_teacher(teacher_id):
	teacher = Teacher.query.get(teacher_id)
	
	if teacher is None:
		return jsonify({'msg': 'teacher does not exist'})
		
	result = teacher.__dict__
	del(result['_sa_instance_state'])
	
	return jsonify(result)
	
# Add a new teacher: /api/teachers/add

from .validateForm import TeacherForm

@app.route('/api/teachers/add', methods = ['POST'])
@login_required
def add_teacher():
	form = TeacherForm(request.form)
	
	if form.validate_on_submit():
		teacher = Teacher(**form.data)
		
		try:
			db.session.add(teacher)
			db.session.commit()
		except:
			return jsonify({ "msg": "can't add to database" })
			
		return jsonify({
			"msg": "Successfully added to database",
			"teacher": "/api/teachers/" + str(teacher.id),
			"all_teachers": "/api/teachers/list"
		})
		
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

# Update a teacher record by id: /api/teacher/update

from .validateForm import TeacherUpdateForm

@app.route('/api/teachers/update/<int:teacher_id>', methods = ['PUT'])
@login_required
def put_teachers(teacher_id):
	updateTeacher = Teacher.query.get(teacher_id)
	
	if updateTeacher is None:
		return jsonify({ "msg": "teacher not found" })
		
	if not current_user.is_admin() and updateTeacher.user_id != current_user.id:
		return jsonify({ "msg": "you are not allowed to update this teacher" })
	
	form = TeacherUpdateForm(request.form)
	
	if form.validate_on_submit():
		for value in form.data:
			if form.data[value] != '':
				setattr(updateTeacher, value, form.data[value])
    
		db.session.commit()
		
		result = updateTeacher.__dict__
		
		del result['_sa_instance_state']
		
		return jsonify({ 
			"msg": "updated successfully", 
			"result": result 
		})
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)
	
# Delete a teacher record by id: /api/teachers/delete/<teacher_id>
@app.route('/api/teachers/delete/<int:teacher_id>', methods = ['DELETE','GET'])
@login_required
def delete_teacher_id(teacher_id):
	teacher = Teacher.query.get(teacher_id)
	
	if teacher is None:
		return jsonify({ "msg": "teacher not found" })
	if not current_user.is_admin() and teacher.user_id != current_user.id:
		return jsonify({ "msg": "you are not allowed to delete this teacher" })
	
	try:
		db.session.delete(teacher)
		db.session.commit()
	except:
		return jsonify({ "msg": "Can't delete" })
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_teachers": "/api/teachers/list"
	})
	
from geopy.geocoders import GoogleV3
from .helpers import distance

geolocator = GoogleV3(timeout=5)

@app.route('/api/teachers/recommend', methods=['POST'])
def recommend_teachers():
	'salary_per_hour', 'level_to_teach','location', 'subjects'
	limit = request.args['limit']
	
	subjects = request.form['subjects']
	level_to_teach = request.form['level_to_teach']
	salary_per_hour = request.form['salary_per_hour']
	
	teachers = db.session.query(Teacher) \
			  .filter(Teacher.subjects == subjects) \
			  .filter(Teacher.level_to_teach == level_to_teach) \
			  .filter(Teacher.salary_per_hour < salary_per_hour) \
			  .limit(limit).all()
	
	results = [ teacher.__dict__ for teacher in teachers ]
	for result in results:
		del(result['_sa_instance_state'])
		
	return jsonify(results)