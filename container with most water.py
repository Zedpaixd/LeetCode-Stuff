# https://leetcode.com/problems/container-with-most-water   Python 3
# Runtime: 720 ms, faster than 97.80% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.4 MB, less than 54.33% of Python3 online submissions for Container With Most Water.

class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater,initial,end = 0,0,len(height)-1
        while initial < end:
            if height[initial] <= height[end]:
                maxWater = max(maxWater,(end-initial)*height[initial])
                initial += 1
            else:
                maxWater = max(maxWater,(end-initial)*height[end])
                end -= 1
        return maxWater
      
# https://leetcode.com/submissions/detail/756688039/
