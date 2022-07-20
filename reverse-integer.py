# https://leetcode.com/problems/reverse-integer  Python 3

# Runtime: 30 ms, faster than 97.20% of Python3 online submissions for Reverse Integer.
# Memory Usage: 13.8 MB, less than 62.97% of Python3 online submissions for Reverse Integer.

class Solution:
    def reverse(self, x: int) -> int:
        if x >= 0:
            return int(str(x)[::-1]) if int(str(x)[::-1]) < 2**31-1 else 0 
        else:
            return int(str(x)[:0:-1])*-1 if int(str(x)[:0:-1]) < 2**31 else 0
          
# https://leetcode.com/submissions/detail/752349257/
