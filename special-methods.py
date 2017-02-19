class Book(object):

    def __init__(self,title,author,pages):
        print("A book has been created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, Author: %s, Pages: %s" %(self.title,self.author,self.pages)


b = Book("Learn Python","James",100)

print ("Book Details:",b)

