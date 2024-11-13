X = 100


def func(a):
    b = 2

    # X = 999  # shadowing
    def inner(c):
        d = 22

        print("-- Inside inner --")
        print("Built-in names:", len, round, str, list, True, None)
        print("Global names:", X, func, MyClass)
        print("Enclosing names:", a, b, inner)
        print("Local names:", c, d, end="\n\n")

    inner(11)

    print("-- Inside func --")
    print("Built-in names:", len, round, str, list, True, None)
    print("Global names:", X, func, MyClass)
    print("Local names:", a, b, inner, end="\n\n")


class MyClass:
    pass


# sum = 0  # shadowing - not recommended

func(1)

print("-- In global --")
print("Built-in names:", len, round, str, list, True, None)
print("Global names:", X, func, MyClass)
