
def value_frequencies(input_dict):
    freq = {}
    for value in input_dict.values():
        if value in freq:
            freq[value] += 1
        else:
            freq[value] = 1
    return freq


my_dict = {
    "a": 10,
    "b": 20,
    "c": 10,
    "d": 30,
    "e": 20,
    "f": 10
}

result = value_frequencies(my_dict)

print("Value Frequencies:")
for val, count in result.items():
    print(f"{val} appears {count} times")
