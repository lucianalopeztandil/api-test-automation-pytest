isbn = "qaautomation4"

def add_book_payload():
    return {
        "name": "Learn Appium Automation with Java",
        "isbn": isbn,
        "aisle": "2299",
        "author": "John foe"
    }

def params_get_book():
    return {'ID':isbn}

def delete_book_payload(bookId):
    return {
        "ID" : bookId
    }