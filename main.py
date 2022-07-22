from app import app
from configdb import mysql
from flask import jsonify
from flask import flash, request ,render_template

@app.route("/") 
def index():
    return render_template("index.html")


@app.route('/search', methods=['GET']) 
def home():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT * FROM books")
        fetchdata = cur.fetchall()
        respone = jsonify(fetchdata)
        respone.status_code = 500
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close


@app.route('/info/1', methods=['GET'])
def home0():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT name, count FROM books WHERE id =1" )
        fetchdata = cur.fetchone()
        respone = jsonify(fetchdata)
        respone.status_code = 500
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close

@app.route('/info/2', methods=['GET'])
def home1():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT name, count FROM books WHERE id =2" )
        fetchdata = cur.fetchone()
        respone = jsonify(fetchdata)
        respone.status_code = 500
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close

@app.route('/info/3', methods=['GET'])
def home2():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT name, count FROM books WHERE id =3" )
        fetchdata = cur.fetchone()
        respone = jsonify(fetchdata)
        respone.status_code = 500
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close

@app.route('/info/4', methods=['GET'])
def home3():
    try:
        cur = mysql.connection.cursor()
        cur.execute("SELECT name, count FROM books WHERE id =4" )
        fetchdata = cur.fetchone()
        respone = jsonify(fetchdata)
        respone.status_code = 500
        return respone
    except Exception as e:
        print(e)
    finally:
        cur.close


@app.errorhandler(404)
def showMessage(error=None):
    message = {
        'status': 404,
        'message': 'Record not found: ' + request.url,
    }
    respone = jsonify(message)
    respone.status_code = 404
    return respone
        
if __name__ == "__main__":
    app.run(host='127.0.0.1' , port=5000 ,debug=True )