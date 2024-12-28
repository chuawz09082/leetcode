class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array using the heap data structure.
        
        @param nums: List of integers to be sorted.
        @return: List of integers sorted in ascending order.
        """
        # Step 1: Convert the input list into a min-heap.
        # This rearranges the elements of nums so that the smallest element
        # is always at the root of the heap.
        heapq.heapify(nums)
        
        # Step 2: Initialize an empty list to store the sorted elements.
        heap = []
        
        # Step 3: Extract elements from the heap one by one.
        # Each time we pop from the heap, the smallest element is removed and added to 'heap'.
        while nums:
            curr = heapq.heappop(nums)  # Pop the smallest element from the heap
            heap.append(curr)           # Append it to the sorted result list
        
        # Step 4: Return the sorted list.
        return heap
        