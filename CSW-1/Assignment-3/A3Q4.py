def sales(*args,**kwargs):
  total = 0
  for i in args:
    total += i
  print("Total Sales Amount:", total)
  print("Number of Extra Information Items:", len(kwargs))

  if len(kwargs)>0:
    for k in kwargs:
      print(k,kwargs[k])

sale = input("enter amount ").split()

l = []
for x in sale:
  l.append(int(x))

extra = int(input("enter your extras : "))

dict = {}


for i in range(extra):
    key = input("Enter key: ")
    value = input("Enter value: ")
    dict[key] = value
sales(*l,**dict)
