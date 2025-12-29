class Person:
  def __init__(self,gender):
    self.gender = gender
class College:
  def __init__(self,s1,s2):
    self.s1 = Person("Male")
    self.s2 = Person("Female")
c = College("","")
print(c.s1.gender)
print(c.s2.gender)