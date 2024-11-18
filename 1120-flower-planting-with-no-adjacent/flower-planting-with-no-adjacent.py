class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        # If the number of gardens is less than or equal to 4, each can be assigned a unique flower
        if n <= 4:
            return list(range(1, n + 1))

        # Create a dictionary to represent the graph, where each garden points to its neighbors
        pathsdict = collections.defaultdict(list)
        for g1, g2 in paths:
            pathsdict[g1].append(g2)
            pathsdict[g2].append(g1)

        # Initialize an array to store the flower type for each garden
        flowers = [0 for _ in range(n)]  # 0 means no flower assigned yet
        # List of garden indices
        numbers = list(range(n))
        # Start with the first garden
        number = numbers.pop(0)

        # Assign flowers until all gardens have been assigned a flower
        while flowers.count(0) > 0:
            # Find the next garden without a flower
            while flowers[number] != 0:
                number = numbers.pop(0)
            # Get all neighbors of the current garden
            neighbours = pathsdict[number + 1]
            # Initialize the list of flower types to choose from (1 to 4)
            chooseflower = list(range(1, 5))

            # Check the flowers assigned to the neighbors
            for neighbour in neighbours:
                neighborflower = flowers[neighbour - 1]
                # If the neighbor has a flower, remove that option from the available flowers
                if neighborflower != 0 and neighborflower in chooseflower:
                    chooseflower.remove(neighborflower)
            # Assign the first available flower to the current garden
            flowers[number] = chooseflower[0]

        # Return the flower assignments for all gardens
        return flowers
        