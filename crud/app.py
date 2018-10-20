from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key="flash message"
app.config["MYSQL_HOST"]='localhost'
app.config["MYSQL_USER"]='root'
app.config["MYSQL_PASSWORD"]=''
app.config["MYSQL_DB"]='crud'

mysql=MySQL(app)

@app.route('/')
def index():
	cur=mysql.connection.cursor()
	cur.execute("SELECT * FROM STUDENTS")
	data=cur.fetchall()
	cur.close()
	return render_template('index.html',students=data)

@app.route("/insert",methods=['POST'])
def insert():
	if request.method=="POST":
		flash("Data inserted successfully")
		regno=request.form["regno"]
		name=request.form["name"]
		email=request.form["email"]
		phone=request.form["phone"]

		cur=mysql.connection.cursor()
		cur.execute("INSERT INTO students(regno,name,email,phone) VALUES(%s,%s,%s,%s)",(regno,name,email,phone))
		mysql.connection.commit()
		return redirect(url_for("index"))
@app.route("/update",methods=["POST","GET"])
def update():
	if request.method=="POST":
		regno=request.form["regno"]
		name=request.form["name"]
		email=request.form["email"]
		phone=request.form["phone"]
		cur=mysql.connection.cursor()
		cur.execute("UPDATE students SET name=%s,email=%s,phone=%s WHERE regno=%s",(name,email,phone,regno))
		flash("Data updated successfully")
		mysql.connection.commit()
		return redirect(url_for("index"))

@app.route('/delete/<string:regno_data>',methods=["POST","GET"])
def delete(regno_data):
	cur=mysql.connection.cursor()
	cur.execute("DELETE FROM students WHERE regno=%s",[regno_data])
	flash("Data updated successfully")
	mysql.connection.commit()
	return redirect(url_for("index"))
if __name__ == '__main__':
	app.run(debug=True)

