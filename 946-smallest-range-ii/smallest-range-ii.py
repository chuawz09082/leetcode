class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Sort the array to make it easier to work with neighboring elements
        nums.sort()
        
        # Initialize minnum and maxnum to the smallest and largest elements in the sorted array
        minnum, maxnum = nums[0], nums[-1]
        
        # Calculate the initial range (difference between max and min values)
        ans = maxnum - minnum

        # Iterate over each element except the last one
        for i in range(len(nums) - 1):
            # `a` is the current element and `b` is the next element in the sorted array
            a, b = nums[i], nums[i + 1]
            
            # Calculate the new potential maximum by reducing `maxnum` by `k` or increasing `a` by `k`
            # Calculate the new potential minimum by increasing `minnum` by `k` or reducing `b` by `k`
            # This simulates adjusting each element by +/- k to minimize the range
            new_max = max(maxnum - k, a + k)
            new_min = min(minnum + k, b - k)
            
            # Update `ans` with the minimum range found so far
            ans = min(ans, new_max - new_min)
        
        # Return the minimum possible range
        return ans


        