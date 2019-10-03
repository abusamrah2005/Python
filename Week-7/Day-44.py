class car:
    def __init__(self, carbrand, carcolor):
        self.brand = carbrand
        self.color = carcolor
    def printname(self):
        print(self.cbrand, self.cyear)


class prop(car):
    def __init__(self, carbrand, carcolor, model):
        super().__init__(carbrand, carcolor)
        self.manufacturing_year = model
    
    def car_details(self):
        print("\nthis car is", self.brand, "color", self.color, 
        "and Manufacturing Year is", self.manufacturing_year)

x = prop("Chevrolet", "ًWhite", "2015")
x.car_details()


