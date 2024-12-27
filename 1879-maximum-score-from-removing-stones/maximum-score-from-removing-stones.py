class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # Create a max-heap by storing the negative values of a, b, and c
        # Python's heapq implements a min-heap by default, so using negatives simulates a max-heap
        heap = [-a, -b, -c]
        heapq.heapify(heap)  # Convert the list into a heap structure

        score = 0  # Initialize the score to count the number of moves

        # Continue until fewer than two piles remain
        while len(heap) > 1:
            # Pop the two largest piles (stored as negatives, so negate them back to positive)
            largest = -heapq.heappop(heap)
            second_largest = -heapq.heappop(heap)

            # Increment the score as one stone is removed from each of the two largest piles
            score += 1

            # If the largest pile still has stones after removing one, push it back into the heap
            if largest - 1 > 0:
                heapq.heappush(heap, -(largest - 1))  # Push the decremented value as negative

            # If the second-largest pile still has stones after removing one, push it back into the heap
            if second_largest - 1 > 0:
                heapq.heappush(heap, -(second_largest - 1))  # Push the decremented value as negative
        
        # Return the total score, which is the maximum number of moves possible
        return score



            
            

        




        