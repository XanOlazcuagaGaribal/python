from flask import Flask
from flask import request, render_template

app = Flask(__name__)
 
@app.route("/")
def index():
 return "Hello my app!"

@app.route("/index/<name>")
def hello(name):
    return "Hello %s" % name

@app.route("/template/<name>")
def template(name):
    return render_template("template.html", name=name)

if __name__ == '__main__':
    app.run(debug=True)