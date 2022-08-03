# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    reversed1 = None
    while head:
        current = head.next # creates a new ListNode object with all elements but the first element of the list
        head.next = reversed1 # isolates the first element of the List by replacing the next variable with the current reversed list (starting with None)
        reversed1 = head # saves the current head to the current reversed list (because it's currently reversed lol)
        head = current # makes the current head the rest of the objects not reversed yet and also makes sure that the current head is not None so it doesn't exit out.
    return reversed1


# recursive solution. i actually have no idea how this works bc i refuse to draw it out. but here anyway lol
def reverseList2( head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head # this is not head and not head.next so we can rearrange head.next.next to be the correct head. checks if it's the end of the list. not head is needed here because of empty head input.
    node = reverseList2(head.next) # reversed list
    print(head.next)
    print(node)
    head.next.next = head # makes a circle to point it to itself
    print(head)
    head.next = None # isolates?
    return node

# recursive solution but muy slow.
def reverseList3(head: Optional[ListNode], newHead = None) -> Optional[ListNode]:
    if not head: return newHead # returns the full reversed list
    next = head.next # creates a new ListNode featuring all of List[1:]
    head.next = newHead # isolates current head and replaces the end with the current reversed list 
    return reverseList3(next, head)