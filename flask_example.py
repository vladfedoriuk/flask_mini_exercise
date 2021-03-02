from flask import Flask, request
from flask_wtf import FlaskForm
from wtforms import StringField, validators
import functools 
from datetime import datetime
import json
import os

class ContactForm(FlaskForm):
	name = StringField(validators=[
		validators.Length(min=3, max=25)
		])
	email = StringField(validators=[
		validators.Length(min=5, max=35),
		validators.Email()
		])
	job = StringField(validators=[
		validators.AnyOf(['IT', 'HR', 'Bank'], message="No option matched"),
		validators.DataRequired()
		])
	def date_check(form, field):
		if int(field.data)!=datetime.now().month:
			raise wtforms.validators.ValidationError()
	date = StringField(validators=[date_check, validators.DataRequired()])



class LocaleForm(FlaskForm):
	def is_locale(form, field):
		if not field.data.isalpha():
			raise wtforms.validators.ValidationError()

	locale = StringField(validators=[validators.DataRequired(), is_locale])


class UserForm(FlaskForm):
	email = StringField(validators=[validators.Email(), validators.DataRequired()])
	password = StringField(validators=[validators.Length(min=6), validators.DataRequired(), validators.EqualTo('confirmation')])
	confirmation = StringField()

app = Flask(__name__)
app.config.update(
    DEBUG=True,
    SECRET_KEY=os.environ.get('SECRET_KEY'),
    WTF_CSRF_ENABLED=False,
)


@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        print(request.form)
        form = ContactForm(request.form)
        print(form.validate())

        if form.validate():
            return ('valid', 200)
        else:
            return ('invalid', 400)

    if request.method == 'GET':
        return ('hello world!', 200)


@app.route('/hello/<path:user>')
def hello(user):
	return f'hello {user}!'


@app.route('/serve/<path:filename>')
def show(filename):
	try:
		prefix = '.\\'+'files'+'\\'
		f = open(prefix+filename, 'r')
	except FileExistsError:
		return "file doesn't exist", 404
	except FileNotFoundError:
		return "file not found", 404
	return f.read(), 200

@app.route('/add/<int:x>/<int:y>')
def add(x, y):
	return str(x+y)


@app.route('/max/<s>/<t>/<e>')
def the_longest(s, t, e):
	return functools.reduce(lambda x, y: max(x, y, key=len), (s, t, e))


@app.route('/file/<filename>')
def check_exist(filename):
	try:
		f = open(filename)
	except:
		return str(False)
	finally:
		f.close()
	return str(True)


@app.route('/locales', methods=['GET', 'POST'])
def locales():
	try:
		l = locales.loc
	except AttributeError:
		locales.loc = {'ru', 'en', 'it'}

	if request.method == 'GET':
		return json.dumps(list(locales.loc))

	if request.method == 'POST':
		print(f'Form: {request.form}')
		form = LocaleForm(request.form)
		print(form.validate())
		if form.validate():
			locales.loc.add(form.locale.data)
			return 'updated', 200
		else:
			return 'invalid locale', 400


@app.route('/form/user', methods=['POST'])
def validation():
	if request.method=='POST':
		print(f'Form: {request.form}')
		form = UserForm(request.form)
		return json.dumps({'status': form.validate(), 'errors': form.errors})

if __name__ == '__main__':
	app.run()	