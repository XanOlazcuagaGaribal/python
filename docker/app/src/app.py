from flask import Flask,request, render_template, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello"
    #return render_template("base.html")

if __name__ == "__main__":
   app.run(debug=True)