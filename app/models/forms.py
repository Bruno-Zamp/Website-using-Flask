from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.fields.html5 import EmailField
from wtforms.validators import DataRequired, Email, InputRequired, EqualTo

class LoginForm(FlaskForm):
	username = StringField("username", validators=[DataRequired()])
	password = PasswordField("password", validators=[DataRequired()])
	remember = BooleanField("remember")
class CriarContaForm(FlaskForm):
	username = 	StringField("username", validators=[DataRequired()])
	email = 	EmailField("email", validators = [DataRequired(), Email()])
	name = 		StringField("name", validators=[DataRequired()])
	password = 	PasswordField("password", validators=[InputRequired(), EqualTo('confirm', message='Passwords must match')])
	confirm  = 	PasswordField('repeat password')
	
