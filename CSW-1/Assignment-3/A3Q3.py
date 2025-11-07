nums = list(map(int,input("enter integers : ").split()))
if len(nums) < 3:
    print("Please enter at least 3 integers.")
else:
  a,b,*rest = nums
  print(a,b,rest)
  a,b = b,a
  print(a,b,rest)

  add = sum(rest)
  print(add)
  a,*middle,b = nums
  print(a,middle,b)