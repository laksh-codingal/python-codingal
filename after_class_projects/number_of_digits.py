
num = int(input("Enter a number: "))

if num < 0:
    num = -num

count = 0
while num > 0:
    count += 1
    num = num // 10

print("Total digits:", count)


