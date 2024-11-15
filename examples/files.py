with open("legb.py", "r") as f:
    for line in f:
        print(line, end="")

# file is automatically closed after with block
print(f.closed)

with open("out.txt", "w") as f:
    f.write("Hello\n")
    f.write("World\n")
