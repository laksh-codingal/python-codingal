

numbers1 = [1, 2, 3]

numbers2 = [4, 5, 6]

addition = map(lambda x, y: x + y, numbers1, numbers2)
print("the addition of two lists is:- ")
print(list(addition))


numbers = [1, 2, 3, 4, 5]

def sq(n):
    return n*n

square = list(map(sq, numbers))
print("square of numbers in list is:- ")
print(square)
