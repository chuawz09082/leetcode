class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        
        if min(nums) > target:
            return 0
        
        hash = [0 for _ in range(target+1)]

        for num in nums:
            if num <= target:
                hash[num] += 1

        for pos in range(nums[0], target):
            if hash[pos] == 0:
                continue
            for num in nums:
                if pos+num <= target:
                    hash[pos+num] += hash[pos]
                else:
                    break

        return hash[target]