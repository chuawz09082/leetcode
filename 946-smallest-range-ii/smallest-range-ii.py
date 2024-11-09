class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        nums.sort()
        minnum,maxnum = nums[0],nums[-1]
        ans = maxnum - minnum

        for i in range(len(nums)-1):
            a,b = nums[i],nums[i+1]
            ans = min(ans,max(maxnum-k,a+k) - min(minnum+k,b-k))
        return ans


        