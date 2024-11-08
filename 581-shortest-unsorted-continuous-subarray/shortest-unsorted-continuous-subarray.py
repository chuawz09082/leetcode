class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        # Create a sorted version of the array to compare with the original
        numssort = sorted(nums)
        
        # If the array is already sorted, return 0 (no need to sort any subarray)
        if numssort == nums:
            return 0
        
        # Initialize pointers for the left and right bounds of the subarray
        left = 0
        right = len(nums) - 1
        
        # Flags to track when the left and right boundaries are fixed
        fixleft = False
        fixright = False

        # Iterate from both ends of the array towards the center
        while left < right:
            # Move the left pointer rightward until finding a mismatch
            if not fixleft and nums[left] == numssort[left]:
                left += 1
            else:
                fixleft = True  # Fix the left boundary once a mismatch is found
            
            # Move the right pointer leftward until finding a mismatch
            if not fixright and nums[right] == numssort[right]:
                right -= 1
            else:
                fixright = True  # Fix the right boundary once a mismatch is found

            # If both boundaries are fixed, calculate the length of the unsorted subarray
            if fixleft and fixright:
                return right - left + 1  # Length of the unsorted subarray
            
        