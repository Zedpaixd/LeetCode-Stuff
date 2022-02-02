# https://leetcode.com/problems/add-two-numbers/   Python3   28ms

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
            
            if l1:
                finsum += (l1.val * tens) 
                l1 = l1.next
                
            if l2:
                finsum += (l2.val * tens) 
                l2 = l2.next
                
            tens *= 10
            
        finalOutput = ListNode()
        output = finalOutput
        
        for char in str(finsum)[::-1]:
            output.next = ListNode(int(char))
            output = output.next
            
        return finalOutput.next
        
        
