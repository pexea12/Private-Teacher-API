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
	
# /users/get/
@app.route('/users/get/email=<email>@<host>&password=<password>', methods=['GET'])
def get_users(email, host, password):
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    query = "select * from users where email = ? and password = ?"
    email = email + '@' + host
    c.execute(query, (email, password))
    record = c.fetchone()
    if record is None:
        non_exist_return = 'Khong ton tai user'  #
        return non_exist_return
    user_return = jsonify(
        {"id": record[0], "username": record[1], "password": record[3], "email": record[2], "phone": record[4]})  #
    return user_return


# /users/add/
@app.route('/users/add/username=<name>&email=<email>@<host>&password=<password>&phone=<phone>', methods=['POST', 'GET'])
def post_users(name, email, password, phone, host):
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    email = email + '@' + host
    query = "insert into users (name,email,password,phone) values (?,?,?,?)"
    try:
        c.execute(query, (name, email, password, phone))
    except sqlite3.Error:
        return 'Error'
    conn.commit()
    conn.close()
    return 'Success Add'


# /users/update/
# url for update email
@app.route('/users/update/email=<email>@<host0>&password=<password>&<column>=<value>@<host>', methods=['PUT', 'GET'])
# url for update name,phone , password
@app.route('/users/update/email=<email>@<host0>&password=<password>&<column>=<value>', methods=['PUT', 'GET'])
def put_users(email, host0, password, column, value, host=None):
    if column == 'id':
        return
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()
    query = "select * from users where email = ? and password = ?"
    email = email + '@' + host0
    c.execute(query, (email, password))
    record = c.fetchone()
    if record is None:
        wrong_return = "Wrong Identity Or Non Exist"  #
        return wrong_return
    else:
        if host is not None:
            value = value + '@' + host
        update_query = "update users set {0} = ? where email = ? and password = ?".format(column)
        try:
            c.execute(update_query, (value, email, password))
            conn.commit()
        except sqlite3.Error:
            error_return = 'Error'  #
            return error_return

    success_return = 'Success Update'  #
    return success_return


# /users/delete/
@app.route('/users/delete/email=<email>@<host>&password=<password>', methods=['DELETE', 'GET'])
def delete_users(email, host, password):
    conn = sqlite3.connect('database/database.db')
    c = conn.cursor()

    delete_query = "delete from users where email = ? and password = ?"
    email = email + '@' + host
    c.execute(delete_query, (email, password))
    conn.commit()

    return 'Success Del'

if __name__ == '__main__':
	app.run(debug=True)