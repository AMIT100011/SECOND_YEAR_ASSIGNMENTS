class Student:
  def __init__(self,name,roll):
    self.name = name
    self.roll = roll
  def display(self):
        print("Name:", self.name)
        print("Roll Number:", self.roll)
        print("--------------------")

n = int(input("no of students you want to add"))
l=[]
for i in range(n):
  name = input("enter name ")
  roll = input("enter roll ")
  s = Student(name,roll)
  l.append(s)
for x in l:
  x.display()
