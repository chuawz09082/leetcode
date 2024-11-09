class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        # Sort the numbers to make processing smaller remainders easier
        nums.sort()
        
        # If the total sum of the numbers is divisible by 3, return it as is
        if sum(nums) % 3 == 0:
            return sum(nums)
        
        # Create a dictionary to group numbers by their remainder when divided by 3
        remaindict = collections.defaultdict(list)
        
        # Calculate the initial sum of the array
        finalsum = sum(nums)

        # Populate remaindict with numbers grouped by their remainders
        for num in nums:
            if num % 3 == 0:
                continue  # Skip numbers that are already divisible by 3
            else:
                remaindict[num % 3].append(num)

        # Case 1: If the sum leaves a remainder of 1 when divided by 3
        if finalsum % 3 == 1:
            poss1 = float('inf')  # Initialize as infinity to find the minimum difference
            poss2 = float('inf')  # Another possibility with two numbers of remainder 2

            # Find the smallest number with remainder 1, if available
            if remaindict[1]:
                poss1 = remaindict[1][0]
            
            # Find the sum of the two smallest numbers with remainder 2, if available
            if len(remaindict[2]) > 1:
                poss2 = sum(remaindict[2][0:2])
            
            # Choose the smallest difference that can make the sum divisible by 3
            mindiff = min(poss1, poss2)
            finalsum -= mindiff  # Subtract the minimum difference from the final sum
        
        # Case 2: If the sum leaves a remainder of 2 when divided by 3
        else:
            poss1 = float('inf')  # Minimum single number with remainder 2
            poss2 = float('inf')  # Sum of two smallest numbers with remainder 1

            # Find the smallest number with remainder 2, if available
            if remaindict[2]:
                poss1 = remaindict[2][0]
            
            # Find the sum of the two smallest numbers with remainder 1, if available
            if len(remaindict[1]) > 1:
                poss2 = sum(remaindict[1][0:2])
            
            # Choose the smallest difference that can make the sum divisible by 3
            mindiff = min(poss1, poss2)
            finalsum -= mindiff  # Subtract the minimum difference from the final sum

        # Return the maximum sum that is divisible by 3
        return finalsum


