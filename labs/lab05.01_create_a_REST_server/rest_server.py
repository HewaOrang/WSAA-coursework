# This program creates a basic REST server using Flask
# Author: Hewa Orang

from flask import Flask, url_for, request, redirect, abort

app = Flask(__name__, static_url_path='', static_folder='staticpages')

@app.route('/')
def index():
    return "Hello"

@app.route('/books', methods=['GET'])
def getall():
    return "get all"

@app.route('/books/<int:id>', methods=['GET'])
def findbyid(id):
    return "find by id"

# cretate
@app.route('/books', methods=['POST'])
def create():
    # read json form the body
    jsonstring = request.json

    return f"create {jsonstring}"

# update
@app.route('/books/<int:id>', methods=['PUT'])
def update(id):
    jsonstring = request.json
    return f"update {id} {jsonstring}"

# delete
@app.route('/books/<int:id>', methods=['DELETE'])
def delete(id):
    return f"delete {id}"


if __name__ == "__main__":
    app.run(debug=True)