# Using class-level and static methods



class book:

    # todo: Properties defined at the class level are shared by all instances

        #Creating class attribute
    BOOK_TYPES = ('HARDCOVER', 'PAPERPACK', 'EBOOK')

    # todo: double-underscore properties are hideen from other classes

    __booklist = None
    # todo: create a class method
    @classmethod
    def getbooktypes (cls):
        return cls.BOOK_TYPES


    # todo: create a static method
    @staticmethod

    def getbooklist():
        if book.__booklist == None:
            book.__booklist =[]
        return book.__booklist


    # instance methods receive a specific object instance  as an argument 
    # and operate on data specific to that object instance


    def setTitle(self, newtitle):
        self.title = newtitle
        
    def __init__(self, title, booktype):
        self.title = title

        if (not booktype in book.BOOK_TYPES):
            raise ValueError (f'{booktype} is not a valid book type')
        else:
            self.booktype = booktype




b1 = book('book1', 'HARDCOVER')
b2 = book('book1', 'PAPERPACK')

# to access class attributes
print('book types:', book.getbooktypes())



# use of static methods to access 

thebooks = book.getbooklist()

thebooks.append(b1)
thebooks.append(b2)

print('==' * 20)
print(thebooks)
print('==' * 20)


print(b1)
print(b1.title)






