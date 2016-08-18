from api import app
from flask import render_template
from api.validateForm import UserForm

app.secret_key = 'Intelligence Program'

@app.route('/test')
def test():
	form = UserForm()
	return render_template('test.html', form=form)

	
app.run(debug=True)