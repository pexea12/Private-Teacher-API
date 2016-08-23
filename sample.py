''' Create sample data '''
''' Only run for the first time '''


from api import db, User, Student, Teacher

db.create_all()


db.session.add(User(
	'Magnus Carlsen',
	'carlsen@gmail.com',
	'carlsen',
	'1234',
	'Admin'
))

db.session.add(User(
	'Veselin Topalov',
	'topalov@gmail.com',
	'topalov',
	'10001',
	'Member'
))

db.session.add(User(
	'Levon Aronian',
	'aronian@gmail.com',
	'aronian',
	'12345',
	'Admin'
))

db.session.add(User(
	'Vladimir Kramnik',
	'kramnik@gmail.com',
	'kramnik',
	'123456',
	'Member'
))

db.session.add(User(
	'Anish Giri',
	'giri@gmail.com',
	'giri',
	'1234567',
	'Member'
))

db.session.commit()

db.session.add(Student(
	'Magnus Carlsen',
	'carlsen_temp@gmail.com',
	'04343634',
	'Best chess player in the world. No need to explain',
	32523,
	'Norway Chess School',
	'Elite',
	1,
	'182 Luong The Vinh, Thanh Xuan, Ha Noi',
	'Math',
	'default1.jpg'
))

db.session.add(Student(
	'Giri Dad',
	'giridad@gmail.com',
	'0433243634',
	'Best chess player in the world. No need to explain',
	32523,
	'Netherland Chess School',
	'Medium',
	5,
	'144 Xuan Thuy, Cau Giay, Ha Noi',
	'Math',
	'default1.jpg'
))

db.session.add(Student(
	'Carlsen bro',
	'carlsen_temp_2@gmail.com',
	'04343634',
	'Best chess player in the world. No need to explain',
	300,
	'Norway Chess School',
	'Beginner',
	1,
	'Dai hoc Bach Khoa Ha Noi',
	'Math',
	'default1.jpg'
))

db.session.add(Student(
	'Topalov son 2',
	'topalov_son_2@gmail.com',
	'04343634wtewe',
	'Brother of Best chess player in the world. No need to explain',
	200,
	'Bulgary Chess School',
	'Normal',
	2,
	'16A Ly Nam De, Ha Noi',
	'Math',
	'default1.jpg'
))

db.session.add(Student(
	'Topalov son 1',
	'topalov_son_1@gmail.com',
	'043423523634',
	'Second Best chess player in the world. No need to explain',
	12433,
	'Bulgary Chess School',
	'Elite',
	2,
	'Ho Chi Minh City',
	'Math',
	'default1.jpg'
))

db.session.commit()


db.session.add(Teacher(
	'Magnus Carlsen', 
	'carlsen1@gmail.com',
	'3252364',
	'Best teacher in the world. no need to argue',
	123,
	'worker',
	'Norway ambassador',
	'elite',
	1,
	'43 Nguyen Chi Thanh, Hanoi',
	'Math'
))

db.session.add(Teacher(
	'Magnus Carlsen', 
	'carlsen2@gmail.com',
	'3252364',
	'Best teacher in the world. no need to argue. teach beginner also',
	1236,
	'worker',
	'Norway ambassador',
	'beginner',
	1,
	'47 Nguyen Chi Thanh, Hanoi',
	'Math'
))

db.session.add(Teacher(
	'Ruslan Ponomariov', 
	'ponomariov@gmail.com',
	'32523623524',
	'Ukraina. country of chess',
	12334,
	'student',
	'University of Engineering and Technology',
	'expert',
	2,
	'Sapa, Lao Cai',
	'Math'
))

db.session.add(Teacher(
	'Alexander Grischuk', 
	'grischuk@gmail.com',
	'3252364343',
	'Best russian teacher in the world. no need to argue',
	123,
	'student',
	'University of Science and Technology',
	'medium',
	5,
	'Manchester, England',
	'Math'
))

db.session.add(Teacher(
	'Peter Svidler', 
	'svilder@gmail.com',
	'323463252364',
	'want to have a lesson? call me maybe',
	1232,
	'student',
	'Chu Van An high school',
	'beginner',
	2,
	'43 Nguyen Chi Thanh, Hanoi',
	'Math'
))

db.session.commit()