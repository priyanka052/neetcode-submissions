
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        grprev = dummy
        while True:
            kth = grprev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next
            grnext = kth.next
        
            prev = grnext
            curr = grprev.next
            while curr != grnext:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp

            temp =  grprev.next
            grprev.next = kth
            grprev = temp