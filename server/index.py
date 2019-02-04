from flask import Flask, render_template, request, g, jsonify, redirect, url_for
import json
import sqlite3
from flask_cors import CORS
app = Flask(__name__)

CORS(app)
app.config['SECRET_KEY'] = 'you-will-never-guess'

DATABASE = './data/database.db'

authenticated = False


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(DATABASE)
        g.db.row_factory = sqlite3.Row
    return g.db


def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('./data/schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()


@app.cli.command('initdb')
def initdb_command():
    init_db()
    print('Initialized database')


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


@app.route('/')
def home():
    print(authenticated)
    return render_template('index.html', authenticated=authenticated)


@app.route('/login', methods=['GET', 'POST'])
def login():
    global authenticated
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Invalid Credentials. Please try again.'
        else:
            authenticated = True
            return redirect(url_for('home'))
    return render_template('login.html', error=error)


@app.route('/logout')
def logout():
    global authenticated
    authenticated = False
    return redirect(url_for('home'))


@app.route('/houses')
def houses():
    cur = get_db().cursor()
    cur.execute('select * from houses')
    rows = cur.fetchall()
    return app.response_class(json.dumps([dict(ix) for ix in rows]), mimetype='application/json')
