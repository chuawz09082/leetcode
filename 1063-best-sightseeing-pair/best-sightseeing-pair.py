class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        """
        Finds the maximum score of a sightseeing pair, where the score is defined as:
        score(i, j) = values[i] + values[j] + i - j with i < j.

        @param values: List[int] - A list of integers representing the values of sightseeing points.
        @return: int - The maximum score for a pair of sightseeing points.
        """

        length = len(values)  # Length of the input list
        max_score = 0  # Initialize the maximum score to 0

        # Step 1: Compute `left_max`, which stores the maximum contribution from the left
        # for each index. This considers the formula `values[k] + k - 1` for k < i.
        left_max = [0] * length
        for i in range(1, length):
            # Update the left maximum contribution up to index `i`.
            # `values[i-1] - 1` represents the score from the previous value, accounting for the distance penalty.
            # `left_max[i-1] - 1` ensures we propagate the maximum score seen so far with the distance penalty.
            left_max[i] = max(values[i - 1] - 1, left_max[i - 1] - 1)
            # Update the maximum score by combining the current value and the best left contribution.
            max_score = max(values[i] + left_max[i], max_score)

        # Step 2: Compute `right_max`, which stores the maximum contribution from the right
        # for each index. This considers the formula `values[k] - k - 1` for k > i.
        right_max = [0] * length
        for i in range(length - 2, -1, -1):
            # Update the right maximum contribution from index `i` onwards.
            # `values[i+1] - 1` represents the score from the next value, accounting for the distance penalty.
            # `right_max[i+1] - 1` ensures we propagate the maximum score seen so far with the distance penalty.
            right_max[i] = max(right_max[i + 1] - 1, values[i + 1] - 1)
            # Update the maximum score by combining the current value and the best right contribution.
            max_score = max(values[i] + right_max[i], max_score)

        # Step 3: Return the maximum score achieved.
        return max_score

        