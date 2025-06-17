from flask import Flask, request, render_template, redirect, make_response
from markupsafe import escape  # for secure version

app = Flask(__name__)

comments = []  # In-memory comment store

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        resp = make_response(redirect('/comment'))
        # Set secure cookie
        resp.set_cookie('username', username, 
                        httponly=True, 
                        secure=True, 
                        samesite='Strict', 
                        max_age=300)
        return resp
    return render_template('login.html')

@app.route('/comment', methods=['GET', 'POST'])
def comment():
    if request.method == 'POST':
        comment_text = request.form['comment']
        # INSECURE: direct input (XSS possible)
        comments.append(comment_text)
        return redirect('/comment')
    return render_template("comment.html", comments=comments)

@app.route('/comment_secure', methods=['GET', 'POST'])
def comment_secure():
    if request.method == 'POST':
        comment_text = escape(request.form['comment'])  # secure escape
        comments.append(comment_text)
        return redirect('/comment_secure')
    return render_template("comment.html", comments=comments)

@app.route('/xss_demo')
def xss_demo():
    return render_template('xss_demo.html')

if __name__ == '__main__':
    app.run(ssl_context='adhoc')  # HTTPS for Secure Cookie
