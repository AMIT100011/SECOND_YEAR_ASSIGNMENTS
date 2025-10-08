import string

def is_palindrome_for_loop(s):
  s = s.lower()
  for i in range(len(s) // 2):
    if s[i] != s[len(s) - 1 - i]:
      return False
    return True

def is_palindrome_two_pointer(s):
    s = s.lower()
    newstr = ""
    for char in s:
      if char.isalnum():
            newstr += char

    left ,right = 0,len(newstr)-1
    while left < right:
        if newstr[left] != newstr[right]:
            return False
        left += 1
        right -= 1
    return True


text = input("Enter a string: ")

# Call both functions
result1 = is_palindrome_for_loop(text)
result2 = is_palindrome_two_pointer(text)

# Display results
print("\n--- Palindrome Check Results ---")
print(f"For-loop Check      : {'Palindrome' if result1 else 'Not Palindrome'}")
print(f"Two-pointer Check   : {'Palindrome' if result2 else 'Not Palindrome'}")


