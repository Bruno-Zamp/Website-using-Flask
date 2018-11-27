from app import db


#Tabela de informações dos usuários
class User(db.Model): 
	__tablename_ = "user"
	
	id = db.Column(db.Integer , primary_key=True)
	username = db.Column(db.String , unique=True)
	password = db.Column(db.String)
	name = db.Column(db.String)
	email = db.Column(db.String, unique=True)
	
	@property
	def is_authenticated(self):
		return True
		
	@property
	def is_active(self):
		return True
		
	@property
	def is_anonymous(self):
		return False
		
	def get_id(self):
		return  str(self.id)
	
	def __init__(self, username, password, name, email): #Construtor da classe
		self.username = username
		self.password = password
		self.name = name
		self.email = email
		
	def __repr__(self): #Representação na chamada
		return "<User %r>" % self.username

#Tabela de informações dos posts dos usuários
class Post(db.Model):
	__tablename_ = "posts"
	
	id = db.Column(db.Integer , primary_key=True)
	content = db.Column(db.Text)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
	
	user = db.relationship('User', foreign_keys=user_id) 
	
	def __init_(self, content, user_id): #Construtor da classe
		self.content = content
		self.user_id = user_id
	
	def __repr__(self): #Representação na chamada
		return "<Post %r" % self.id
	
#Tabela de informações dos seguidores do usuário
class Follow(db.Model):
	__tablename_ = "follow"
	
	id = db.Column(db.Integer, primary_key=True)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id')) 
	follower_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	
	user = db.relationship('User', foreign_keys= user_id)
	follower = db.relationship('User', foreign_keys= follower_id)
	
	def __repr__(self): #Representação na chamada
		return "<Follow %r" % self.id

		
