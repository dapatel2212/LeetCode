'''Given an integer x, return true if x is a palindrome, and false otherwise.'''

class Solution:
    def isPalindrome(self,x):
        x = str(x)
        if x == x[::-1]:
            print("Is pelindrome")
        else:
            print("Is not a palindrome")
Sol = Solution()

Sol.isPalindrome(number = int(input("Enter the number: ")))