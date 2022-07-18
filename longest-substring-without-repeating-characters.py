# https://leetcode.com/problems/longest-substring-without-repeating-characters/   Python3   61 ms | 14MB  - faster than 94.53% of Python3 online submissions
#                                                                                                         - less memory than 92.90% of Python3 online submission

class Solution:
        
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        
        slen = 0
        res=[]
        
        for i in s:
            if i not in res:
                res.append(i)
                slen = max(slen,len(res))
            else:
                y = res.index(i)
                res = res[y+1:]
                res.append(i)
                slen = max(slen,len(res))
        return slen
