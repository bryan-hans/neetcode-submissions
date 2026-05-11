class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 1. Find middle
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # 2. Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # cut the list in half
        while curr:
            curr.next, prev, curr = prev, curr, curr.next

        # 3. Merge two halves
        first, second = head, prev
        while second:
            next_second = second.next       # save before overwriting
            second.next = first.next
            first.next = second
            first = second.next             # advance to original first.next
            second = next_second            # advance to next in second half