import numpy as np

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        # Special cases for edge cases in the input
        if n == 1:
            return [0]  # Only one node, it is the root and the only result
        if not edges:
            return []  # No edges provided, no trees can be formed

        # Build an adjacency list to represent the graph
        edgesdict = collections.defaultdict(list)
        for edge1, edge2 in edges:
            # Add each connection in both directions (undirected graph)
            edgesdict[edge1].append(edge2)
            edgesdict[edge2].append(edge1)

        # Initialize a list of leaf nodes (nodes with only one neighbor)
        leaves = [key for key, value in edgesdict.items() if len(value) == 1]

        # Start with all nodes, gradually trim the leaves
        remaining_nodes = n
        print(edgesdict)  # Debug: print the adjacency list to verify structure
        
        # Perform a topological-like trim of the leaves
        while remaining_nodes > 2:
            # Decrease the count of remaining nodes by the number of leaves
            remaining_nodes -= len(leaves)
            new_leaves = []  # List to store new leaves after removing current ones

            # Remove current leaves from the graph
            for leaf in leaves:
                # Each leaf has only one neighbor, pop it
                neighbor = edgesdict[leaf].pop()
                # Remove the leaf from its neighbor's list
                edgesdict[neighbor].remove(leaf)

                # If the neighbor becomes a leaf (only one connection left), add it to new_leaves
                if len(edgesdict[neighbor]) == 1:
                    new_leaves.append(neighbor)

            # Update the list of leaves to the newly identified leaves
            leaves = new_leaves

        # Remaining nodes are the roots of the minimum height trees
        return leaves




