'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

x = 121
x = str(x)
if x == x[::-1]:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")