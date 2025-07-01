
lists_items = int(input("give a set of numbers not seperated by comma eg:- '123854824' :- "))


my_list = []

my_list.append(lists_items)

start_range = int(input("enter the starting range:- "))

end_range = int(input("enter the end range:- "))

odd_list = []

even_list = []

for num in range(start_range, end_range + 1):
    if num%2 == 0:
        even_list.append(num)
    else:
        odd_list.append(num)

print("the odd numbers are:- ", odd_list)
print("the even numbers are:- ", even_list)
