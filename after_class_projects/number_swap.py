
a = int(input("Enter first number:- "))
b = int(input("Enter second number:- "))
c = int(input("Enter third number:- "))

print("\nBefore swapping:")
print(f"a = {a}, b = {b}, c = {c}")

# Swapping in circular manner: a -> b, b -> c, c -> a
a, b, c = c, a, b

print("\nAfter swapping:")
print(f"a = {a}, b = {b}, c = {c}")