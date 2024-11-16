class Solution:
    def treeDiameter(self, edges: List[List[int]]) -> int:
        # If there are no edges, the tree diameter is 0 (no path exists)
        if not edges:
            return 0

        # Create an adjacency list to represent the graph
        edgedict = collections.defaultdict(list)

        # Populate the adjacency list with the provided edges
        for edge1, edge2 in edges:
            edgedict[edge1].append(edge2)  # Add edge1's connection to edge2
            edgedict[edge2].append(edge1)  # Add edge2's connection to edge1

        # Helper function to perform BFS and find the longest path starting from `startnode`
        def bfs(startnode: int) -> List[int]:
            current = [[startnode]]  # Initialize BFS with the starting node in a path
            longest = []  # Variable to keep track of the longest path found so far

            # Perform BFS
            while current:
                currentlvl = current.pop()  # Get the last path from the stack
                neighbors = edgedict[currentlvl[-1]]  # Get neighbors of the last node in the path

                # If the current node is a leaf and the path is the longest so far, update `longest`
                if len(neighbors) == 1 and neighbors[0] in currentlvl and len(currentlvl) > len(longest):
                    longest = currentlvl
                    continue  # Skip further exploration of this path

                # Add unvisited neighbors to the path and push the new path to the stack
                for neighbor in neighbors:
                    if neighbor not in currentlvl:  # Avoid cycles by skipping visited nodes
                        current.append(currentlvl + [neighbor])

            # Return the longest path found from the starting node
            return longest

        # Step 1: Perform BFS from any node (first node in the edge list) to find the farthest node
        tmp_longest = bfs(edges[0][0])
        farthest_node = tmp_longest[-1]  # The farthest node in the longest path

        # Step 2: Perform BFS from the farthest node to find the actual longest path in the tree
        final_longest = bfs(farthest_node)

        # The diameter of the tree is the number of edges in the longest path
        return len(final_longest) - 1





        
        
        