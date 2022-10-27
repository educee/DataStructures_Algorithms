# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next or not head.next.next:
            return head
        
        i = 1
        oddptr = head
        evenptr = evenhead =  head.next
        cur = head
        
        while cur:
            if i>2 and (i%2) != 0:
                oddptr.next = cur
                oddptr = oddptr.next
                
            elif i>2 and (i%2) == 0:
                evenptr.next = cur
                evenptr = evenptr.next
            cur = cur.next
            i += 1
        evenptr.next = None       
        oddptr.next = evenhead
        
        return head
