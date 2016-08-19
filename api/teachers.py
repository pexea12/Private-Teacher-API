from api import app, db, Teacher
from flask import jsonify, request

def selectParams():
	''' Select necessary params from request.args '''
	params = {}
	list = ['id', 'name', 'email', 'phone', 'description', 'salary_per_hour', 'job', 'work_place', 'level_to_teach', 'user_id', 'image', 'location', 'location_lon', 'location_lat', 'rating', 'rating_number' ]
	
	for name in list:
		if name in request.args:
			params[name] = request.args[name]
	return params
	
# Get list of all teachers: /api/teachers/list
@app.route('/api/teachers/list', methods = ['GET'])
def get_all_teachers():
	teachers = Teacher.query
	
	limit = request.args.get('limit', None)
	
	params = selectParams()
	
	if limit is not None:
		teachers = teachers.limit(limit)
		
	teachers = teachers.filter_by(**params).all()
	
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

@app.route('/api/teachers/update', methods = ['PUT'])
def put_teachers():
	params = selectParams()
	
	if len(params) == 0:
		return jsonify({ "msg": "no record to update" })
		
	updateTeachers = Teacher.query.filter_by(**params).all()
	
	form = TeacherUpdateForm(request.form)
	
	if form.validate_on_submit():
		for user in updateTeachers:
			for name in form.data:
				if form.data[name] != '':
					setattr(user, name, form.data[name])
    
		db.session.commit()
		
		results = [teacher.__dict__ for teacher in updateTeachers]
		
		for result in results:
			del result['_sa_instance_state']
		
		return jsonify({ "msg": "updated successfully", "results": results })
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

	
# /api/teachers/delete/
@app.route('/api/teachers/delete', methods=['DELETE'])
def delete_teachers():

	params = selectParams()
	
	deleteTeachers = Teacher.query.filter_by(**params).all()
	
	try:
		for teacher in deleteTeachers:
			db.session.delete(teacher)
		db.session.commit()
	except:
		return jsonify({ "msg": "Can't delete" })
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_teachers": "/api/teachers/list"
	})
	elete
	
# Delete a teacher record by id: /api/teachers/delete/<teacher_id>
@app.route('/api/teachers/delete/<int:teacher_id>', methods = ['DELETE'])
def delete_teacher_id(teacher_id):
	teacher = Teacher.query.get(teacher_id)
	
	try:
		db.session.delete(teacher)
		db.session.commit()
	except:
		return jsonify({ "msg": "Can't delete" })
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_teachers": "/api/teachers/list"
	})