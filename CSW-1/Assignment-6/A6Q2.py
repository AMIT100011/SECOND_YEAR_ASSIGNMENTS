class Animal:
  def __init__(self,name,species):
    self.name = name
    self.species = species
  def __str__(self):
    return f"Animal Name: {self.name}, Species: {self.species}"
a = Animal("Leo","Lion")
print(a)


