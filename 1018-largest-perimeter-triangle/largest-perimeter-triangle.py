class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort(reverse = True)
        start = 0
        nxt = 1
        last = 2

        while last < len(nums) and (nums[start] + nums[nxt] <= nums[last] or nums[nxt] + nums[last] <= nums[start] or nums[start] + nums[last] <= nums[nxt]):
            start += 1
            nxt += 1
            last += 1
        
        if last == len(nums):
            return 0
        else:
            return nums[start] + nums[nxt]+nums[last]
        

        