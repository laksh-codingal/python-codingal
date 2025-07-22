
class rectangle():

    def __init__(self, lenght, width):
        self.lenght = lenght
        self.width = width

    def calculate_area(self):
        return self.lenght * self.width
    
area = rectangle(77, 88)

print(area.calculate_area())

