
n = int(input("enter a number"))
for i in range(1, n + 1):
    for j in range(n - i):
        print(' ', end='')
    for k in range(i):
        print('*', end='')
    print()