# https://leetcode.com/problems/median-of-two-sorted-arrays/  Python 3   98ms | 14.1MB   - faster than 92.25% of Python3 online submissions
#                                                                                        - less memory than 96.62% of Python3 online submission

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
#         aAvg = 0
#         bAvg = 0
#         division = 0
#         if (len(a)>0):
#             aMid = ((len(a)+1) // 2) - 1
#             aAvg = (a[aMid] + a[aMid+1 if len(a)%2==0 else aMid+0]) / 2
#             division += 1
#         if (len(b)>0):
#             bMid = ((len(b)+1) // 2) - 1
#             bAvg = (b[bMid] + b[bMid+1 if len(b)%2==0 else bMid+0]) / 2
#             division += 1
            
#         return (aAvg+bAvg)/division 
        nums1 = sorted(nums1+nums2)
        mid = (len(nums1)+1)//2
        return (nums1[mid-1]+nums1[mid-1 if len(nums1)%2==1 else mid-0])/2
        
      
# https://leetcode.com/submissions/detail/750306342/
