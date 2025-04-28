from flask import Flask, render_template, request, redirect, url_for
from auth import authenticate_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

# LOGIN Route (POST method)
@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']

    if authenticate_user(username, password):
        return "Login Successful! 🎯 (You can redirect to dashboard here)"
    else:
        return "Invalid username or password. ❌ Try again."

if __name__ == '__main__':
    app.run(debug=True)
