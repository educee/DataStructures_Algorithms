#Leetcode - 206
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return None
        curNode = head
        prevNode = None
        
        while curNode:
            tmpNode = curNode.next
            curNode.next = prevNode
            prevNode = curNode
            curNode = tmpNode
            
        return prevNode
