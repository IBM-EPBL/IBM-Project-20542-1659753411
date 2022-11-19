from flask import Flask, request,render_template,redirect, url_for, session
import ibm_db
import re

app=Flask(__name__)
app.secret_key='a'
 
# conn = ibm_db.connect("DATABASE=bludb;HOSTNAME=ba99a9e6-d59e-4883-8fc0-d6a8c9f7a08f.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=31321;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=nnr87238;PWD=PUmIqXYukgkiGmGq", "", "")
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    global userid
    msg = ''
    
    if request.method == 'POST':
        username = request.form['email']
        password = request.form['password']
        sql = "SELECT * FROM users WHERE username =? AND password=?"
        # stmt = ibm_db.prepare(conn, sql)
        # ibm_db.bind_param(stmt, 1, username)
        # ibm_db.bind_param(stmt, 2, password)
        # ibm_db.execute(stmt)
        # account = ibm_db.fetch_assoc(stmt)
        # print(account)

        if False:
            session['loggedin'] = True
            session['id'] = account['USERNAME']
            userid = account['USERNAME']
            session['username'] = account['USERNAME']

            msg = 'Logged in successfully !'
            return render_template('dashboard.html', msg=msg)
        else:
            msg = 'Incorrect username / password !'+username
            return render_template('home.html', msg=msg)

if __name__ == "__main__":
    app.run(debug=True)