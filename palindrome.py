# https://leetcode.com/problems/palindrome-number/ 49ms | 13.8 MB   - faster than 99.35% of Python3 online submissions
#                                                                   - less memory than 96.43% of Python3 online submissions

class Solution:
    def isPalindrome(self, x: int) -> bool:
        return str(x)==str(x)[::-1]
      
      
# or for non python specific:

        if x<0 or (x!=0 and x%10==0):
            return False

        reverse = 0
        while x>reverse:
            reverse = reverse*10 + (x%10)
            x = x//10
        return x==reverse or x==(reverse//10) 
