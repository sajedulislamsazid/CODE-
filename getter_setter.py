class User:
    def __init__(self, name, age, money) -> None:
        self._name = name
        self._age = age
        self._money = money

    @property
    def age(self):
        return self._age

    @property
    def money(self):
        return self._money

    @property
    def salary(self):
        return self._money

    @salary.setter
    def salary(self, value):
        if value < 0:
            raise ValueError("Salary cannot be negative")
        self._money = value

samsu = User('Kopa', 21, 12000)
print(samsu.age)  # This will print the age of the user, which is 21.
print(samsu.money)  # This will print the money of the user, which is 12000.

print(samsu.age)  # This will print the age of the user, which is 21.
print(samsu.salary)  # This will print the salary of the user, which is 12000.
samsu.salary = 15000  # This will set the salary of the user to 15000.      
