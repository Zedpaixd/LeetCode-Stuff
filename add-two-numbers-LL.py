# https://leetcode.com/problems/add-two-numbers/   Python3   112 ms | 13.9 MB    - Less memory than 99.34% of python3 submissions

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        finsum = 0
        tens = 1
        
        while l1 or l2:
            
            if l1 or l2:
                finsum += ((l1.val if l1 else 0) * tens) 
                l1 = (l1.next if l1 else None)
                finsum += ((l2.val if l2 else 0) * tens) 
                l2 = (l2.next if l2 else None)
                
            tens *= 10
            
        finalOutput = ListNode()
        output = finalOutput
        
        for char in str(finsum)[::-1]:
            output.next = ListNode(int(char))
            output = output.next
            
        return finalOutput.next
