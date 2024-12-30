class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        intnums = sorted(list(map(int,nums)),reverse = True)
        return str(intnums[k-1])
        