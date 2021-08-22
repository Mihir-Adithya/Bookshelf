class Books:
    def __init__(self, name, author, price, release):
        self.book_name = name
        self.book_author = author
        self.book_price = price
        self.book_release = release
     
    def add_Books(self):
        print("Name: "+ self.book_name)
        print("Author: "+self.book_author)
        print("Price of Book: "+ self.book_price)
        print("Book Release: "+ self.book_release)
        print("Book Added!")

book1 = Books("Harry Potter and the Sorcerer's Stone","JK Rowling","355","26 June 1997")
book1.add_Books()

book2 = Books("A Passage to India","E.M.Forster","140","4 June 1924",)
book2.add_Books()
