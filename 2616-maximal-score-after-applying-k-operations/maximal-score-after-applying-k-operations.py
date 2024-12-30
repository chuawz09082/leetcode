class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        """
        Calculates the maximum score achievable by performing at most k operations 
        on the elements of the array. In each operation, the largest element is selected, 
        added to the score, and replaced with its value divided by 3 (rounded up).

        @param nums: List of integers representing the elements of the array.
        @param k: Maximum number of operations allowed.
        @return: The maximum score achievable.
        """
        # Step 1: Convert all elements in nums to negative values to simulate a max-heap
        # (since Python's heapq implements a min-heap by default).
        copy_nums = [-num for num in nums]
        heapify(copy_nums)  # Transform the list into a heap.

        # Initialize variables to track the score and the number of operations performed.
        score = 0  # The cumulative score.
        operations = 0  # Number of operations performed.

        # Step 2: Perform operations until the maximum limit (k) is reached.
        while operations < k:
            # Pop the largest element from the heap (convert it back to positive).
            curr_score = heappop(copy_nums)
            
            # Add the absolute value of the current largest element to the score.
            score -= curr_score  # Subtract because the heap contains negative values.
            
            # Push the current element back into the heap after dividing it by 3
            # (rounding up to the nearest integer) and negating it for the max-heap simulation.
            heappush(copy_nums, -ceil(-curr_score / 3))
            
            # Increment the operation count.
            operations += 1

        # Step 3: Return the total score after performing all operations.
        return score
        