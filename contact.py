from flask import Flask, url_for, render_template, redirect
from wtforms import validators, StringField, TextField, SubmitField
from flask_wtf import FlaskForm, RecaptchaField


app = Flask(__name__)
app.secret_key = 'something'

app.config.update(
	secret_key = "something",
	DEBUG=True,
	WTF_CSRF_ENABLED = True,
	WTF_CSRF_SECRET_KEY = "this must be changed",
	RECAPTCHA_PUBLIC_KEY = "this also must be changed",
	RECAPTCHA_PRIVATE_KEY = "and this"
)

class ContactForm(FlaskForm):
	name = StringField('name', validators=[validators.DataRequired()])
	email = StringField('email', validators=[validators.Email(message='Not a valid email'), validators.DataRequired()])
	body = TextField('body', validators=[
			validators.Length(min=4, message='the comment is too short'), 
			validators.DataRequired(message='You need to provide a comment')
		])
	recaptcha = RecaptchaField()
	submit = SubmitField('Submit')


@app.route('/contact/', methods=['GET', 'POST'])
def contact():
	form = ContactForm()
	if form.validate_on_submit():
		return redirect(url_for('success'))
	return render_template('contact.html', form = form)


@app.route('/', methods=["GET", "POST"])
def success():
	return "succes", 200

if __name__ == '__main__':
	app.run()