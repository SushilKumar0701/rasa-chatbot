from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def landing():
    return render_template('index.html')

@app.route("/login")
def login():
    return render_template('login.html')

@app.route("/gtn")
def gtn():
    return render_template('gtn.html')

if __name__ == "__main__":
    app.run(debug=True)