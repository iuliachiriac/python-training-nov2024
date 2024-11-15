def grep(text, file):
    lines_matching = []
    with open(file) as f:
        for line in f:
            if text in line:
                lines_matching.append(line)
    return lines_matching


if __name__ == "__main__":
    output = grep("def", "functions.py")
    print(output)

    with open("legb.py", "r") as f:
        for line in f:
            print(line, end="")

    # file is automatically closed after with block
    print(f.closed)

    with open("out.txt", "w") as f:
        f.write("Hello\n")
        f.write("World\n")

    windows_path = r"D:\User\PyCharmProjects\new"  # raw string
