important links  : https://flask-migrate.readthedocs.io/en/latest/
https://flask.palletsprojects.com/en/3.0.x/

Virtual environments


Use a virtual environment to manage the dependencies for your project, both in development and in production.

What problem does a virtual environment solve? The more Python projects you have, the more likely it is that you need to work with different versions of Python libraries, or even Python itself. Newer versions of libraries for one project can break compatibility in another project.

Virtual environments are independent groups of Python libraries, one for each project. Packages installed for one project will not affect other projects or the operating system’s packages.

Python comes bundled with the venv module to create virtual environments.

Create an environment
Create a project folder and a .venv folder within:
After you have entered in th directory

Linux:

$ python3 -m venv .venv
$ . .venv/bin/activate

Windows: 

> py -3 -m venv .venv
> .venv\Scripts\activate

Something that is very important:
pip install Flask-SQLAlchemy


Flask Migrate
pip install Flask-Migrate
pip install Flask-script
$ flask db init
$ flask db migrate -m "Initial migration."
$ flask db upgrade

Para fazer o Login: 
pip install -U Flask-WTF

