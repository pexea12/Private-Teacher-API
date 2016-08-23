from api import app, login_manager

app.secret_key = 'Intelligence Program'

import routes

login_manager.init_app(app)


app.run(debug=True)