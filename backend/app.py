from flask import Flask, render_template, request, redirect, url_for
from auth import authenticate_user, register_user

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        dob = request.form['dob']
        email = request.form['email']
        username = request.form['username']
        password = request.form['password']
        confirm_password = request.form['confirm_password']

        if password != confirm_password:
            return "Passwords do not match. ❌ Please try again."

        register_user(first_name, last_name, dob, email, username, password)
        return redirect(url_for('home'))

    return render_template('signup.html')

# LOGIN Route (POST method)
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if authenticate_user(username, password):
            return redirect(url_for('dashboard'))
        else:
            return "Invalid username or password. ❌ Try again."

    # If GET request (user clicks Login button)
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
