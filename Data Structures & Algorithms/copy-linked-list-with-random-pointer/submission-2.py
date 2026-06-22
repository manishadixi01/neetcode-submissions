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
            return None
        copydict = {}

        curr = head
        while curr:
            newnode = Node(curr.val)
            copydict[curr] = newnode
            curr = curr.next

        temp = head
        while temp:
            copynode = copydict[temp]
            copynode.next = copydict[temp.next] if temp.next else None
            copynode.random = copydict[temp.random] if temp.random else None
            temp = temp.next
        return copydict[head]


        
        