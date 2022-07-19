# https://leetcode.com/problems/two-sum/   Python 3  
# Runtime: 67 ms, faster than 90.59% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 50.46% of Python3 online submissions for Two Sum.

# "Hashmap" edition

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        a = {}
        for i in range(len(nums)):
            pair = target - nums[i]
            if pair in a.keys():
                return[a[pair],i]
            else:
                a[nums[i]] = i

# https://leetcode.com/submissions/detail/751503334/
