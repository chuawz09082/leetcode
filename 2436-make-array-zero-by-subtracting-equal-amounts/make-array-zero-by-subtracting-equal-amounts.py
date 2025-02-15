class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # Count the occurrences of each unique number in the array
        count = Counter(nums)

        # If zero exists in the array, it doesn't contribute to operations,
        # so we exclude it from the count of unique numbers.
        if 0 in count.keys():
            return len(count.keys()) - 1  # Subtract one to ignore zero
        else:
            return len(count.keys())  # Return the number of unique non-zero elements

        