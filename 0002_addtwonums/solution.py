def add_two_numbers(l1, l2):
    w1 = l1
    w2 = l2
    overflow = 0
    head = None
    current = None
    while w1 or w2:
        val = getattr(w1, 'val', 0) + getattr(w2, 'val', 0) + overflow
        node_val = val % 10
        node = ListNode(node_val)
        if not head:
            head = node
        else:
            current.next = node
        current = node
        overflow = 1 if val > 9 else 0
        w1 = getattr(w1, 'next', None)
        w2 = getattr(w2, 'next', None)
    
    if overflow > 0:
        node = ListNode(overflow)
        current.next = node
        current = node
    
    return head

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        return add_two_numbers(l1, l2)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_linked_list(items):
    if not items:
        return None

    head = ListNode(items[0])
    current = head

    for item in items[1:]:
        node = ListNode(item)
        current.next = node
        current = node

    return head

def to_list(head):
    result = []
    current = head
    while current:
        result.append(current.val)
        current = current.next
    return result

def addTwoNumbers(a1, a2):
    sol = Solution()
    return to_list(sol.addTwoNumbers(to_linked_list(a1), to_linked_list(a2)))

a1 = [2, 4, 3, 8]
a2 = [5, 6, 4]
result = addTwoNumbers(a1, a2)
print(result)
