import sqlite3

''' Generate database for project '''
''' WARNING: Only run this file when the database is empty '''

conn = sqlite3.connect('database.db')
print('Opened database successfully')

conn.execute('CREATE TABLE IF NOT EXISTS users ( \
	id INTEGER PRIMARY KEY AUTOINCREMENT, \
	name VARCHAR(30) NOT NULL, \
	email VARCHAR(40) UNIQUE NOT NULL, \
	password TEXT NOT NULL, \
	phone VARCHAR(20) NOT NULL\
)')
print('Create users table successfully')

conn.execute('CREATE TABLE IF NOT EXISTS teachers ( \
	id INTEGER PRIMARY KEY AUTOINCREMENT, \
	name VARCHAR(30) NOT NULL, \
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
print("Create teachers table successfully")

conn.execute('CREATE TABLE IF NOT EXISTS students ( \
	id INTEGER PRIMARY KEY AUTOINCREMENT, \
	name VARCHAR(30) NOT NULL, \
	address_lon VARCHAR(20), \
	address_lat VARCHAR(20), \
	phone VARCHAR(20) NOT NULL, \
	email VARCHAR(40) UNIQUE NOT NULL, \
	user_created INTEGER NOT NULL, \
	description TEXT, \
	price INTEGER, \
	school VARCHAR(30), \
	level TEXT, \
	FOREIGN KEY(user_created) REFERENCES users(id) \
)')
print("Create students table successfully")

conn.execute('CREATE TABLE IF NOT EXISTS subjects ( \
	id INTEGER PRIMARY KEY AUTOINCREMENT, \
	name VARCHAR(20) NOT NULL \
)')
print("Create subjects table successfully")

conn.execute('CREATE TABLE IF NOT EXISTS teacher_subject ( \
	teacher_id INTEGER NOT NULL, \
	subject_id INTEGER NOT NULL, \
	FOREIGN KEY(teacher_id) REFERENCES teachers(id) ON DELETE CASCADE, \
	FOREIGN KEY(subject_id) REFERENCES subjects(id) ON DELETE CASCADE \
)')
print("Create teacher_subject table successfully")

# Add data to subjects table

conn.execute("INSERT INTO subjects (name) VALUES ('Mathematics')")
conn.execute("INSERT INTO subjects (name) VALUES ('Physics')")
conn.execute("INSERT INTO subjects (name) VALUES ('Chemistry')")
conn.execute("INSERT INTO subjects (name) VALUES ('History')")
conn.execute("INSERT INTO subjects (name) VALUES ('Geography')")
conn.execute("INSERT INTO subjects (name) VALUES ('English')")
conn.execute("INSERT INTO subjects (name) VALUES ('Biography')")
conn.execute("INSERT INTO subjects (name) VALUES ('Computer Science')")
conn.execute("INSERT INTO subjects (name) VALUES ('Literature')")
conn.execute("INSERT INTO subjects (name) VALUES ('French')")
conn.execute("INSERT INTO subjects (name) VALUES ('Chinese')")
conn.execute("INSERT INTO subjects (name) VALUES ('Russian')")
conn.execute("INSERT INTO subjects (name) VALUES ('Others')")