class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        # Initialize a dictionary to store lists of (worker, bike) pairs by their Manhattan distance
        distdict = collections.defaultdict(list)
        
        # Initialize the result list with None, where each index represents a worker
        # This list will eventually hold the assigned bike index for each worker
        result = [None] * len(workers)

        # Calculate the Manhattan distance between each worker and each bike
        for i in range(len(workers)):
            for j in range(len(bikes)):
                # Calculate Manhattan distance between worker[i] and bike[j]
                manh = abs(bikes[j][0] - workers[i][0]) + abs(bikes[j][1] - workers[i][1])
                # Add the (worker, bike) pair to the list associated with this distance in distdict
                distdict[manh].append((i, j))

        # Sort distdict by distance (key) and then by (worker, bike) pairs within each distance
        distdict = dict(sorted(distdict.items(), key=lambda item: (item[0], sorted(item[1]))))

        # Iterate through each sorted distance key in distdict
        for key in distdict.keys():
            values = distdict[key]  # Retrieve the list of (worker, bike) pairs for this distance
            for worker, bike in values:
                # Assign the bike to the worker if the worker has no bike and the bike is not assigned
                if result[worker] is None and bike not in result:
                    result[worker] = bike  # Assign bike to worker in the result list
        
        # Return the final list of assigned bikes for each worker
        return result



        