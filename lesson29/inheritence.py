
class person( object ):

    def __init__(self, name, idnumber):
        self.name = name
        self.idnumber = idnumber

    def display(self):
        print(self.name)
        print(self.idnumber)

class employee( person ):
    def __init__(self, name, idnumber, salary, post):
        self.salary  = salary
        self.post = post


        person.__init__(self, name, idnumber)

obj = employee("laksh", "7977000", "3,00,000", "senior architect")

print(obj.display())
