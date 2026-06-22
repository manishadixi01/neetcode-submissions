class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head and not head.next and not head.next.next:
            return head
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        first = head
        last = prev
        while last:
            tmp1, tmp2 = first.next, last.next
            first.next = last
            last.next = tmp1
            first = tmp1
            last = tmp2