"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        dictcopy = {}
        curr = head
        while curr:
            copy = Node(curr.val)
            dictcopy[curr] = copy
            curr = curr.next
        temp = head
        while temp:
            node = dictcopy[temp]
            node.next = dictcopy[temp.next] if temp.next else None
            node.random = dictcopy[temp.random] if temp.random else None
            temp = temp.next
        return dictcopy[head]

        
        