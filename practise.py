from flask import Flask, request
from wtforms import validators, StringField
from flask_wtf import FlaskForm
import random
import os
import json

FLASK_RANDOM_SEED = os.environ.get('FLASK_RANDOM_SEED', 2)

class Number(object):
	obj = None
	def __new__(cls, *args, **kwargs):
		if cls.obj is None:
			cls.obj = object.__new__(cls, *args, **kwargs)
			cls.obj.number = None

		return cls.obj



class NumberForm(FlaskForm):

	def is_num(form, field):
		if not str(field.data).isdigit():
			raise wtforms.validators.ValidationError()


	guess = StringField(validators=[validators.DataRequired(), is_num])


app = Flask(__name__)

app.config.update(
	DEBUG=True,
    WTF_CSRF_ENABLED=False,
)



@app.route('/', methods=['GET'])
def generate_number():
	if request.method == 'GET':
		random.seed(FLASK_RANDOM_SEED)
		number = Number()
		number.number = random.randint(1, 10)
		return 'number was guessed', 200


@app.route('/guess', methods=['POST'])
def guess():
	if request.method == 'POST':
		form = NumberForm(request.form)
		if form.validate():
			num = Number().number
			print(type(Number()))
			if not num:
				return "number wasn't guessed", 400
			if int(form.guess.data) < num:
				return json.dumps({'res':['<', 200]})
			if int(form.guess.data) > num:
				return json.dumps({'res':['>', 200]})
			return json.dumps({'res':['=', 200]})
		return json.dumps({'status': form.validate(), 'errors': form.errors})


with app.test_request_context('/'):
	print(request, type(request), request.method)

if __name__ == '__main__':
	app.run()
