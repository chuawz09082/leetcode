class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        # Initialize an empty list to store the factors of n
        factors = []

        # Iterate through all numbers from 1 to n (inclusive)
        for num in range(1, n + 1):
            # Check if num is a factor of n (i.e., divides n without leaving a remainder)
            if n % num == 0:
                factors.append(num)  # If so, add it to the list of factors
            if len(factors) == k:
                break

        # Check if there are at least k factors
        if len(factors) == k:
            # If yes, return the k-th factor (1-based index, so we use k-1 for 0-based indexing)
            return factors[k - 1]
        else:
            # If there are fewer than k factors, return -1 to indicate it doesn't exist
            return -1
        