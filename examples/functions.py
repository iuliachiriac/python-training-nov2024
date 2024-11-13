def greet(name, greeting=None):
    greeting = greeting or "hello"
    print(f"{greeting.capitalize()}, {name}!")


# calls with positional arguments:
greet("Anna")
greet("Jane", "hi")

# call with keyword arguments:
greet(greeting="hi", name="Jane")


def decrement(nr, step=1):
    if step < 10:
        return nr - step
    return nr + 10 - step


print(decrement(10))

result = decrement(10, 12)
print(result)


def varargs(*args, sep=None, **kwargs):
    print(args, type(args))
    print("sep =", sep)
    print(kwargs, type(kwargs), end="\n\n")


varargs()
varargs(1)
varargs(1, 2, 3, 4)
varargs(1, 2, 3, 4, sep="-")
varargs(name="Anna", age=20)
