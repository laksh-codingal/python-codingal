
class India():

    def capital(self):
        print("capital of india is delhi")

    def lan(self):
        print("the most spoken language is hindi and tamil")

    def type(self):
        print("india is a devoloping country")

class USA():

    def capital(self):
        print("capital of usa is washington d.c")

    def lan(self):
        print("the most spoken language is english")

    def type(self):
        print("Usa is a devoloped country")

obj_ind = India()
obj_usa = USA()

for x in (obj_ind, obj_usa):
    x.capital()
    x.lan()
    x.type()


    
