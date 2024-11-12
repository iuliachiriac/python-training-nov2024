print("while loop:")
i = 0

while i < 5:
    print(i)
    i += 1  # i = i + 1

print("\nfor loop on a string:")

text = "hello"
for char in text:
    print(char)

print("\nfor loop on a range object:")

for i in range(3, 7):
    print(i)


print("while loop with break:")
i = 0

while i < 5:
    if i >= 3:
        break
    print(i)
    i += 1

print("while loop with continue:")
i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
