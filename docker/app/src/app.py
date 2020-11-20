from flask import Flask,request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello"

@app.route('/index')
def index():
    name="Xan"
    return render_template('base.html',title="Welcome",name=name)

if __name__ == "__main__":
   app.run(host='0.0.0.0')