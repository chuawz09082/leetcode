"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # If the input graph is empty, return None
        if not node:
            return None
        
        # If the node has no neighbors, return a new node with the same value
        # (This handles isolated nodes)
        if not node.neighbors:
            return Node(node.val)

        # Dictionary to store cloned nodes. Each key is an original node,
        # and the value is its corresponding cloned node.
        cloned = {}

        # Initialize a queue for BFS traversal starting with the input node
        queue = [node]
        
        # Clone the root node and add it to the cloned dictionary
        cloned[node] = Node(node.val)

        # Perform BFS traversal to clone the graph
        while queue:
            # Pop the first node in the queue for processing
            current = queue.pop(0)

            # Traverse each neighbor of the current node
            for neighbor in current.neighbors:
                # If the neighbor has not been cloned yet
                if neighbor not in cloned:
                    # Create a clone of the neighbor
                    cloned[neighbor] = Node(neighbor.val)
                    # Add the original neighbor to the queue for further processing
                    queue.append(neighbor)
                
                # Link the cloned current node to the cloned neighbor
                cloned[current].neighbors.append(cloned[neighbor])
        
        # Return the clone of the root node as the entry point to the cloned graph
        return cloned[node]
                

        

