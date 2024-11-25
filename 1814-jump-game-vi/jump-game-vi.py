class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # Max-heap to store (-score, index) for max-priority retrieval
        heap = [(-nums[0], 0)]  # Start with the first element
        n = len(nums)
        
        for i in range(1, n):
            # Ensure the top of the heap is within the range of `k`
            while heap[0][1] < i - k:
                heapq.heappop(heap)
            
            # Get the maximum score so far and add the current value
            max_score = -heap[0][0]
            nums[i] += max_score  # Update the current index with the best score so far
            
            # Push the current score and index into the heap
            heapq.heappush(heap, (-nums[i], i))
        
        # The last element in nums contains the maximum score to reach the end
        return nums[-1]