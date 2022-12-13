
s= input("Enter a string: ")
s = s.casefold()
rev = reversed(s)
if list(s) == list(rev):
   print("The string is a palindrome.")
else:
   print("The string is not a palindrome.")
