# This program wites a module to intercat with API.
# By: Hewa Orang

import requests

URL = "http://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(URL)
    return response.json()

def readbook(book_id):
    geturl = URL + "/" + str(book_id)
    response = requests.get(geturl)
    return response.json()

def createbook(book):
    response = requests.post(URL, json=book)
    return response.json()

def updatebook(book_id, book):
    puturl = URL + "/" + str(book_id)
    response = requests.put(puturl, json=book)
    return response.json()

def deletebook(book_id):
    deleteurl = URL + "/" + str(book_id)
    response = requests.delete(deleteurl)
    return response.json()

if __name__ == "__main__":
    print("Reading all books...")
    print(readbooks())

    print("\nReading one book...")
    print(readbook(1712))

    print("\nCreating a book...")
    new_book = {
        "title": "Lab 03 Test Book",
        "author": "Your Name",
        "price": 25
    }
    created_book = createbook(new_book)
    print(created_book)

    created_id = created_book["id"]

    print("\nUpdating the new book...")
    updated_book = {
        "title": "Lab 03 Updated Book",
        "author": "Your Name",
        "price": 30
    }
    print(updatebook(created_id, updated_book))

    print("\nDeleting the new book...")
    print(deletebook(created_id))


