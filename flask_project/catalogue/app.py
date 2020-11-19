from flask import Flask
from flask import request, render_template, jsonify
import json

app = Flask(__name__)

books=[
  {
      'id':1,
      'titre' : 'un titre',
  },
  {
      'id':2,
      'titre': 'un autre titre random',
  }
]

@app.route("/")
def index():
 return "Hello DC!"

@app.route("/api/books", methods = ['GET'])
def books():
    return jsonify(book)

@app.route("/api/book/<int:id>",methods = ['GET'])
def return_id(id):
    results=[]
    for book in books:
        if book['id'] == id:
            results.append(book)
            return jsonify(results)
        else:
            return "No books found"
    

#Ne marche pas
@app.route("/api/book/<path:titre>")
def return_titre(titre):
    results=[]
    for book in books:
        if book['id'] == id:
            results.append(book)
            return jsonify(results)
        else:
            return "No books found"
            
    #return jsonify(book['title'])

@app.route("/api/books/titre")
def hello(name):
    return "Hello %s" % name

if __name__ == '__main__':
    app.run(debug=True)