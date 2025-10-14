
class A:
    def __init__(self,a):
        self.a=a

    def __lt__(self,other):
        if self.a < other.a:
            return "obj 1 has value less than obj2"
        else:
            return "obj2 has value less than obj1"
        
    def __eq__(self,other):
        if self.a == other.a:
            return "both are equal"
        else:
            return "both are not equal"

obj1 = A(2)
obj2 = A(3)
print(obj1<obj2)
print(obj1==obj2)

