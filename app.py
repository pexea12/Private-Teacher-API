from api import app
from flask import render_template
from api.validateForm import UserForm

app.secret_key = 'Intelligence Program'
	
app.run(debug=True)