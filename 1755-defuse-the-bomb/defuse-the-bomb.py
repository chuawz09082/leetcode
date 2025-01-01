class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        """
        Decrypts a circular code based on the given rules.
        
        @param code: List of integers representing the circular code.
        @param k: Integer determining the direction and range of decryption.
        @return: List of integers representing the decrypted code.
        """

        # If k is 0, replace every element in `code` with 0.
        if k == 0:
            return [0 for _ in range(len(code))]

        # Calculate the base sum for the circular range repetition.
        # This is the total contribution of multiple complete rounds of `code` in `k`.
        basesum = (abs(k) // len(code)) * sum(code)

        # Initialize the result list with the base sum for each index.
        result = [basesum for _ in range(len(code))]

        # Create a copy of `code` concatenated with itself for easy circular access.
        copy_code = code + code

        # Determine the starting index and direction based on the sign of `k`.
        if k < 0: 
            # If k is negative, start from the end of the original array.
            start = len(code)
            add = -1  # Move in the negative direction.
        else:
            # If k is positive, start from the beginning.
            start = 0
            add = 1  # Move in the positive direction.

        # Adjust k to represent the effective range within the circular list.
        k = ((add * k) % len(code)) * add

        # Compute the initial sum for the first element in the result list.
        # This sum includes elements from `start + add` to `start + k + add`.
        startsum = sum(copy_code[start + add : start + k + add : add])
        result[0] += startsum

        # Iterate through the rest of the elements in the `code`.
        for i in range(1, len(code)):
            if k > 0:
                # If k is positive, update the window sum by adding the new element
                # and removing the leftmost element from the previous window.
                startsum += copy_code[start + k + add + i - 1] - copy_code[start + add + i - 1]
            else:
                # If k is negative, update the window sum by subtracting the new element
                # and adding the leftmost element from the previous window.
                startsum += -copy_code[start + k + add + i] + copy_code[start + add + i]

            # Update the result for the current index.
            result[i] += startsum

        # Return the decrypted code.
        return result

        
        