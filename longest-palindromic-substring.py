# https://leetcode.com/problems/longest-palindromic-substring/   Python 3
# Runtime: 1001 ms, faster than 80.18% of Python3 online submissions for Longest Palindromic Substring.
# Memory Usage: 13.8 MB, less than 91.28% of Python3 online submissions for Longest Palindromic Substring.

class Solution:
    
    def longestPalindrome(self, s: str) -> str:
        longest = s[0]
        for i in range(len(s)):
            ifeven = self.getPal(s,i,i+1)
            ifodd = self.getPal(s,i,i+2)
            #if max(len(ifeven),len(ifodd)) > len(longest):
            #    longest = ifeven if len(ifeven) > len(ifodd) else ifodd                            # both options are just as fine but lambdas are slightly better
            longest = max([longest,ifodd,ifeven], key=lambda x: len(x))
        return longest
    
    def getPal(self,s: str, l: int, r: int) -> str:
        while (l >= 0 and r < len(s) and s[l] == s[r]):
            l=l-1
            r=r+1
        return s[l+1:r]

# https://leetcode.com/submissions/detail/751536281/
