class Node:
    def __init__(self, key = None, value = None, next = None):
        self.key = key
        self.value = value
        self.next = next

class MyHashMap:

    def __init__(self):
        
        self.map = [None] * 10000

    def put(self, key: int, value: int) -> None:

        idx = key % 10000
        if self.map[idx] is None:
            self.map[idx] = Node(key, value)
        else:
            curr = self.map[idx]
            while True:
                if curr.key == key:
                    curr.value = value
                    return
                if not curr.next:
                    break
                curr = curr.next
            curr.next = Node(key, value)

    def get(self, key: int) -> int:

        idx = key % 10000
        curr = self.map[idx]
        while curr:
            if key == curr.key:
                return curr.value
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:

        idx = key % 10000
        head = curr = self.map[idx]
        if not curr:
            return
        elif curr.next is None and curr.key == key:
            self.map[idx] = None
        prev = None
        while curr.next:
            if curr.key == key:
                prev.next = curr.next if prev else None
                return
            prev = curr
            curr = curr.next






        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)