# Definition for singly-linked list.
class ListNode:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next
class Solution:
    def middleNode(head):
        s=head
        f=head
        while f and f.next and s is not None:
            f=f.next.next
            s=s.next
        return s
    head=ListNode(10)
    head.next=ListNode(5)
    head.next.next=ListNode(2)
    head.next.next.next=ListNode(1)
    Middle=middleNode(head)
    print(f"the middle node is {Middle.data}")
