# https://leetcode.com/problems/string-to-integer-atoi/  Python 3

# Runtime: 19 ms, faster than 100.00% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 13.9 MB, less than 29.65% of Python3 online submissions for String to Integer (atoi).


class Solution:
    def myAtoi(self, s: str) -> int:
        s=s.strip()
        if len(s) == 0:
            return 0
        sign = 1
        nb = 0
        if s[0] in "+-":
            sign = int(s[0]+'1')
            s=s[1:]
        for chara in s:
            if chara in '0123456789':
                nb = nb * 10 + ord(chara)-48
            else:
                break
        return max(-2**31, min(nb*sign,2**31-1))
      
      
# https://leetcode.com/submissions/detail/753098900/
