from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
   # llamado a OpenAI
   return "Hello World!"


@app.route('/bye')
def bye():
   return "Goodbye!"


@app.route('/iniciar-sesion')
def iniciar_sesion():
   return "Iniciar sesión"


@app.route('/users/<username>')
def users(username):
   return "Perfil de usuario: " + username


