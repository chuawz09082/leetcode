class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # Get the lengths of nums1 and nums2
        m = len(nums1)
        n = len(nums2)
        
        # Initialize a 2D DP table with dimensions (m+1) x (n+1)
        # dp[i][j] represents the length of the longest common subarray starting at nums1[i] and nums2[j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Variable to track the maximum length of a common subarray
        maxlength = 0

        # Iterate over nums1 and nums2 in reverse order
        # This ensures that we solve smaller subproblems before larger ones
        for i in range(m - 1, -1, -1):  # Loop over nums1
            for j in range(n - 1, -1, -1):  # Loop over nums2
                # If the current elements are equal, update dp[i][j]
                if nums1[i] == nums2[j]:
                    dp[i][j] = dp[i + 1][j + 1] + 1  # Extend the length by 1
                    maxlength = max(maxlength, dp[i][j])  # Update the maximum length found so far

        # Return the maximum length of a common subarray
        return maxlength
