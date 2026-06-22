class ListNode:
    def __init__(self, key = None, next = None):
        self.key = key
        self.next = next

class MyHashSet:

    def __init__(self):
        self.length = 1000
        self.hashset = [ListNode(None,None) for i in range(self.length)]

    def hashindex(self, key):
        return key % self.length

    def add(self, key: int) -> None:
        idx = self.hashindex(key)
        curr = self.hashset[idx]
        while curr.next:
            if curr.key == key:
                return
            curr = curr.next
        if curr.key != key:
            curr.next = ListNode(key)

    def remove(self, key: int) -> None:
        idx = self.hashindex(key)
        prev = self.hashset[idx]
        curr = prev.next
        while curr:
            if curr.key == key:
                prev.next = curr.next
                return # Key removed, exit
            prev = curr
            curr = curr.next

    def contains(self, key: int) -> bool:
        idx = self.hashindex(key)
        curr = self.hashset[idx].next
        while curr:
            if curr.key == key:
                return True
            curr = curr.next
        return False
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)