import re
def filter_emails(a):
  pattern = r'^[A-Za-z0-9][A-Za-z0-9._]*@[A-Za-z]+\.[A-Za-z]{2,4}$'
  result = []
  for x in a:
    if re.match(pattern,x):
      result.append(x)
  return result


a = ["student123@gmail.com", "teacher.name@soa.edu", "abc.xyz@abc.in",
"xyz#12@abc.com", "bad@1n.com"]
print(filter_emails(a))
