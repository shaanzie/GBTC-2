from flask import Flask, render_template,Response, request
from flask_mysqldb import MySQL
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'Voting'

mysql = MySQL(app)

@app.route('/login', methods = ['POST'])
def index():
    print(request.json)
    cur = mysql.connection.cursor()
    cur.execute("SELECT count(*) FROM Voting WHERE UID = ID")
    if(cur):
        return Response(status=201)

if __name__ == '__main__':
    app.run()