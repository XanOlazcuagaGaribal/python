from flask import Flask
from flask import request, render_template, jsonify
import json
import os

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

@app.route("/api/book/<path:titre>")
def return_titre(titre):
    books = library()
    for book in books:
        if book['titre'] == titre:
            selected = book
    return selected    

def load_books():
    SITE_ROOT = os.path.realpath(os.path.dirname(__file__))
    json_url = os.path.join(SITE_ROOT, "json", "books.json")
    return json.load(open(json_url))

@app.route("/api/booksfile", methods = ['GET'])
def books_file():
    books = load_books()
    return jsonify(books)

@app.route("/api/booksfile/<int:book_id>",methods = ['GET'])
def return_file_id(book_id=None):
    books = load_books()
    for book in books:
        if book['pageCount'] == int(book_id):
            selected = book
    return selected    

@app.route("/api/booksfile/<path:titre>")
def return_file_titre(titre):
    books = load_books()
    for book in books:
        if book['title'] == titre:
            selected = book
    return selected

if __name__ == '__main__':
    app.run(debug=True)