from flask import Flask,render_template,request
from flask_mysqldb import MySQL
#import yaml
app = Flask(__name__)
# config db

app.config['MYSQL_HOST'] ='localhost'
app.config['MYSQL_USER'] ='root'
app.config['MYSQL_PASSWORD'] ='farak007'
app.config['MYSQL_DB'] ='flaskapp'
@app.route("/",methods =['GET','POST'])
def index():
    if request.method == 'POST':
        employ = request.form
        name = employ['name']
        designation = employ['designation']
        address = employ['address']
        phone = employ['phone_number']
        cur = mysql.connection.cursor()
        cur.execute("INSERT INTO users(name,designation,address,phone) VALUES(%s,%s,%s,%d)",(name,designation,address,phone))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')

app.run(debug =True)
