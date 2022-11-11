# from heapq import heapify, heappush, heappushpop
# from typing import List


class DoubleLinkedListNode:
    def __init__(self, key: int = -1, value: int = 0):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None
        

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.head = DoubleLinkedListNode()
        self.tail = DoubleLinkedListNode()
        self.hashmap = {}
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def move_to_tail2(self, node):
        # cut the original connection of node
        node.prev.next = node.next
        node.next.prev = node.prev
    
        # move to tail
        self.tail.prev.next = node
        node.prev = self.tail.prev
        node.next = self.tail
        self.tail.prev = node
            
    def move_to_tail(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

        node.next = self.tail
        node.prev = self.tail.prev
        self.tail.prev.next = node
        self.tail.prev = node
    
    def get(self, key:int):
        res = self.hashmap.get(key, -1)
        if res == -1:
            return res
        else:
            # move this key to tail (recently used)
            self.move_to_tail(res)
            return res.value
        
    def put(self, key: int, value: int):
        if key in self.hashmap:
            curNode = self.hashmap[key]
            curNode.value = value
            self.move_to_tail(curNode)
        else:
            # exceed the capacity, remove the least commonly used
            if len(self.hashmap) == self.capacity:
                node = self.head.next
                self.head.next = node.next
                node.next.prev = self.head
                self.hashmap.pop(node.key)
            
            curNode = DoubleLinkedListNode(key, value)
            self.hashmap[key] = curNode
            # self.move_to_tail(curNode)
            curNode.prev = self.tail.prev
            curNode.next = self.tail
            self.tail.prev.next = curNode
            self.tail.prev = curNode

        
            


# Your LRUCache object will be instantiated and called as such:
capacity = 2

obj = LRUCache(capacity)

obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))