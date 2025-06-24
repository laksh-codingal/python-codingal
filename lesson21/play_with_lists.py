
list = [7,9,8,6,1,4]
print("orginal list is", list)

sum = 0

for i in list:
    sum = sum+i

avg =sum / len(list)
print(avg)

list.sort()

print(list)

print("the smallest element is ",list[0])
print("the largest element is ",list[-1])
