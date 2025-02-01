class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # Edge case: If the input string is empty, return an empty list
        if not digits:
            return []
            
        # Mapping of digits to corresponding letters as per the phone keypad
        memo = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        
        # Initialize the result list with the letters corresponding to the first digit
        current = memo[int(digits[0])]
        start = 1  # Start processing from the second digit

        # Iterate through the remaining digits
        while start < len(digits):
            nxtlevel = []  # Temporary list to store combinations for the current digit
            
            # For each combination so far (current), append letters corresponding to the new digit
            for i in range(len(current)):
                for j in range(len(memo[int(digits[start])])):
                    # Concatenate the current combination with each possible letter of the new digit
                    nxtlevel.append(current[i] + memo[int(digits[start])][j])
            
            # Move to the next digit
            start += 1
            # Update the current list with new combinations
            current = nxtlevel
        
        # Return the final list of combinations
        return current

        