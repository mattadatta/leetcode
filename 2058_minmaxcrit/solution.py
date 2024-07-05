def min_max_crits(head):
    prev = head
    curr = getattr(head, "next", None)
    next = getattr(curr, "next", None)

    min_dist = -1
    first_crit = None
    curr_crit = None

    i = 2
    while next:
        if (curr.val < prev.val and curr.val < next.val) or (curr.val > prev.val and curr.val > next.val):
            if not first_crit:
                first_crit = i
            if curr_crit:
                if min_dist == -1:
                    min_dist = i - curr_crit
                else:
                    min_dist = min(min_dist, i - curr_crit)
            curr_crit = i

        prev = curr
        curr = next
        next = next.next
        i += 1

    if first_crit and (first_crit != curr_crit):
        return [min_dist, curr_crit - first_crit]
    else:
        return [-1, -1]

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        return min_max_crits(head)


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

def nodesBetweenCriticalPoints(l):
    sol = Solution()
    return sol.nodesBetweenCriticalPoints(to_linked_list(l))

l = [1,3,2,2,3,2,2,2,7]
result = nodesBetweenCriticalPoints(l)
print(result)
