class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # Sort the list in ascending order
        nums.sort()
        
        # Initialize result to store the sum of minimum pairs
        result = 0
        
        # Iterate over the sorted list, selecting every second element starting from index 0
        # This effectively adds the smaller number from each consecutive pair
        for i in range(0, len(nums), 2):
            result += nums[i]
        
        # Return the total sum of minimum values from each pair
        return result
        