class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNumbers(l1, l2):
    dummy = ListNode()
    current = dummy
    carry = 0

    p = l1
    q = l2

    while p is not None or q is not None:
        x = p.val if p else 0
        y = q.val if q else 0

        sum_val = x + y + carry
        carry = sum_val // 10

        current.next = ListNode(sum_val % 10)
        current = current.next

        if p:
            p = p.next
        if q:
            q = q.next

    if carry > 0:
        current.next = ListNode(carry)

    return dummy.next
