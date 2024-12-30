class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        """
        Calculates the minimum time required for workers to level a mountain of a given height.
        Each worker contributes to reducing the mountain's height based on their worker time.

        @param mountainHeight: The initial height of the mountain to be leveled.
        @param workerTimes: A list where each element represents the time a worker takes for one shift.
        @return: The minimum time required to level the mountain.
        """

        # Initialize a priority queue (min-heap) to manage worker end times.
        # Each entry in the heap is a tuple (worker_end_time, current_shift, worker_index).
        workers_endtime = []

        # Populate the heap with the initial end time for each worker.
        # Each worker starts their first shift.
        for i in range(len(workerTimes)):
            heappush(workers_endtime, (workerTimes[i], 2, i))  # (end_time, next_shift_multiplier, worker_index)

        # Variable to track the minimum time required to level the mountain.
        mintime = 0

        # Variable to track the remaining height of the mountain.
        height = mountainHeight

        # Process the mountain height until it is completely leveled.
        while height > 0:
            # Pop the worker with the earliest end time from the heap.
            curr_endtime, curr_shift, curr_worker = heappop(workers_endtime)

            # Calculate the next end time and shift multiplier for the current worker.
            new_endtime = curr_endtime + curr_shift * workerTimes[curr_worker]
            new_shift = curr_shift + 1

            # Decrease the mountain's height by 1, as the current worker completes one shift.
            height -= 1

            # Push the updated end time and shift multiplier for the current worker back into the heap.
            heappush(workers_endtime, (new_endtime, new_shift, curr_worker))

            # Update the minimum time to reflect the latest end time.
            mintime = curr_endtime

        # Return the total time taken to level the mountain.
        return mintime
        