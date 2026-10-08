from abc import ABC, abstractmethod
from dataclasses import dataclass


class Student:
    school = "CS50"

    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} lives in {self.house}"

    @classmethod
    def from_string(cls, student_data):
        name, house = student_data.split(",")
        return cls(name.strip(), house.strip())

    @staticmethod
    def valid_house(house):
        return house in {"Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"}


class Wizard(Student):
    def __init__(self, name, house, patronus):
        super().__init__(name, house)
        self.patronus = patronus

    def cast_spell(self):
        return f"{self.name} casts a spell with a {self.patronus} patronus"


class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, amount):
        if amount < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = amount

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.balance += amount

    def withdraw(self, amount):
        if amount <= 0 or amount > self.balance:
            raise ValueError("Invalid withdrawal amount")
        self.balance -= amount

    def __str__(self):
        return f"{self.owner}: ${self.balance:.2f}"


@dataclass
class Book:
    title: str
    author: str
    pages: int


class Library:
    def __init__(self, name):
        self.name = name
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        return [book.title for book in self.books]


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"


def main():
    student = Student("Harry", "Gryffindor")
    print(student)
    print(f"School: {Student.school}")
    print(f"Valid house: {Student.valid_house(student.house)}")

    parsed_student = Student.from_string("Hermione, Gryffindor")
    print(parsed_student)

    wizard = Wizard("Luna", "Ravenclaw", "hare")
    print(wizard)
    print(wizard.cast_spell())
    print(f"Is a student: {isinstance(wizard, Student)}")

    account = BankAccount("Harry", 100)
    account.deposit(50)
    account.withdraw(25)
    print(account)

    book = Book("The Example Book", "A. Author", 200)
    print(f"{book.title} by {book.author}, {book.pages} pages")

    library = Library("CS50 Library")
    library.add_book(book)
    library.add_book(Book("Another Example", "B. Author", 150))
    print(f"{library.name}: {', '.join(library.list_books())}")

    shapes = [Rectangle(4, 5), Circle(3)]
    for shape in shapes:
        print(f"{type(shape).__name__} area: {shape.area():.2f}")

    first_vector = Vector(2, 3)
    second_vector = Vector(4, 1)
    print(f"Vector addition: {first_vector + second_vector}")


if __name__ == "__main__":
    main()