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