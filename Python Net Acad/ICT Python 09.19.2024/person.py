"""
Write a Python program to create a person class. Include attributes like name, country and date of birth. Implement a method to determine the person's age.
"""
from datetime import date

class Person:
    def __init__(self, name, country, date_of_birth):
        self.name = name
        self.country = country
        self.date_of_birth = date_of_birth

    def calcualteAge(self):
        today = date.today()
        age = today.year - self.date_of_birth.year
        if today < date(today.year, self.date_of_birth.month, self.date_of_birth.day):
            age -= 1
        return age
    
person1 = Person("Mikel Kulla", "Albania", date(2002, 4, 8))
print(f"Name: {person1.name}")
print(f"Country: {person1.country}")
print(f"Birthday: {person1.date_of_birth}")
print(f"Age: {person1.calcualteAge()}")