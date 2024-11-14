from functools import cache, wraps


@cache
def my_func(a, b):
    print(f"Computing {a} + {b}")
    return a + b


@cache
def factorial(n):
    print(f"Called factorial({n})")
    return n * factorial(n-1) if n else 1


# print(my_func(10, 2))
# print(my_func(10, 2))
# print(my_func(10, 2))
#
# print(factorial(5))
# print(factorial(4))
# print(factorial(7))


def make_pretty(func):
    @wraps(func)
    def inner(*args, **kwargs):
        print(f"I am {func.__name__} and I got decorated")
        result = func(*args, **kwargs)
        return result
    return inner


@make_pretty
def ordinary():
    print("I am ordinary")


@make_pretty
def greet(name):
    print(f"Hello, {name}!")


@make_pretty
def decrement(nr, step=1):
    """Decrements nr by step"""
    return nr - step


# ordinary = make_pretty(ordinary)  # ordinary = make_pretty.<locals>.inner

ordinary()
# print(ordinary)

greet("Anna")

print(decrement(10))
print(decrement(10, step=2))

print(decrement.__name__, decrement.__doc__)
help(decrement)
