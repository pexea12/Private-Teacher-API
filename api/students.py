from api import app, db, Student
from flask import jsonify, request

def selectParams():
	''' Select necessary params from request.args '''
	params = {}
	list = ['id', 'name', 'email', 'phone', 'description', 'price_per_hour', 'school', 'level', 'user_id', 'image', 'location', 'location_lon', 'location_lat']
	
	for name in list:
		if name in request.args:
			params[name] = request.args[name]
	return params
	
# Get list of all students: /api/students/list
@app.route('/api/students/list', methods = ['GET'])
def get_all_students():
	students = Student.query
	
	limit = request.args.get('limit', None)
	
	params = selectParams()
	
	if limit is not None:
		students = students.limit(limit)
		
	students = students.filter_by(**params).all()
	
	if len(students) == 0:
		return jsonify({ "msg": "no student found" })
	
	results = [ student.__dict__ for student in students ]
	for result in results:
		del(result['_sa_instance_state'])
		
	return jsonify(results)

# Get a student by id: /api/student/<int:student_id>
@app.route('/api/students/<int:student_id>', methods = ['GET'])
def get_a_student(student_id):
	student = Student.query.get(student_id)
	
	if student is None:
		return jsonify({'msg': 'student does not exist'})
		
	result = student.__dict__
	del(result['_sa_instance_state'])
	
	return jsonify(result)
	
# Add a new student: /api/students/add

from .validateForm import StudentForm

@app.route('/api/students/add', methods = ['POST'])
def add_student():
	form = StudentForm(request.form)
	
	if form.validate_on_submit():
		student = Student(**form.data)
		
		try:
			db.session.add(student)
			db.session.commit()
		except:
			return jsonify({ "msg": "can't add to database" })
			
		return jsonify({
			"msg": "Successfully added to database",
			"student": "/api/students/" + str(student.id),
			"all_students": "/api/students/list"
		})
		
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

# Update a student record by id: /api/student/update

from .validateForm import StudentUpdateForm

@app.route('/api/students/update', methods = ['PUT'])
def put_students():
	params = selectParams()
	
	if len(params) == 0:
		return jsonify({ "msg": "no record to update" })
		
	updateStudents = Student.query.filter_by(**params).all()
	
	form = StudentUpdateForm(request.form)
	
	if form.validate_on_submit():
		for user in updateStudents:
			for name in form.data:
				if form.data[name] != '':
					setattr(user, name, form.data[name])
    
		db.session.commit()
		
		results = [student.__dict__ for student in updateStudents]
		
		for result in results:
			del result['_sa_instance_state']
		
		return jsonify({ "msg": "updated successfully", "results": results })
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)

	
# /api/students/delete/
@app.route('/api/students/delete', methods=['DELETE'])
def delete_students():

	params = selectParams()
	
	deleteStudents = Student.query.filter_by(**params).all()
	
	try:
		for student in deleteStudents:
			db.session.delete(student)
		db.session.commit()
	except:
		return jsonify({ "msg": "Can't delete" })
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_students": "/api/students/list"
	})
	elete
	
# Delete a student record by id: /api/students/delete/<student_id>
@app.route('/api/students/delete/<int:student_id>', methods = ['DELETE'])
def delete_student_id(student_id):
	student = Student.query.get(student_id)
	
	try:
		db.session.delete(student)
		db.session.commit()
	except:
		return jsonify({ "msg": "Can't delete" })
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_students": "/api/students/list"
	})