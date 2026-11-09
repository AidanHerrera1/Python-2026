"""
-----------------------------------------------------------------------
ASSIGNMENT 14A: Object practice
-----------------------------------------------------------------------
[ ] 1. Header Docstring included.
[ ] 2. Define a class for a part of your project using PascalCase.
[ ] 3. Use __init__ to set private attributes (__variable).
[ ] 4. Write Setters and Getters for the attributes.
[ ] 5. Write a summary function that returns a formatted description.
[ ] 6. Instantiate two distinct objects and print their summaries.
-----------------------------------------------------------------------
"""

class Sneaker:
    def __init__(self, brand, model, size, stock):
        self.__brand = brand
        self.__model = model
        self.__size = size
        self.__stock = stock

    def set_brand(self, brand):
        self.__brand = brand

    def get_brand(self):
        return self.__brand

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_size(self, size):
        self.__size = size

    def get_size(self):
        return self.__size

    def set_stock(self, stock):
        self.__stock = stock

    def get_stock(self):
        return self.__stock

    def summary(self):
        return f"Brand: {self.__brand}, Model: {self.__model}, Size: {self.__size}, Stock: {self.__stock}"


sneaker1 = Sneaker("Nike", "Air Max", 10, 5)
sneaker2 = Sneaker("Adidas", "Ultraboost", 9, 3)

print(sneaker1.summary())
print(sneaker2.summary())








#