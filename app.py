from api import app, login_manager

app.secret_key = 'Intelligence Program'
	
login_manager.init_app(app)

import routes

app.run(debug=True)