class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.count = 0
        self.capacity = capacity
        self.cache = {}

    def get(self, key):
        """
        Retrieve the value associated with the key.
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            node = self.cache.get(key)
            self.__move_to_front(node)
            return node.value
        return -1

    def put(self, key, value):
        """
        Insert or update the key-value pair in the cache.
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.cache:
            node = self.cache.get(key)
            node.value = value
            self.__move_to_front(node)
        else:
            node = LRUNode(key, value)
            self.__add_to_front(node)
            self.cache[key] = node

    def __move_to_front(self, node):
        if not node.prev:
            return
        
        node.prev.next = node.next
        if node.next:
            node.next.prev = node.prev
        else:
            self.tail = node.prev
        
        node.prev = None
        node.next = self.head
        self.head.prev = node
        self.head = node

    def __add_to_front(self, node):
        if self.count == 0:
            self.head = node
            self.tail = node
            self.count = 1
            return
        
        self.head.prev = node
        node.next = self.head
        self.head = node

        if self.count < self.capacity:
            self.count += 1
            return
        
        del self.cache[self.tail.key]
        self.tail = self.tail.prev
        self.tail.next = None
        
class LRUNode(object):
    def __init__(self, key, value, next=None, prev=None):
        self.key = key
        self.value = value
        self.next = next
        self.prev = prev

    def __str__(self):
    #     return f"LRUNode(key={self.key}, value={self.value})"

    # def __repr__(self):
        next_key = self.next.key if self.next else None
        prev_key = self.prev.key if self.prev else None
        return f"LRUNode(key={self.key}, value={self.value}, next={next_key}, prev={prev_key})"


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.put(3, 3)
