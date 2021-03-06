from flask import Flask, render_template, request, g, jsonify, redirect, url_for, flash
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


@app.route('/', methods=['GET', 'POST'])
def login():
    global authenticated
    error = False
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = True
            flash("You know nothing Jon Snow!")
            # if error == True:
            #     flash ("You know nothing Jon Snow!")
            # else:
            #     return redirect(url_for('home'))
        else:
            authenticated = True
            return redirect(url_for('home'))
    return redirect(url_for('home'))
    # return render_template('index.html', error=error)


@app.route('/logout')
def logout():
    global authenticated
    authenticated = False
    return redirect(url_for('home'))

# Add House
@app.route('/houses', methods=['GET', 'POST'])
def houses():
    if request.method == 'GET':
        cur = get_db().cursor()
        cur.execute('select * from houses')
        rows = cur.fetchall()
        return app.response_class(json.dumps([dict(ix) for ix in rows]), mimetype='application/json')
    elif request.method == 'POST':
        try:
            name = request.form['name']
            location = request.form['location']
            price = request.form['price']
            size = request.form['size']
            description = request.form['description']
            picture = request.form['picture']

            cur = get_db().cursor()
            cur.execute("INSERT INTO houses (name, location, price, size, description, picture) "
                        "VALUES(?, ?, ?, ?, ?, ?)", (name, location, price, size, description, picture))

            get_db().commit()
            msg = "Record successfully added"
        except:
            get_db().rollback()
            msg = "error in insert operation"
        finally:
            return render_template("result.html", msg=msg)
            get_db().close()
    


#Delete House
@app.route('/houses/<int:house_id>', methods=['GET', 'POST', 'DELETE', ])
def houseById(house_id):
    if request.method == 'GET':
        cur = get_db().cursor()
        cur.execute('select * from houses where houses.id = %s' % house_id)
        house = dict(cur.fetchone())
        return render_template('houseDetails.html', house=house)
    elif request.method == 'POST':
        try:
            cur = get_db().cursor()
            cur.execute('DELETE FROM houses where houses.id = %s' % house_id)

            get_db().commit()
            msg = "Record successfully deleted"
        except:
            get_db().rollback()
            msg = "error in delete operation"
        finally:
            return render_template("result.html", msg=msg)
            get_db().close()


@app.route('/editHouse/<int:house_id>', methods=['GET', 'POST', 'DELETE', ])
def editHouse(house_id):
    if request.method == 'GET':
        cur = get_db().cursor()
        cur.execute('select * from houses where id = %s' % house_id)
        house = dict(cur.fetchone())
        return render_template('editHouse.html', house=house)
    elif request.method == 'POST':
        try:
            name = request.form['name']
            location = request.form['location']
            price = request.form['price']
            size = request.form['size']
            description = request.form['description']
            picture = request.form['picture']

            cur = get_db().cursor()
            cur.execute ("UPDATE houses SET name=?, Location=?, price=?, size=?, description=?, picture=? WHERE id=?" ,(name, location, price, size, description, picture, house_id))
            
            get_db().commit()
            msg = "Record successfully updated"
        except:
            get_db().rollback()
            msg = "Error in update operation"
        finally:
            return render_template("result.html", msg=msg)
            get_db().close()
    



@app.route('/enternew')
def new_house():
    # return redirect(url_for('addFormHome'))
    return render_template('addFormHome.html')

#edit House
 

if __name__ == '__main__':
    app.run(debug=True)
