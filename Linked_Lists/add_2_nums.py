#Leetcode - 2 add 2 numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        outList = ListNode(0)
        result = outList
        carry = 0
        while l1 and l2:
            resultVal = l1.val + l2.val + carry
            carry = resultVal//10
            outList.next = ListNode(resultVal%10)
            outList = outList.next
            l1 = l1.next
            l2 = l2.next
            
        while l1:
            resultVal = l1.val + carry
            carry = resultVal//10
            outList.next = ListNode(resultVal%10)
            outList = outList.next
            l1 = l1.next
        
        while l2:
            resultVal = l2.val + carry
            carry = resultVal//10
            outList.next = ListNode(resultVal%10)
            outList = outList.next
            l2 = l2.next
            
        if carry:
            outList.next = ListNode(carry)
            
        return result.next
            
