
from abc import ABC,abstractmethod

class animal(ABC):
     def move(self):
          pass
     
class human(animal):
     def move(self):
          print("i can walk")

class snake(animal):
     def move(self):
          print("i can crawl")

class dog(animal):
     def move(self):
          print("i can bark")

class lion(animal):
     def move(self):
          print("i can roar")

a = human()
a.move()

b = snake()
b.move()

c=dog()
c.move()

d = lion()
d.move()
