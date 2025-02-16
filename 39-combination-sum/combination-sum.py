class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
       # Dictionary to store unique combinations for each sum
        memo = defaultdict(set)

        # Get the smallest candidate number to determine the iteration range
        minnum = min(candidates)

        # Iterate from the smallest candidate number up to the target
        for num in range(minnum, target + 1):
            # If `num` is a candidate itself, store it as a valid combination
            if num in candidates:
                memo[num].add((num,))  # Store as a tuple for uniqueness

            # Iterate from `num-1` down to `num//2`, trying to break `num` into two parts
            for nxt in range(num - 1, num // 2 - 1, -1):
                firstnum = memo[nxt]  # Get stored combinations for `nxt`
                secondnum = memo[num - nxt]  # Get stored combinations for `num - nxt`

                # If both parts have valid combinations, merge them
                if firstnum and secondnum:
                    combinations = [
                        tuple(sorted(list(x) + list(y)))  # Sort and merge unique combinations
                        for x in firstnum
                        for y in secondnum
                    ]
                    memo[num].update(combinations)  # Store merged combinations in `memo`

        # Retrieve the final unique combinations for `target`
        result = memo[target]

        # Convert tuples back to lists and return the final result
        return [list(x) for x in result]
