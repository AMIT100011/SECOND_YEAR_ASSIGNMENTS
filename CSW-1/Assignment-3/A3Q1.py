numbers = input("Enter three numbers : ").split()
t = (numbers[0],numbers[1],numbers[2])
x,y,z = int(numbers[0]),int(numbers[1]),int(numbers[2])
print(x,y,z)
y,z = z,y
print(x,y,z)


