# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def detectCycle( head: Optional[ListNode]) -> Optional[ListNode]:
    slow = head
    fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: # needed after the moves because it's initially at the same position
            slow2 = head
            while slow != slow2: # floyds algorithm https://www.youtube.com/watch?v=LUm2ABqAs1w
                slow = slow.next
                slow2 = slow2.next
            return slow
    return None
    