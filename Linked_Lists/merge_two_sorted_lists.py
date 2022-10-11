#Leetcode - 21
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        
        outList = ListNode(0)
        resultNode = outList
        
        while list1 and list2:
            if list1.val < list2.val:
                outList.next = list1
                list1 = list1.next
            else:
                outList.next = list2
                list2 = list2.next
            outList = outList.next
            
        if list1:
            outList.next = list1
        elif list2:
            outList.next = list2
            
        return resultNode.next
            
