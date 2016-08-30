from api import app, db, Student, Teacher
from flask import jsonify, request
from flask_login import current_user, login_required

def selectParams():
	''' Select necessary params from request.args '''
	params = {}
	list = ['id', 'name', 'email', 'phone', 'description', 'price_per_hour', 'school', 'level', 'user_id', 'image', 'location', 'subjects']
	
	for name in list:
		if name in request.args:
			params[name] = request.args[name]
	return params
	
# Get list of all students: /api/students/list
@app.route('/api/students/list', methods = ['GET'])
def get_all_students():
	students = Student.query
	
	limit = request.args.get('limit', 20)
	params = selectParams()
		
	students = students.filter_by(**params)
	
	if limit is not None:
		students = students.limit(limit)
	
	students = students.all()
	
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
@login_required
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

@app.route('/api/students/update/<int:student_id>', methods = ['PUT'])
@login_required
def put_students(student_id):
	updateStudent = Student.query.get(student_id)
	
	if updateStudent is None:
		return jsonify({ "msg": "student not found" })
		
	if not current_user.is_admin() and updateStudent.user_id != current_user.id:
		return jsonify({ "msg": "you are not allowed to update this student" })
	
	form = StudentUpdateForm(request.form)
	
	if form.validate_on_submit():
		for value in form.data:
			if form.data[value] != '':
				setattr(updateStudent, value, form.data[value])
    
		db.session.commit()
		
		result = updateStudent.__dict__
		
		del result['_sa_instance_state']
		
		return jsonify({ 
			"msg": "updated successfully", 
			"result": result 
		})
	
	results = { "msg": "can't pass form validation" }
	results["errors"] = form.errors
	
	return jsonify(results)
	
# Delete a student record by id: /api/students/delete/<student_id>
@app.route('/api/students/delete/<int:student_id>', methods = ['DELETE'])
@login_required
def delete_student_id(student_id):
	student = Student.query.get(student_id)
	
	if student is None:
		return jsonify({ "msg": "student not found" })
	if not current_user.is_admin() and student.user_id != current_user.id:
		return jsonify({ "msg": "you are not allowed to delete this student" })
	
	try:
		db.session.delete(student)
		db.session.commit()
	except:
		return jsonify({ "msg": "Can't delete" })
		
	return jsonify({ 
		"msg": "Successfully deleted",
		"all_students": "/api/students/list"
	})
	
@app.route('/api/students/rate/<int:teacher_id>', methods=['GET'])
@login_required
def rate_teacher(teacher_id):
	rating = request.args.get('rating', None)
	
	teacher = Teacher.query.get(teacher_id)
	
	if teacher is None:
		return jsonify({ "msg": "teacher not found" })
	if rating is None:
		return jsonify({ "msg": "you don't rate this teacher"})
		
	current_rating = teacher.rating
	rating_no = teacher.rating_number

	current_rating = (current_rating * rating_no + rating) / rating_no
	rating_no = rating_no + 1

	teacher.rating = current_rating
	teacher.rating_number = rating_no
	
	db.session.commit()
	
	return jsonify({ 
		"msg": "rated successfully",
		"teacher_id": teacher.id,
		"teacher_rating": teacher.rating
	})

from geopy.geocoders import GoogleV3
from .helpers import distance

geolocator = GoogleV3(timeout=5)

@app.route('/api/students/recommend', methods=['POST'])
def recommend_students():
	limit = request.args['limit']
	
	subjects = request.form['subjects']
	level = request.form['level']
	price_per_hour = request.form['price_per_hour']
	
	students = db.session.query(Student) \
			  .filter(Student.subjects == subjects) \
			  .filter(Student.level == level) \
			  .filter(Student.price_per_hour > price_per_hour) \
			  .limit(limit).all()
			  
	print(students)
	
	results = [ student.__dict__ for student in students ]
	for result in results:
		del(result['_sa_instance_state'])
		
	return jsonify(results)
