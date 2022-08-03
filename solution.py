# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
    reversed1 = None
    while head != None:
        current = head.next # creates a new ListNode object with all elements but the first element of the list
        head.next = reversed1 # isolates the first element of the List by replacing the next variable with the current reversed list (starting with None)
        reversed1 = head # saves the current head to the current reversed list (because it's currently reversed lol)
        head = current # makes the current head the rest of the objects not reversed yet and also makes sure that the current head is not None so it doesn't exit out.
    return reversed1


# recursive solution