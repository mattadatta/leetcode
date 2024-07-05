def merge_nodes(head):
    new_head = head.next
    current = new_head
    while current:
        acc = current.val
        walker = current.next
        while walker.val != 0:
            acc += walker.val
            walker = walker.next
        current.val = acc
        current.next = walker.next
        current = walker.next
    
    return new_head

class Solution(object):
    def mergeNodes(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return merge_nodes(head)


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

def mergeNodes(l):
    sol = Solution()
    return to_list(sol.mergeNodes(to_linked_list(l)))

l = [0,1,0,3,0,2,2,0]
result = mergeNodes(l)
print(result)
