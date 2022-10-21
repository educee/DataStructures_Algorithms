# Leetcode - 9
#Given an integer x, return true if x is palindrome integer.

#An integer is a palindrome when it reads the same backward as forward.

#For example, 121 is a palindrome while 123 is not.

def isPalindrome(self, x: int) -> bool:
        num = x
        newnum = 0
        while x>0:
            newnum = (newnum*10) + x%10
            x = x//10
            
        return num == newnum
