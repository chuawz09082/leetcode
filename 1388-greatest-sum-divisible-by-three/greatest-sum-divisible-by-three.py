class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        nums.sort()
        if sum(nums)%3 == 0:
            return sum(nums)
        
        remaindict = collections.defaultdict(list)
        finalsum = sum(nums)


        for num in nums:
            if num%3 == 0:
                continue
            else:
                remaindict[num%3].append(num)
        
        if finalsum%3 == 1:
            poss1 = float('inf')
            poss2 = float('inf')
            if remaindict[1]:
                poss1 = remaindict[1][0]
            if len(remaindict[2]) > 1:
                poss2 = sum(remaindict[2][0:2])
            mindiff = min(poss1,poss2)
            finalsum -= mindiff
        
        else:
            poss1 = float('inf')
            poss2 = float('inf')
            if remaindict[2]:
                poss1 = remaindict[2][0]
            if len(remaindict[1]) > 1:
                poss2 = sum(remaindict[1][0:2])
            mindiff = min(poss1,poss2)
            finalsum -= mindiff

        return finalsum


