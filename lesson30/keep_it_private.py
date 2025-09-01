
class hello:

    __privatevariable = 77

    def __privatemethod(self):
        print("i am in the class hello")

    def hi(self):
        print("private variable is", hello.__privatevariable)

obj = hello()
obj.hi()
obj.__privatemethod()
