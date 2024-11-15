from datetime import date


class Person:
    """Class describing people"""
    count = 0  # class attributes

    def __init__(self, name, dob):
        self.name = name  # instance attributes
        self.date_of_birth = dob
        self._increment_count()

    @classmethod
    def _increment_count(cls):
        cls.count += 1

    @staticmethod
    def years_since(date_start):
        today = date.today()
        years = today.year - date_start.year
        if (today.month, today.day) < (date_start.month, date_start.day):
            years -= 1
        return years

    def greet(self, greeting="hi"):
        print(f"{greeting.capitalize()}! I am {self.name}.")

    def __str__(self):
        return f"Person object (name={self.name}, "\
               f"date_of_birth={self.date_of_birth})"

    def __lt__(self, other):
        return self.date_of_birth > other.date_of_birth


if __name__ == "__main__":
    p1 = Person("Anna", date(1984, 6, 12))
    p2 = Person("John", date(2001, 8, 21))

    print("Instance attributes:", p1.name, p2.name, p1.date_of_birth,
          p2.date_of_birth)

    print("Class attributes:", Person.__name__, Person.__doc__, Person.count)

    p1.greet()
    p2.greet("hello")

    print(str(p1))

    print(f"{p1.name} is younger than {p2.name}:", p1 < p2)

    print(Person.years_since(date(1918, 12, 1)))
    print(p1.years_since(date(1918, 12, 1)))
