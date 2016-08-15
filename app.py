from flask import Flask

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
	
@app.route('/teachers', methods=['GET'])
def get_teachers():
	return 'Return GET teachers'
	
@app.route('/teachers', methods=['POST'])
def post_teachers():
	return 'Return POST teachers'

@app.route('/teachers', methods=['PUT'])
def put_teachers():
	return 'Return PUT teachers'
	
@app.route('/teachers', methods=['DELETE'])
def delete_teachers():
	return 'Return DELETE teachers'
	
@app.route('/users', methods=['GET'])
def get_users():
	return 'Return GET users'
	
@app.route('/users', methods=['POST'])
def post_users():
	return 'Return POST users'

@app.route('/users', methods=['PUT'])
def put_users():
	return 'Return PUT users'
	
@app.route('/users', methods=['DELETE'])
def delete_users():
	return 'Return DELETE users'

if __name__ == '__main__':
	app.run(debug=True)