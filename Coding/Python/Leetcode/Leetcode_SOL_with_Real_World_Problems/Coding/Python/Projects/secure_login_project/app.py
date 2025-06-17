from flask import Flask, render_template, request, redirect, make_response
import hashlib
import datetime

app = Flask(__name__)
app.secret_key = "very_secure_key_123"  # for CSRF token

# Dummy login data
USERS = {
    "usman": hashlib.sha256("password123".encode()).hexdigest()
}

@app.route('/')
def home():
    return render_template("login.html")

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = hashlib.sha256(request.form['password'].encode()).hexdigest()

    if username in USERS and USERS[username] == password:
        resp = make_response(redirect('/dashboard'))
        expires = datetime.datetime.now() + datetime.timedelta(minutes=30)

        resp.set_cookie("session_id", "secure_token_123456", 
                        expires=expires, 
                        httponly=False, 
                        secure=False, 
                        samesite='Strict')

        return resp
    else:
        return "Invalid Credentials", 401

@app.route('/dashboard')
def dashboard():
    session_id = request.cookies.get("session_id")
    if session_id == "secure_token_123456":
        return render_template("dashboard.html")
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    resp = make_response(redirect('/'))
    resp.set_cookie("session_id", "", expires=0)
    return resp

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # HTTPS for Secure cookie
