from abc import ABC, abstractmethod

class LibraryItem(ABC):
    @abstractmethod
    def show_info(self):
        pass

class Book(LibraryItem):
    def __init__(self, id, title, author, quantity):
        self.id = id
        self.title = title
        self.author = author
        self.__quantity = quantity

    def get_quantity(self):
        return self.__quantity

    def borrow_item(self):
        if self.__quantity > 0:
            self.__quantity -= 1
            return True
        return False

    def return_item(self):
        self.__quantity += 1

    def show_info(self):
        print(f"{self.id:<10} | {self.title:<25} | {self.author:<20} | {self.__quantity:<10}")