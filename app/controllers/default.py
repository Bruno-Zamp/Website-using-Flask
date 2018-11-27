from app import app,db, lm  #variavel app do módulo app 
from flask import render_template, flash, redirect, url_for
from flask_login import login_user, logout_user

from app.models.forms import LoginForm,CriarContaForm
from app.models.tables import User

@lm.user_loader
def load_user(id):
	return User.query.filter_by(id=id).first()

#Fortmato de página no Flask!
@app.route("/index/") 			
@app.route("/") 								# 1-rota da página
def index(): 									# 2-função
	return render_template('index.html')		# 3-conteudo

@app.route("/base")
def base():
	return render_template('base.html')

@app.route("/criarConta", methods=["GET","POST"])
def criarConta():
	form = CriarContaForm()
	if form.validate_on_submit():
		Tusername = User.query.filter_by(username = form.username.data).first() # Testa se o usuário está contido no db
		Temail = User.query.filter_by(email = form.email.data).first()
		if Tusername:
			flash("This username -"+Tusername.username+"- has already been used... :(")
		elif Temail:
			flash("This email -"+ Temail.email+"- has already been used... :(")
		else:
			newuser = User(form.username.data, form.password.data, form.name.data, form.email.data)
			db.session.add(newuser)
			db.session.commit()
			flash("Your account has been created!")
			return redirect(url_for ("login"))	
	return render_template('criarConta.html', form=form)

@app.route("/login", methods=["GET","POST"])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username = form.username.data).first() # Testa se o usuário está contido no db
		
		if user and user.password == form.password.data: # Testa se a senha e o usuário estão corretos
			login_user(user)
			return redirect(url_for ("index"))
			flash("Logged in")
		else:
			flash("Invalid login.")
			
	return render_template('login.html', form=form)

@app.route("/logout")
def logout():
	logout_user()
	return redirect(url_for("index"))

@app.route("/teste/<info>")
@app.route("/teste", defaults={"info": None})
def teste(info):
	i = User.query.filter_by(username)
	db.session.add(i)
	db.session.commit()
	return "OK"
