class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:   
        # Step 1: Sort events by their start day
        events.sort(key=lambda x: x[0])

        # Step 2: Initialize a min-heap and variables to track days and attended events
        heap = []
        current_day = 0
        attended = 0
        i = 0
        n = len(events)

        # Step 3: Process events day by day
        while i < n or heap:
            # Move to the next day if the heap is empty
            if not heap:
                current_day = events[i][0]

            # Add all events starting on the current day to the heap
            while i < n and events[i][0] <= current_day:
                # Push the event's end day into the heap
                heapq.heappush(heap, events[i][1])
                i += 1

            # Remove events from the heap that are no longer valid (end day < current_day)
            while heap and heap[0] < current_day:
                heapq.heappop(heap)

            # Attend an event (the one that ends earliest)
            if heap:
                heapq.heappop(heap)  # Remove the event from the heap
                attended += 1  # Increment the count of attended events

            # Move to the next day
            current_day += 1

        return attended

            



            
