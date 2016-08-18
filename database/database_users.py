import sqlite3

''' Generate database for project '''
''' WARNING: Only run this file when the database is empty '''

conn = sqlite3.connect('database.db')
print('Opened database successfully')

conn.execute('CREATE TABLE IF NOT EXISTS priviledges (\
	id INTEGER PRIMARY KEY AUTOINCREMENT, \
	name VARCHAR(30) NOT NULL UNIQUE \
)')

conn.execute('INSERT INTO priviledges (name) VALUES ("Admin")')
conn.execute('INSERT INTO priviledges (name) VALUES ("Member")')
conn.commit()

conn.execute('CREATE TABLE IF NOT EXISTS users ( \
	id INTEGER PRIMARY KEY AUTOINCREMENT, \
	image TEXT, \
	name VARCHAR(30) NOT NULL, \
	email VARCHAR(40) UNIQUE NOT NULL, \
	password TEXT NOT NULL, \
	phone VARCHAR(20) NOT NULL, \
	priviledge INTEGER NOT NULL, \
	FOREIGN KEY(priviledge) REFERENCES priviledges(id) \
)')
print('Create users table successfully')



''' Add some sample data '''

conn.execute('INSERT INTO users (image, name, email, password, phone, priviledge) VALUES ( \
	"/static/default1.jpg", \
	"Magnus Carlsen", \
	"carlsen@yahoo.com.vn", \
	"$2b$12$YvRh77M/ix9Jc/2eDSstaOGt8pT/nTxneJP3tfo86My0EOpGxeu/q", \
	"0123456789", \
	1 \
)')

conn.execute('INSERT INTO users (image, name, email, password, phone, priviledge) VALUES ( \
	"/static/default2.jpg", \
	"Levon Aronian", \
	"aronian@gmail.com", \
	"$2b$12$XFpjtU/7JuY3M8m6DcWxJuVn5OEERf0QcnwAzxz6uOVf6F7PGIKbq", \
	"0123456788", \
	1 \
)')

conn.execute('INSERT INTO users (image, name, email, password, phone, priviledge) VALUES ( \
	"/static/default1.jpg", \
	"Vladimir Kramnik", \
	"kramnik@outlook", \
	"$2b$12$Xgb.RwXXdHzMbztTv4Tq3uIEQts/379dJXepFnZ4lxoEBAtokLkQC", \
	"0123456787", \
	2 \
)')

conn.execute('INSERT INTO users (image, name, email, password, phone, priviledge) VALUES ( \
	"/static/default1.jpg", \
	"Anish Giri", \
	"giri@hotmail.com", \
	"$2b$12$h7ADJfxL3BBXRuAi0zJKZ.HL/BR5OcPFFiFm0C7rzcJm6wF56GOsq", \
	"0123456786", \
	2 \
)')

conn.execute('INSERT INTO users (image, name, email, password, phone, priviledge) VALUES ( \
	"/static/default1.jpg", \
	"Veselin Topalov", \
	"topalov@vnu.edu.vn", \
	"$2b$12$TTkou0qkBfanlttWpjjco.0ryMxROYD5TsANpBuEHqdAbAAM2Vvr.", \
	"0123456785", \
	2 \
)')

conn.commit()
conn.close()