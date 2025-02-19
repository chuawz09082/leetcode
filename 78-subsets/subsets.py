class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # Initialize a list to store subsets
        current = []
        
        # Iterate through each number in the input list
        for num in nums:
            nxtlevel = []  # Temporary list to store new subsets created in this iteration
            
            # Iterate through existing subsets and add the current number to create new subsets
            for i in range(len(current)):
                nxtlevel.append(current[i] + [num])  # Append the new subset
            
            # Add the single-element subset containing only the current number
            current.append([num])
            
            # Extend the current list with the newly generated subsets
            current += nxtlevel
        
        # Add the empty subset (which is always part of the power set)
        current += [[]]
        
        # Return the list of all subsets
        return current
        