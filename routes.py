from api import app
from flask import render_template

@app.route('/')
def test():
	return 'hello world'