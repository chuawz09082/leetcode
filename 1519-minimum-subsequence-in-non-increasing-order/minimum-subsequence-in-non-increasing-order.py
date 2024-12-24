class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        # Edge case: if the array has one or no elements, return it directly
        if len(nums) <= 1:
            return nums

        # Step 1: Sort the array in descending order
        nums.sort(reverse=True)
        
        # Step 2: Initialize the end of the subsequence
        end = 1
        
        # Step 3: Expand the subsequence until its sum is greater than the sum of the remaining elements
        while sum(nums[:end]) <= sum(nums[end:]):
            end += 1
        
        # Step 4: Return the subsequence
        return nums[:end]

        