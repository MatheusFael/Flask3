from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import os
from flask_login import LoginManager


app = Flask(__name__)

# Carregando as configurações do arquivo config.py na raiz do projeto
app.config.from_object('config')

# configurando LoginManager
lm = LoginManager(app)

# Inicializando o banco de dados
db = SQLAlchemy(app)

# Configurando Flask-Migrate
migrate = Migrate(app, db)

# Importando as rotas
from app.models import tables
from app.controllers import default
