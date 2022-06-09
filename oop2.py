
# Create Basic Class
class book:
    def __init__(self, title, author, pages, price):
        self.title = title

        # Add properties 
        self.author = author
        self.pages = pages
        self.price = price  

        self.__secert_book = 'This is a secert book'


    # Create instance of a method
    def getprice(self):

        if hasattr (self, '_discount'):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def set_discount(self, discount_amount):
        self._discount = discount_amount

# Create instance of a class

b1 = book('Brave New world', 'Leo Tolstoy', 1225, 39.95)
b2 = book('War and peace', 'JD Salinger', 234, 29.95)


# print class and property 
print(b1)
print(b1.title)


# print book price

print(f'book {b1.title} price is {b1.getprice()}')


# print book price with discount

print(f'book {b2.title} price before discount is {b2.getprice()}')
b2.set_discount(0.25)
print(f'book price after discount is {b2.getprice()}')

try:
    print(b1.__secert_book)
except:
    print(b1._book__secert_book)