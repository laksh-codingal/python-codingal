
from abc import ABC,abstractmethod

class myclass(ABC):


    def print(self,x):
        print("passed value is", x)


    @abstractmethod
    def task(self):
        print("we are inside myclass abstract method task")

    
class test(myclass):
    def task(self):
        print("we are inside test class")

test_obj = test()
test_obj.task()
test_obj.print(100)

