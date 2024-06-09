from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']


        if username == 'admin' and password == 'password':
            return 'Login successful!'
        else:
            return 'Invalid username or password'


    return render_template('login.html')

@app.route('/greet', methods=['POST'])
def greet():
    name = request.form['name']
    return f'Hello, {name}!'

if __name__ == '__main__':
    app.run()