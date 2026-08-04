"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        clone_dict = {}
        clone_dict[node] = Node(node.val)
        q = []
        q.append(node)

        while q:
            curr = q.pop(0)
            for neighbor in curr.neighbors:
                if neighbor not in clone_dict:
                    newnode = Node(neighbor.val)
                    clone_dict[neighbor] = newnode
                    q.append(neighbor)
                clone_dict[curr].neighbors.append(clone_dict[neighbor])
                    
        return clone_dict[node] if node else None

        