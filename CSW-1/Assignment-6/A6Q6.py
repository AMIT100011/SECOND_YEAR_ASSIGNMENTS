class MyInt(int):
    def __new__(cls, value):
        print("__new__ called for immutable int")
        # Modify value during creation
        value = value * 2
        return super().__new__(cls, value)

    def __init__(self, value):
        print("__init__ called (value already set)")


# Create object
num = MyInt(10)

print("Final value of num:", num)
class Demo:
    def __new__(cls):
        print("__new__ method called")
        obj = object.__new__(cls)   # manual object creation
        return obj

    def __init__(self):
        print("__init__ method called")


# Create object
d = Demo()
