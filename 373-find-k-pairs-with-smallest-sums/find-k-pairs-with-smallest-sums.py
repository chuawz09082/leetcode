class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        if not nums1 or not nums2 or k == 0:
            return []
        
        # Min-heap to store pairs (sum, i, j)
        heap = []
        # Push the first `min(k, len(nums2))` pairs (nums1[0] + nums2[j], 0, j)
        for j in range(min(k, len(nums2))):
            heapq.heappush(heap, (nums1[0] + nums2[j], 0, j))
        
        # Result list
        result = []
        
        # Extract k smallest pairs
        while heap and len(result) < k:
            sum_, i, j = heapq.heappop(heap)
            result.append([nums1[i], nums2[j]])
            # Push the next pair (nums1[i+1] + nums2[j], i+1, j) if within bounds
            if i + 1 < len(nums1):
                heapq.heappush(heap, (nums1[i+1] + nums2[j], i + 1, j))
        
        return result
        