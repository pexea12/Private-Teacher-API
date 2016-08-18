from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

@app.route('/students', methods=['GET'])
def get_students():
	return 'Return GET students'
	
@app.route('/students', methods=['POST'])
def post_students():
	return 'Return POST students'

@app.route('/students', methods=['PUT'])
def put_students():
	return 'Return PUT students'
	
@app.route('/students', methods=['DELETE'])
def delete_students():
	return 'Return DELETE students'

# API for teachers
@app.route('/teachers', methods=['GET'])
def get_teachers():
	conn = sql.connect('database.db')
	con.row_factory = sql.Row
	
	cur = con.cursor()
	cur.execute('SELECT * FROM teachers')
	rows = cur.fetchall()
	
	return jsonify(rows)

conn.execute('CREATE TABLE IF NOT EXISTS teachers ( \
id INTEGER PRIMARY KEY AUTOINCREMENT, \
name VARCHAR(30) NOT NULL, \
image TEXT, \
address_lon VARCHAR(20), \
address_lat VARCHAR(20), \
phone VARCHAR(20) NOT NULL, \
email VARCHAR(40) UNIQUE NOT NULL, \
user_created INTEGER NOT NULL, \
description TEXT, \
expected_salary INTEGER, \
job TEXT, \
work_place TEXT, \
level_to_teach TEXT, \
FOREIGN KEY(user_created) REFERENCES users(id) \
)')
@app.route('/teachers', methods=['POST'])
def post_teachers():
	try:
		name = request.form['name']
		image = request.form['image']
		address_lon = request.form['address_lon']
		address_lat = request.form['address_lat']
		phone = request.form['phone']
		email = request.form['email']
		user_created = request.form['user_created']
		description = request.form['description']
		expected_salary = request.form['expected_salary']
		job = request.form['job']
		work_place = request.form['work_place']
		level_to_teach = request.form['level_to_teach']
		
		with sqlite3.connect('database/database.db') as conn:
			cur = conn.cursor()
			cur.execute('INSERT INTO teachers (name, image, address_lon, address_lat, phone, email, user_created, description, expected_salary, job, work_place, level_to_teach) VALUES (?, ?, ?, ?, ?, ?)')
			conn.commit()
			msg = 'Teacher successfully added'
		except:
			conn.rollback()
			msg = 'Error in insert teacher'
		finally:
			return render_template('result.html', msg=msg)
			conn.close()
			

@app.route('/teachers', methods=['PUT'])
def put_teachers():
	return 'Return PUT teachers'
	
@app.route('/teachers', methods=['DELETE'])
def delete_teachers():
	return 'Return DELETE teachers'
	

if __name__ == '__main__':
	app.run(debug=True)