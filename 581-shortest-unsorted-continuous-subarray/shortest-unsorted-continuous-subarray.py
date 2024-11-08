class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        numssort = sorted(nums)
        if numssort == nums:
            return 0
        left = 0
        right = len(nums)-1
        fixleft = False
        fixright = False

        while left < right:
            if not fixleft and nums[left] == numssort[left]:
                left += 1
            else:
                fixleft = True
            if not fixright and nums[right] == numssort[right]:
                right -= 1
            else:
                fixright = True
            if fixleft and fixright:
                return right-left+1
            
        