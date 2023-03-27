class Book:
    def __init__(self, book_id, book_name, author) -> None:
        self.book_id = book_id
        self.book_name = book_name
        self.author = author

class Library:
    def __init__(self, book_list:list, address:dict) -> None:
        self.books = book_list
        self.address = address

    def find_book_count_author_wise(self, author_q):
        books_count = {}
        for a_book in self.books:
            an_author = a_book.author
            if an_author not in books_count.keys():
                books_count[an_author] = 1
            else:
                books_count[an_author] += 1
        return books_count[author_q]


def get_books_by_city(city, library_list): #library is a list of objects
    books_by_city = []
    for lib in library_list:
        temp_books = []
        if lib.address["city"].lower() == city.lower():
            for a_book in lib.books:
                temp_books.append(a_book.book_name)
        temp_books.sort(reverse=True)
        books_by_city.extend(temp_books)

    if len(books_by_city) == 0:
        return None
    return books_by_city


#----- main -----#
libraries = []

t = int(input())
for _ in range(t):
    book_ct = int(input())
    books_list = []
    address = {}

    for _ in range(book_ct):
        book_id = int(input())
        book_name = input()
        author = input().upper()

        new_book = Book(book_id, book_name, author)
        books_list.append(new_book)

    address["street"] = input()
    address["area"] = input()
    address["city"] = input()
    address["state"] = input()
    address["zip"] = int(input())

    a_library = Library(books_list, address)
    libraries.append(a_library)

query_city = input()

#----- outputs -----# 
lib_1 = libraries[0]
author_1 = lib_1.books[0].author
ct = lib_1.find_book_count_author_wise(author_1)
print(author_1, ct)

city_books = get_books_by_city(query_city, libraries)
if city_books:
  print(city_books)
else:
  print("No Book Found")