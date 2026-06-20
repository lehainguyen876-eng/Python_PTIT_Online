from abc import abstractmethod
from book import LibraryItem

class Person(LibraryItem):
    def __init__(self, id, name):
        self.id = id
        self.name = name

    @abstractmethod
    def show_info(self):
        pass

class Student(Person):
    def __init__(self, id, name, class_name):
        super().__init__(id, name)
        self.class_name = class_name

    def show_info(self):
        print(f"{self.id:<10} | {self.name:<25} | {self.class_name:<15}")