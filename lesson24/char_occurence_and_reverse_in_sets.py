
import array as ar

array_num = ar.array("i", [1, 7, 9, 0, 6, 9, 7, 7, 7, 7])

print("original array", str(array_num))

print("the number of occurunces of number 7 in the array", str(array_num.count(7)))

array_num.reverse()

print("reverse order of the items:- ")
print(str(array_num))

