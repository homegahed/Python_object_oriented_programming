# check class types and instances

class book:
    def __init__(self, title):
        self.title = title


class newspaper:
    def __init__(self, name):
        self.name = name



# Create instances of classes

b1 = book('The Catcher In the Rye')
b2 = book('The Grapes Of Wrath')

n1 = newspaper('The Washington Post')
n2 = newspaper('The New York Times')



# use type() to inspect the object type

print(type(b1))
print(type(n1))


# Compare two types together

print('==' * 20)
print(type(b1) == type(b2))

print('==' * 20)
print(type(b1) == type(n1))



# use isinstance to compare specific instance to a known type

print('==' * 20)
print(isinstance(b1, book))

print('==' * 20)
print(isinstance(n1, newspaper))

print('==' * 20)
print(isinstance(n1, book))


print('==' * 20)
print(isinstance(n1, object))