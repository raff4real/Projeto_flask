from flask import Flask

app = Flask("Exercicio")

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"