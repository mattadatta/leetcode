from collections import deque

def serialize(root):
    results = []

    queue = deque()
    if root != None:
        queue.append(root)

    i = 1
    did_add = True
    while bool(queue):
        i -= 1
        node = queue.popleft()

        if node != None:
            queue.append(node.left)
            queue.append(node.right)
            did_add = did_add or node.left != None or node.right != None
        results.append(str(node.val if node != None else "_"))
        
        if i == 0:
            if not did_add:
                break
            i = len(queue)
            did_add = False

    return ",".join(results)

def deserialize(str):
    if str == "":
        return None
    
    tokens = str.split(",")
    if len(tokens) < 1:
        return None
    
    root = TreeNode(int(tokens[0]))
    queue = deque()
    current = root
    is_left = True
    for s in tokens[1:]:
        if s != "_":
            node = TreeNode(int(s))
            queue.append(node)
            if is_left:
                current.left = node
            else:
                current.right = node
        is_left = not is_left
        if is_left and len(queue) > 0:
            current = queue.popleft()

    return root

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """
        return serialize(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        return deserialize(data)


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
    
    def __repr__(self):
        return f"TreeNode(val={self.val})"

def to_tree_nodes(list):
    if not list or len(list) == 0:
        return None
    
    root = TreeNode(list[0])
    queue = deque()
    current = root
    is_left = True
    for n in list[1:]:
        if n != None:
            node = TreeNode(n)
            queue.append(node)
            if is_left:
                current.left = node
            else:
                current.right = node
        is_left = not is_left
        if is_left and len(queue) > 0:
            current = queue.popleft()
    
    return root

def to_list(root):
    results = []

    queue = deque()
    if root != None:
        queue.append(root)

    i = 1
    did_add = True
    while bool(queue):
        i -= 1
        node = queue.popleft()

        if node != None:
            queue.append(node.left)
            queue.append(node.right)
            did_add = did_add or node.left != None or node.right != None
        results.append(node.val if node != None else None)
        
        if i == 0:
            if not did_add:
                break
            i = len(queue)
            did_add = False

    return results

def run_test(list):
    root = to_tree_nodes(list)
    ser = Codec()
    deser = Codec()
    ans = deser.deserialize(ser.serialize(root))
    return to_list(ans)

list = [1,2,3,None,None,4,5]
result = run_test(list)
print(result)

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
