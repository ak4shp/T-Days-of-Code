class Book:
    def __init__(self, pages:int, price:int, author:str, id:int, title:str) -> None:
        self.pages = pages
        self.price = price
        self.author = author
        self.id = id
        self.title = title


class BookStore:
    def __init__(self, bookStoreName:str, BookList:list) -> None:
        self.bookStoreName = bookStoreName
        self.BookList = BookList

    def findMinimumBookByid(self):
        min_b_id = float('inf')
        idx = 0
        for i, book in enumerate(self.BookList):
            print(book.id)
            b_id = book.id
            if b_id <= min_b_id:
                min_b_id = b_id
                idx = i

        return self.BookList[idx] or None

    def sortBookByid(self):
        books = []
        for book in self.BookList:
            b_id = book.id
            books.append(b_id)
        books.sort()
        return books or None

#* Driver
def main():
    n = int(input())
    books = []
    while n:
        n -= 1
        pages = int(input())
        price = int(input())
        author = input()
        id = int(input())
        title = input()

        current_book = Book(pages, price, author, id, title)
        books.append(current_book)

    new_book_shop = BookStore("New Book Shop", books)

    min_book = new_book_shop.findMinimumBookByid()
    sorted_ids = new_book_shop.sortBookByid()
    print("output: ")
    if min_book == None:
        print("No Data Found")
    else:
        print(min_book.pages)
        print(min_book.price)
        print(min_book.author)
        print(min_book.id)
        print(min_book.title)

    if sorted_ids == None:
        print("No Data Found")
    else:
        for ids in sorted_ids:
            print(ids)

main()



