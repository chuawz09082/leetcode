class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1:
            return nums

        nums.sort(reverse = True)
        end = 1
        

        while sum(nums[:end]) <= sum(nums[end:]):
            end += 1
        return nums[:end]

        