# Create a class Publisher (name). Derive class Book (title, author) from Publisher.
# Derive class Python (price, no_of_pages) from Book. Write a program that
# displays information about a Python book. Use base class constructor invocation
# and method overriding.

class Publisher:
    def __init__(self):
        self.name = 'Anlin'

    def display(self):
        print('Name:', self.name)

class Book(Publisher):
    def __init__(self):
        self.title = 'My Book'
        self.author = 'anlinalbert'

    def display(self):
        super().__init__()
        super().display()
        print('Title:', self.title, '\nAuthor:', self.author)

class Python(Book):
    def __init__(self):
        self.price = '300'
        self.no_of_pages = '100'
    
    def display(self):
        super().__init__()
        super().display()
        print('Price:', self.price, '\nNo.of pages:', self.no_of_pages)

b = Python()
print('Book details are:\n')
b.display()