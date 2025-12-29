class Car:
  def __init__(self, make, model):
    self.make = make
    self.model = model
  def set(self, make, model):
    self.make = make
    self.model = model
  def get(self):
    return f"Car Make: {self.make}, Model: {self.model}"
c1 = Car("Toyota", "Corolla")
print(c1.get())
c2 = Car("None","None")
print(c2.get())
c2.set("Honda", "Civic")
print(c2.get())
