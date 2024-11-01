class Solution:
    def smallestFactorization(self, num: int) -> int:
        # If the number is less than 10, return it directly as it's already a single digit.
        if num < 10:
            return num
        
        factors = []  # List to store the factors that will form the smallest number.
        start = 9     # Start trying to divide by the largest possible digit.
        remain = num  # Variable to track the remaining value after each division.

        # Attempt to factorize `num` by dividing by digits from 9 down to 2.
        while remain > 1:
            # If `remain` is not divisible by any prime factor (2, 3, 5, or 7),
            # it cannot be represented as a product of digits from 1 to 9.
            if remain % 2 != 0 and remain % 3 != 0 and remain % 5 != 0 and remain % 7 != 0:
                return 0
            # Divide `remain` by `start` as many times as possible, adding `start` to `factors` each time.
            while remain % start == 0:
                factors.append(start)
                remain = remain // start
            # Decrease `start` to check the next smaller digit.
            start -= 1

        output = 0  # Variable to build the final number from factors.
        # Construct the smallest number by ordering factors in reverse.
        for n in factors[::-1]:
            output = output * 10 + n  # Build the number digit-by-digit.
            # If output exceeds 32-bit integer limit, return 0 as per problem constraints.
            if output > 2147483647:
                return 0

        return output


        