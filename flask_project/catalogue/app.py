from flask import Flask
from flask import request, render_template, jsonify
import json

app = Flask(__name__)

def library():
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
    return books

@app.route("/")
def index():
 return "Hello DC!"

@app.route("/api/books", methods = ['GET'])
def books_liste():
    books = library()
    return jsonify(books)

@app.route("/api/book/<int:book_id>",methods = ['GET'])
def return_id(book_id=None):
    books = library()
    for book in books:
        if book['id'] == int(book_id):
            selected = book
    return selected    

#Ne marche pas
@app.route("/api/book/<path:titre>")
def return_titre(titre):
    books = library()
    for book in books:
        if book['titre'] == titre:
            selected = book
    return selected    

@app.route("/api/books/titre")
def hello(name):
    return "Hello %s" % name

if __name__ == '__main__':
    app.run(debug=True)