from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "<html><body><h1>this Expense Tracker.<h1></body></html>"

if __name__ == "__main__":
    app.run()
