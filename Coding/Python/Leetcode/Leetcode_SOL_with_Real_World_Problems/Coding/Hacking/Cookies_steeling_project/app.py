from flask import Flask, render_template, request, make_response, redirect

app = Flask(__name__)

# In-memory list to store comments
comments = []

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == 'admin' and password == 'password':
            resp = make_response('Login successful')
            # Vulnerable: Cookie set without HttpOnly or Secure flags
            resp.set_cookie('session_id', '12345')
            return resp
        else:
            return 'Invalid credentials'
    else:
        return render_template('login.html')

@app.route('/comments', methods=['GET', 'POST'])
def comments_vulnerable():
    if request.method == 'POST':
        comment = request.form['comment']
        comments.append(comment)
        return redirect('/comments')
    else:
        return render_template('comments.html', comments=comments)

@app.route('/comments_secure', methods=['GET', 'POST'])
def comments_secure():
    if request.method == 'POST':
        comment = request.form['comment']
        comments.append(comment)
        return redirect('/comments_secure')
    else:
        return render_template('comments_secure.html', comments=comments)

@app.route('/explain_xss')
def explain_xss():
    return render_template('explain_xss.html')

@app.route('/attacker')
def attacker():
    cookie = request.args.get('cookie', '')
    if cookie:
        message = f"Cookie received: {cookie}"
    else:
        message = "No cookie received"
    return message

if __name__ == '__main__':
    app.run(debug=True)