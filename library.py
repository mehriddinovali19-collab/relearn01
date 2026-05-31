class Book:
    def __init__(self, name, author, year):
        self.name = name
        self.author = author
        self.year = year
    

    def show_data(self):
        print(f"Name of the book: {self.name}")
        print(f"Author of the book: {self.author}")
        print(f"Year of the book: {self.year}")



class Library:
    def __init__(self):
        self.books = []

    
    def add_book(self, book):
        self.books.append(book)
        print(f"{book.name} qo'shildi!")


    def all_books(self):
        for kitob in self.books:
            kitob.show_data()
    

    def search_book(self, name):
        for book in self.books:
            if book.name.lower() == name:
                book.show_data()
                return 
        print("Book not founded!")


kitob1 = Book("O'tkan kunlar", "Abdulla Qodiriy", 1925)
kitob2 = Book("Mehrobdan chayon", "Abdulla Qodiriy", 1929)
kitob3 = Book("Kecha va kunduz", "Cho'lpon", 1936)
kitob4 = Book("Sarob", "Abdulla Qahhor", 1943)
kitob5 = Book("Qo'shchinor chiroqlari", "Odil Yoqubov", 1958)
    
kitobxona = Library()

kitobxona.add_book(kitob1)
kitobxona.add_book(kitob2)
kitobxona.add_book(kitob3)
kitobxona.add_book(kitob4)
kitobxona.add_book(kitob5)
print("-----------------all books ------------------------")
kitobxona.all_books()
print("--------------Searched Book---------------")
kitobxona.search_book("sarob")