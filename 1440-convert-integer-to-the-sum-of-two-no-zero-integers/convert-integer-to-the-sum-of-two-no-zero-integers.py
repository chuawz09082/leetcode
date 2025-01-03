class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        """
        Finds two integers `a` and `b` such that:
        - a + b = n
        - Neither `a` nor `b` contains the digit '0'.

        @param n: The target sum.
        @return: A list [a, b] of two integers satisfying the conditions.
        """
        # Initialize `start` to 1 and `end` to n-1
        start = 1
        end = n - 1

        # Iterate until both `start` and `end` do not contain the digit '0'
        while '0' in list(str(end)) or '0' in list(str(start)):
            # Increment `start` and decrement `end` to try the next pair
            start += 1
            end -= 1
        
        # Return the pair [start, end] that satisfies the conditions
        return [start, end]
        