def merge_two_lists(list1, list2):
    w1 = list1
    w2 = list2
    head = None
    current = None
    while w1 != None or w2 != None:
        node = None
        if w1 != None and w2 != None:
            if w1.val <= w2.val:
                node = w1
                w1 = w1.next
            else:
                node = w2
                w2 = w2.next
        elif w1 != None:
            node = w1
            w1 = w1.next
        else:
            node = w2
            w2 = w2.next
        
        if current != None:
            current.next = node
        else:
            head = node
        current = node
    
    return head

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        return merge_two_lists(list1, list2)

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

def mergeTwoLists(list1, list2):
    sol = Solution()
    return sol.mergeTwoLists(to_linked_list(list1), to_linked_list(list2))

sol = Solution()
list1 = [1, 2]
list2 = [3, 4]
result = sol.mergeTwoLists(list1, list2)
print(result)
