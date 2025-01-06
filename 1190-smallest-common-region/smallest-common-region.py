class Solution:
    def findSmallestRegion(self, regions: List[List[str]], region1: str, region2: str) -> str:
        """
        Finds the smallest common region that contains both region1 and region2.
        
        @param regions: A list of lists, where each sublist contains a region and its subregions.
        @param region1: The name of the first region.
        @param region2: The name of the second region.
        @return: The name of the smallest common region that contains both region1 and region2.
        """
        
        # Dictionary to store the parent of each region.
        memo = {}

        # Process the input regions to populate the parent-child relationships in `memo`.
        for region in regions:
            # The first element of each sublist is the parent region.
            # All subsequent elements are its subregions.
            for i in range(1, len(region)):
                memo[region[i]] = region[0]
        
        # Lists to store the hierarchy (parent chain) of region1 and region2.
        parents1 = [region1]
        parents2 = [region2]

        # Build the parent chain for region1 until we reach the root.
        while parents1[-1] in memo.keys():
            # Append the parent of the last region in the chain.
            parents1.append(memo[parents1[-1]])

        # Build the parent chain for region2 until we find a common parent with region1.
        while parents2[-1] not in parents1:
            # Append the parent of the last region in the chain.
            parents2.append(memo[parents2[-1]])
        
        # The last region in parents2 is the smallest common region.
        return parents2[-1]