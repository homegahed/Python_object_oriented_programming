# Understanding class inheritance 

class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price

class Magazine:
    def __init__(self, title, Publisher, price, period):
        self.title = title
        self.Publisher = Publisher
        self.price = price
        self.period = period


class Newspaper:
    def __init__(self, title, Publisher, price, period):
        self.title = title
        self.Publisher = Publisher
        self.price = price
        self.period = period


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")


print(b1)
print(b1.title)