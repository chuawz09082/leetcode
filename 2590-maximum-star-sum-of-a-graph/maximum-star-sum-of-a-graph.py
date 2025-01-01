class Solution:
    def maxStarSum(self, vals: List[int], edges: List[List[int]], k: int) -> int:
        """
        Calculates the maximum star sum of a graph with node values and edges.
        A star graph consists of a center node and its connected neighbors. The sum
        is calculated using the node value of the center and the top-k highest
        neighbor values (if positive).

        @param vals: List of integers representing node values.
        @param edges: List of edges where each edge connects two nodes.
        @param k: Maximum number of neighbors to consider for the sum.
        @return: The maximum star sum possible.
        """
        # Dictionary to store the neighbors' values for each node
        memo = collections.defaultdict(list)
        
        # Min-heap to prioritize nodes based on their values for processing
        values = []
        
        # Set to track seen nodes (to avoid duplicates in the heap)
        seen = set()

        # Edge case: If there are no edges, return the maximum node value
        if not edges:
            return max(vals)

        # Step 1: Populate `memo` with neighbor values and build the `values` heap
        for edge in edges:
            # Add the negative values of neighbors (to simulate max-heap behavior with heapq)
            if vals[edge[1]] > 0:
                heappush(memo[edge[0]], -vals[edge[1]])
            if vals[edge[0]] > 0:
                heappush(memo[edge[1]], -vals[edge[0]])

            # Add nodes to the heap for processing
            if edge[0] not in seen:
                seen.add(edge[0])
                heappush(values, (-vals[edge[0]], edge[0]))
            if edge[1] not in seen:
                seen.add(edge[1])
                heappush(values, (-vals[edge[1]], edge[1]))

        # Initialize the maximum star sum
        maxvalue = -float('inf')

        # Edge case: If no neighbors are stored, return the maximum node value
        if not memo:
            return max(vals)

        # Step 2: Process each node in the `values` heap
        while values:
            # Get the current node with the largest value
            startvalue, startnode = heappop(values)

            # Get the top-k smallest (i.e., largest positive) neighbors for the node
            nextnodes = heapq.nsmallest(min(k, len(memo[startnode])), memo[startnode])

            # Calculate the total value of the star (node + neighbors)
            totalvalue = -startvalue - sum(nextnodes)

            # Update the maximum star sum if the current star's value is larger
            if totalvalue > maxvalue:
                maxvalue = totalvalue

        # Return the maximum star sum
        return maxvalue


        