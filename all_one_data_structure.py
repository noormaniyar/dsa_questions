"""
    Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

    Implement the AllOne class:

    AllOne() Initializes the object of the data structure.
    inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
    dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
    getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
    getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
    Note that each function must run in O(1) average time complexity.
"""


class Node:
    def __init__(self, freq):
        self.freq = freq
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):
        self.key_count = {}  # key -> count
        self.freq_nodes = {}  # count -> Node
        self.head = Node(float('-inf'))  # Dummy head (smallest)
        self.tail = Node(float('inf'))  # Dummy tail (largest)
        self.head.next = self.tail
        self.tail.prev = self.head

    def _add_node_after(self, new_node, prev_node):
        """Add new_node after prev_node in the doubly linked list."""
        next_node = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        new_node.next = next_node
        next_node.prev = new_node

    def _remove_node(self, node):
        """Remove a node from the doubly linked list."""
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node
        del self.freq_nodes[node.freq]

    def _move_key(self, key, old_node, new_node):
        """Move key from old_node to new_node."""
        old_node.keys.remove(key)
        if not old_node.keys:
            self._remove_node(old_node)
        new_node.keys.add(key)

    def inc(self, key):
        """
        Increments the count of the string key by 1. If key does not exist, insert it with count 1.
        :type key: str
        :rtype: None
        """
        if key in self.key_count:
            cur_count = self.key_count[key]
            cur_node = self.freq_nodes[cur_count]
            new_count = cur_count + 1
        else:
            cur_count = 0
            cur_node = self.head
            new_count = 1

        self.key_count[key] = new_count

        if new_count not in self.freq_nodes:
            new_node = Node(new_count)
            self.freq_nodes[new_count] = new_node
            self._add_node_after(new_node, cur_node)
        else:
            new_node = self.freq_nodes[new_count]

        if cur_count > 0:
            self._move_key(key, cur_node, new_node)
        else:
            new_node.keys.add(key)

    def dec(self, key):
        """
        Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it.
        :type key: str
        :rtype: None
        """
        cur_count = self.key_count[key]
        cur_node = self.freq_nodes[cur_count]

        if cur_count == 1:
            del self.key_count[key]
            cur_node.keys.remove(key)
            if not cur_node.keys:
                self._remove_node(cur_node)
        else:
            new_count = cur_count - 1
            self.key_count[key] = new_count
            if new_count not in self.freq_nodes:
                new_node = Node(new_count)
                self.freq_nodes[new_count] = new_node
                self._add_node_after(new_node, cur_node.prev)
            else:
                new_node = self.freq_nodes[new_count]
            self._move_key(key, cur_node, new_node)

    def getMaxKey(self):
        """
        Returns one of the keys with the maximal count. If no element exists, return an empty string "".
        :rtype: str
        """
        if self.tail.prev == self.head:
            return ""
        return next(iter(self.tail.prev.keys))

    def getMinKey(self):
        """
        Returns one of the keys with the minimum count. If no element exists, return an empty string "".
        :rtype: str
        """
        if self.head.next == self.tail:
            return ""
        return next(iter(self.head.next.keys))




# Your AllOne object will be instantiated and called as such:
key = "exampleKey"
obj = AllOne()
obj.inc(key)
obj.dec(key)
param_3 = obj.getMaxKey()
param_4 = obj.getMinKey()
print(obj)
print(obj.inc(key))
print(obj.dec(key))
print(param_3)
print(param_4)