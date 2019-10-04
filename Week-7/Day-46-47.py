# Python Week-7 Day-46-47 
# Seventh Week Challenge


print("\n\n")
class library:
    def __init__(self, book, shelf):
        self.book = book
        self.shelf = shelf

xx = library( 300, 45)
print ("WE have",xx.book, "Book",
 "In Our library","Spread over",
  xx.shelf, "shelf")
print(" ---- ")

class science_section(library):
    def __init__(self, book, shelf, name ):
        super().__init__(book, shelf)
        self.name = name

    def printinfo(self):
        print("Number Of Books is", self.book,
         "Number Of Shelf", self.shelf,
          "And We Have Section For",self.name)

y = science_section(20, 4, "Physics books")
y.printinfo()