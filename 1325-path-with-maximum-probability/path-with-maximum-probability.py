class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        """
        Finds the maximum probability path from the start_node to the end_node in a graph.

        @param n: Total number of nodes in the graph.
        @param edges: List of edges where each edge is represented as [node1, node2].
        @param succProb: List of probabilities corresponding to the edges.
        @param start_node: Starting node of the path.
        @param end_node: Target node of the path.
        @return: Maximum probability of reaching end_node from start_node.
        """

        # Create a graph representation using a dictionary (adjacency list)
        # Key: Node, Value: List of tuples (probability, connected_node)
        memo = collections.defaultdict(list)

        # Priority queue for managing nodes and their probabilities
        probabilities = []

        # Variable to store the maximum probability found
        max_probability = 0

        # Build the adjacency list from the given edges and probabilities
        for i in range(len(edges)):
            # Add both directions since the graph is undirected
            memo[edges[i][0]].append((succProb[i], edges[i][1]))
            memo[edges[i][1]].append((succProb[i], edges[i][0]))
        
        # If the start node has no neighbors, return 0 (no path exists)
        if not memo[start_node]:
            return 0

        # Push the start node into the priority queue with initial probability of 1
        # We use negative probabilities because heapq is a min-heap by default
        heappush(probabilities, (-1, start_node, set()))  # (probability, current_node, visited_nodes)

        # Perform a modified Dijkstra's algorithm to find the max probability path
        while probabilities:
            # Pop the node with the highest probability
            probability, nxt_node, seen = heappop(probabilities)
            probability = -probability  # Convert back to positive probability

            # If the current probability is less than the max found so far, exit early
            if probability < max_probability:
                break

            # Explore neighbors of the current node
            for nxt_prob, node in memo[nxt_node]:
                if node not in seen:  # Avoid visiting already seen nodes
                    # If the neighbor is the end node, update the max probability
                    if node == end_node:
                        max_probability = max(max_probability, probability * nxt_prob)
                    else:
                        # Otherwise, push the neighbor into the priority queue
                        # Update the probability and mark the node as visited
                        heappush(probabilities, (-probability * nxt_prob, node, seen | {node}))
        
        # Return the maximum probability to reach the end node
        return max_probability


            
        




        