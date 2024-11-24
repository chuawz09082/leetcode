class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Create a min-heap
        heap = []
        
        for num in nums:
            heapq.heappush(heap, num)  # Add the element to the heap
            if len(heap) > k:
                heapq.heappop(heap)  # Remove the smallest element if heap size exceeds k
        # The root of the heap is the k-th largest element
        return heap[0]