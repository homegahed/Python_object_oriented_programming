# Using composition to build complex objects


from tkinter import PAGES


class Book:
    def __init__(self, title, price, author=None):

        self.title = title
        self.price = price


        self.author = author

        #self.authorfname = authorfname    ## not needed and will build replaced by class author which hold a tuple of author first name and last name 
        #self.authorlname = authorlname

        self.chapters = []


    def addchapter(self, chapter):
        self.chapters.append(chapter)


    def getbookpagecount(self):
        result = 0
        for ch in self.chapters:
            result = result + ch.pagecounts
        return result



# build class author and used in composition with class book
class author:
    def __init__(self, fname, lname):
        self.fname = fname
        self.lname = lname

    def __str__(self):
        return f"{self.fname} {self.lname}"


class chapter:
    def __init__(self, name, pagecounts):
        self.name = name
        self.pagecounts = pagecounts



a = author("Leo", "Tolstoy")

b1 = Book("War and Peice", 39.0, a)
b1.addchapter(chapter("Chapter 1", 125))
b1.addchapter(chapter("Chapter 2", 97))
b1.addchapter(chapter("Chapter 3", 143))


print(b1.title)
print(b1.price)

print(b1.author.fname)
print(b1.author.lname)

print(b1.getbookpagecount())



print(b1.author)