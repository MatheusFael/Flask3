from app import app , db
from flask_login import login_user
from flask import render_template, flash
from app.models.tables import User
from app.models.forms import LoginForm




@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')


@app.route('/login', methods = ['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():

        user = User.query.filter_by(username = form.username.data).first()
        if user and user.password == form.data.password:
            login_user(user)
           
        else:
            return 'USER NOT FOUND'
    else:
        print(form.errors)
    return render_template('login.html', form = form)

@app.route('/teste/<info>')
@app.route('/teste', defaults = {'info': None})
def teste(info):
    r = User.query.filter_by(username='faelson').first()
    db.session.delete(r)
    db.session.commit()
    return 'OK'







# @app.route("/index/<user>")
# @app.route("/", defaults = {'user': None})
# def index(user):
#     return render_template('index.html', user = user)
