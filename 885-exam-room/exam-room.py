class ExamRoom:

    def __init__(self, n: int):
        """
        Initialize the ExamRoom with `n` seats.
        """
        self.n = n  # Total number of seats
        self.heap = []  # List to store occupied seats in sorted order

    def seat(self) -> int:
        """
        Allocate a seat to a student such that the distance to the closest 
        occupied seat is maximized.
        """
        if not self.heap:
            # If no seats are occupied, allocate seat 0
            self.heap.append(0)
            return 0

        # Initialize the variables to track the best seat and maximum distance
        seat = 0
        max_distance = self.heap[0]  # Distance from seat 0 to the first occupied seat

        # Calculate maximum distance between consecutive occupied seats
        for i in range(len(self.heap) - 1):
            prev_seat = self.heap[i]  # Current occupied seat
            next_seat = self.heap[i + 1]  # Next occupied seat
            distance = (next_seat - prev_seat) // 2  # Midpoint between two seats
            if distance > max_distance:
                # Update the best seat and the maximum distance
                seat = prev_seat + distance
                max_distance = distance

        # Check the distance from the last occupied seat to the end of the row
        if self.n - 1 - self.heap[-1] > max_distance:
            # If this distance is greater, allocate the last seat
            seat = self.n - 1

        # Add the allocated seat to the occupied list and keep it sorted
        self.heap.append(seat)
        self.heap.sort()

        return seat

    def leave(self, p: int) -> None:
        """
        A student leaves seat `p`, freeing it up.
        """
        self.heap.remove(p)  # Remove the seat `p` from the occupied list

        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)