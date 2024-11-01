class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = nums[0]
        start = 0
        if len(nums) == 1:
            return True

        i =1

        while gas > 0:
            gas = max(gas-1,nums[i])
            if gas >= len(nums)-1-i:
                return True           
            i += 1
        return False
