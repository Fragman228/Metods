from datetime import date

class Person:
    def __init__(self, name):
        self.name = name
        self.curyear = date.today().year

    def genperson(self, age):
        self.age = age
        perage = self.curyear - self.age
        if perage < 18:
            return "Person is low aged"
        else:
            return f"Name: {self.name}, Age: {self.curyear - self.age}"
per1 = Person("Василий").genperson(2005)
print(per1)
