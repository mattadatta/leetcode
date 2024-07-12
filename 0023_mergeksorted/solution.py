import heapq

def merge_k_lists(lists):
    queue = []

    i = 0
    for l in lists:
        if l != None:
            heapq.heappush(queue, (l.val, i, l))
            i += 1
    
    head = heapq.heappop(queue)[-1] if len(queue) > 0 else None
    if head != None and head.next != None:
        heapq.heappush(queue, (head.next.val, i, head.next))
        i += 1

    current = head
    while len(queue) > 0:
        node = heapq.heappop(queue)[-1]
        current.next = node
        current = node
        next = node.next
        if next != None:
            heapq.heappush(queue, (next.val, i, next))
            i += 1
    
    return head

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        return merge_k_lists(lists)


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return f"ListNode(val={self.val}, has_next={self.next != None})"

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

def mergeKLists(lists):
    sol = Solution()
    return to_list(sol.mergeKLists([to_linked_list(l) for l in lists]))

lists = [[1,4,5],[1,3,4],[2,6]]
result = mergeKLists(lists)
print(result)
