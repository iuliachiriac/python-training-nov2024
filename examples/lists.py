l = [0, 1, 1, 2, 3, 6, 7, 8, 10, 100]

# There is no need to capture the result of reverse (or other list methods that
# change the list), because it will always return None (and change the list in
# place)
# var = l.reverse()
# print(var)  # None

l.reverse()
print(l)
