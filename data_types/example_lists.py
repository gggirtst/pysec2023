numbers = [0, 1, 2, 3, 4]
strings = ["one", "two", "three"]

print(numbers)
print(strings)

combined = numbers + strings

print(combined)

extra_combined = [0, "text", [0,1,2], {"kris": "taps"}]
print(extra_combined)

print("size of extra_combined is: {}".format(len(extra_combined)))

extra_combined.append("another string")
print(extra_combined)

extra_combined.extend(strings)
print(extra_combined)





