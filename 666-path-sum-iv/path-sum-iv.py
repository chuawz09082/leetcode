class Solution:
    def pathSum(self, nums: List[int]) -> int:
        # Sort numbers in descending order to process from leaf nodes to root
        nums.sort(reverse=True)
        
        # List to store paths from leaf to root in reverse order
        listnums = []
        
        # Maximum depth of the tree, derived from the first (largest) element in nums
        maxdepth = nums[0] // 100
        
        # Initialize path sum to accumulate the sum of values for all paths
        pathsum = 0

        # Iterate through each number in the sorted nums
        for num in nums:
            # If the current node is at the maximum depth (leaf node)
            if num // 100 == maxdepth:
                listnums.append([num])  # Start a new path with this leaf node
                pathsum += num % 10     # Add the node's value to the path sum
                continue  # Move to the next node in nums

            # Count to track connections to children in the existing paths
            countnum = 0

            # Traverse the list of paths to check for valid connections from the current node
            for j in range(len(listnums)):
                # Check if the current node is the parent of the last node in listnums[j]
                # Conditions: Same level difference, valid parent-child positioning in the tree
                if ((listnums[j][-1] // 10) % 10 == 2 * ((num // 10) % 10) or
                    (listnums[j][-1] // 10) % 10 == 2 * ((num // 10) % 10) - 1) and \
                   listnums[j][-1] // 100 == num // 100 + 1:
                    
                    listnums[j].append(num)  # Append current node to the path
                    pathsum += num % 10      # Add the node's value to path sum
                    countnum += 1            # Increment count of valid connections
                    
                    # If the current node has connected all valid paths for its level, break
                    if countnum == 2 ** (maxdepth - num // 100):
                        break

            # If no paths were found for the current node, start a new path with it
            if countnum == 0:
                listnums.append([num])
                pathsum += num % 10  # Add value of the current node to path sum

        # Return the accumulated path sum for all paths from root to leaf
        return pathsum
        



        