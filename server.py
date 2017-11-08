from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')
@app.route('/')
def index():
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    return render_template('index.html', all_friends=friends)
@app.route('/friends', methods=['POST'])
def create():
	query = "INSERT INTO friends(name,age,friend_date,year,created_at,updated_at) VALUES(:name,:age,:friend_date,:year,NOW(),NOW())"
	data = {
		'name': request.form['name'],
		'age': request.form['age'],
		'friend_date': request.form['friend_date'],
		'year': request.form['year']
	}
	mysql.query_db(query, data)
	return redirect('/')
app.run(debug=True)