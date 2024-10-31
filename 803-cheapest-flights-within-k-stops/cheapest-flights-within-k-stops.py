
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # If the source and destination are the same, the cost is 0
        if src == dst:
            return 0

        # Dictionary to store direct flights, where keys are starting cities,
        # and values are lists of tuples (destination city, cost).
        flightdict = defaultdict(list)
        
        # Initialize a queue for BFS with the starting point (src),
        # -1 stops (because we haven't moved yet), and 0 cost.
        queue = deque([(src, -1, 0)])
        
        # Set the initial minimum price to infinity, representing no viable route yet.
        minprice = float('inf')
        
        # Dictionary to track the minimum cost for each (city, stops) combination.
        # This helps avoid revisiting more expensive routes.
        seen = {(src, -1): 0}

        # Populate the flight dictionary with the given flight data.
        for flight in flights:
            u, v, cost = flight
            flightdict[u].append((v, cost))
        
        # Perform BFS on the queue to explore all possible routes
        while queue:
            # Dequeue the current city, number of stops made so far, and the accumulated cost
            city, stops, cost = queue.popleft()

            # If the destination is reached within the allowed stops and with a lower cost, update minprice
            if city == dst and stops <= k and cost <= minprice:
                minprice = cost
                continue
            
            # If we've exceeded the maximum allowed stops, skip this path
            if stops + 1 > k:
                continue
            
            # Explore the neighboring cities (direct flights) from the current city
            for next_city, next_cost in flightdict[city]:
                # Calculate the total cost to reach the next city from the current city
                tmpcost = cost + next_cost

                # Continue if we already found a cheaper path to this city with the same stops,
                # or if the cost exceeds the current minimum price found.
                if ((next_city, stops + 1) in seen and seen[(next_city, stops + 1)] <= tmpcost) or tmpcost >= minprice:
                    continue
                
                # Update the minimum cost for reaching the next city with the current number of stops
                seen[(next_city, stops + 1)] = tmpcost
                
                # Enqueue the next city with the updated number of stops and cost
                queue.append((next_city, stops + 1, tmpcost))
                    
        # If we found a valid route to the destination, return the minimum price;
        # otherwise, return -1 to indicate it's unreachable within k stops.
        return minprice if minprice < float('inf') else -1

