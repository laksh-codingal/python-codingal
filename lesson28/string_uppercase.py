

class io:
    def __init__(self):
        self.str1 = " "

    
    def get_string(self):
        self.str1 = input("enter a string:- ")


    def print_string(self):
        print("the result is:- ", self.str1.upper())

    
str1 = io()


str1.get_string()
str1.print_string()

