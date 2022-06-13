# Understanding class inheritance 


# Defining new base class for removing duplications 

class Publications:
    def __init__(self, title, price):
        self.title = title
        self.price = price


class Periodical(Publications):
    def __init__(self, title, price, period, publisher):
        super().__init__(title, price)
        self.period = period
        self.publisher = publisher



class Book(Publications):
    def __init__(self, title, author, pages, price):

        super().__init__(title, price)
        #self.title = title # Not need anymore as the attribute is inherited from publications class
        self.author = author
        self.pages = pages
        #self.price = price # Not need anymore as the attribute is inherited from publications class

class Magazine(Periodical):
    def __init__(self, title, publisher, price, period):

        super().__init__(self, title, price, period, publisher)
        #self.title = title
        #self.publisher = publisher
        #self.price = price
        #self.period = period


class Newspaper(Periodical):
    def __init__(self, title, publisher, price, period):
        super().__init__(self, title, price, period, publisher)
        
        #self.title = title
        #self.Publisher = Publisher
        #self.price = price
        #self.period = period


b1 = Book("Brave New World", "Aldous Huxley", 311, 29.0)
n1 = Newspaper("NY Times", "New York Times Company", 6.0, "Daily")
m1 = Magazine("Scientific American", "Springer Nature", 5.99, "Monthly")


print(b1.author)
print(n1.Publisher)
print(b1.price, m1.price, n1.price)