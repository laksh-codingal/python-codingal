

x = frozenset([1, 2, 3 ,4, 5, 6, 7])

y = frozenset([1, 6, 7, 0, 4554, 666])

print(x.isdisjoint(y))

print(x.difference(y))

print(x | y)

