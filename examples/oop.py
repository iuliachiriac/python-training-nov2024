from datetime import date


class Person:
    """Class describing people"""
    count = 0  # class attributes

    def __init__(self, name, dob):
        self.name = name  # instance attributes
        self.date_of_birth = dob
        Person.count += 1

    def greet(self, greeting="hi"):
        print(f"{greeting.capitalize()}! I am {self.name}.")


if __name__ == "__main__":
    p1 = Person("Anna", date(1984, 6, 12))
    p2 = Person("John", date(2001, 8, 21))

    print("Instance attributes:", p1.name, p2.name, p1.date_of_birth,
          p2.date_of_birth)

    print("Class attributes:", Person.__name__, Person.__doc__, Person.count)

    p1.greet()
    p2.greet("hello")
