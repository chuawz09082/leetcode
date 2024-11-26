class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        """
        Determine if it is possible to pick up and drop off all passengers 
        according to the given trips within the vehicle's capacity.
        
        Args:
        trips (List[List[int]]): A list of trips where each trip is represented 
            as [num_passengers, start_location, end_location].
        capacity (int): The maximum number of passengers the vehicle can hold.

        Returns:
        bool: True if the trips can be completed within capacity, False otherwise.
        """
        # Step 1: Sort trips by start location and then by end location
        trips = sorted(trips, key=lambda x: (x[1], x[2]))
        
        # Step 2: Create a dictionary to store passengers starting at each location
        dict_trip = collections.defaultdict(list)
        last_idx = 0  # Track the last location where a trip ends

        # Populate the dictionary and find the farthest end location
        for trip in trips:
            dict_trip[trip[1]].append((trip[2], trip[0]))  # Map start location to (end location, num_passengers)
            if trip[2] > last_idx:
                last_idx = trip[2]  # Update the last index to the farthest drop-off point

        # Step 3: Initialize a min-heap to manage active trips
        heap = []
        heapq.heappush(heap, (trips[0][2], trips[0][0], trips[0][1]))  # Add the first trip
        current_idx = trips[0][1]  # Start processing from the first trip's start location
        current_capacity = capacity - trips[0][0]  # Update the current capacity after picking up passengers

        # Step 4: Iterate through all locations up to the last drop-off point
        while current_idx < last_idx and current_capacity >= 0:
            # Remove trips that have reached their end location
            while heap and heap[0][0] <= current_idx:
                current_capacity += heap[0][1]  # Add back the passengers from the completed trip
                heapq.heappop(heap)  # Remove the completed trip from the heap

            # Check if there are any trips starting at the current location
            if current_idx in dict_trip.keys():
                for i in range(len(dict_trip[current_idx])):
                    nxt_idx, passengers = dict_trip[current_idx][i][0], dict_trip[current_idx][i][1]

                    # If there is enough capacity, add the trip to the heap and update capacity
                    if current_capacity >= passengers and (nxt_idx, passengers, current_idx) not in heap:
                        heapq.heappush(heap, (nxt_idx, passengers, current_idx))
                        current_capacity -= passengers
                    # If there is not enough capacity, return False immediately
                    elif current_capacity < passengers and (nxt_idx, passengers, current_idx) not in heap:
                        return False
            
            # Move to the next location
            current_idx += 1

        # Step 5: Check if the trips can be completed with the remaining capacity
        if current_capacity >= 0:
            return True
        return False



        

        