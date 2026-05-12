class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Find the middle
        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second = slow.next
        prev, slow.next = None, None

        # Reverse the second list 
        while second:
            temp = second.next 
            second.next = prev 
            prev = second 
            second = temp 
        
        # Merge two halfs 
        first, second = head, prev

        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
            


            
        
        


            
        


        