digits = [1, 2, 3]
output = [(x, y) for x in digits for y in digits if x != y]
print(output)
# [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
