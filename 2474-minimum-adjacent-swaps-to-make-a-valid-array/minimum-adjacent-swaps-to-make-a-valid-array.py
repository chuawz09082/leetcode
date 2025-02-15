class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        n = len(nums)  # Get the length of the array
        low = min(nums)  # Find the minimum value in the array
        high = max(nums)  # Find the maximum value in the array
        
        # If all elements are the same, no swaps are needed
        if low == high:
            return 0

        # Find the index of the first occurrence of the minimum value
        low_idx = nums.index(low)

        # Find the index of the last occurrence of the maximum value
        # We reverse the array to get the last occurrence easily and adjust the index
        high_idx = n - nums[::-1].index(high) - 1  

        # If the smallest element appears before the largest, simple sum of swaps
        if low_idx < high_idx:
            return low_idx + n - high_idx - 1
        else:  # If the smallest element appears after or at the same index as the largest, adjust for one overlap
            return low_idx + n - high_idx - 2
        