# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr, prev = head, None

        while curr:
             temp = curr.next
             curr.next = prev
             prev = curr
             curr = temp 
        reversed_head = prev

        dummy = ListNode(0)
        dummy.next = reversed_head
        curr = dummy 

        for nums in range(n - 1):
            curr = curr.next
        curr.next = curr.next.next

        curr, prev = dummy.next, None 

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev



             
            
            
        




        