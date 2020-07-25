from flask import *
import sqlite3,requests,json
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html',dashboard='active',up='Dashboard',URL=json.loads(requests.get('http://127.0.0.1:4040/api/tunnels').text)['tunnels'][0]['public_url']+'/data')
@app.route('/user')
def user():
    return render_template('index.html',profile='active',up='User Profile')
@app.route('/author')
def author():
    return render_template('index.html',author='active',up='Author')
@app.route('/data')
def data():
    x=sqlite3.connect('../data.db')
    db=x.cursor()
    n=0
    for i in db.execute('SELECT * FROM CHAT'):
        n+=i[1]
    return str(n)
app.run(debug=True)