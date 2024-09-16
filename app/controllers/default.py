from app import app, db
from flask_login import login_user, LoginManager  # Importa LoginManager
from flask import render_template, flash
from app.models.tables import User
from app.models.forms import LoginForm

# Configuração do LoginManager
login_manager = LoginManager()
login_manager.init_app(app)  # Inicializa o LoginManager com o app

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))  # Função para carregar o usuário pelo ID

login_manager.login_view = 'login'  # Define a rota de login padrão

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST', 'GET'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            flash('Logged in')
        else:
            flash('Invalid Login')
    else:
        print(form.errors)
    return render_template('login.html', form=form)

@app.route('/teste/<info>')
@app.route('/teste', defaults={'info': None})
def teste(info):
    r = User.query.filter_by(username='faelson').first()
    db.session.delete(r)
    db.session.commit()
    return 'OK'







# @app.route("/index/<user>")
# @app.route("/", defaults = {'user': None})
# def index(user):
#     return render_template('index.html', user = user)
