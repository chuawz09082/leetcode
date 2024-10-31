class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        # Sort the greed factors of the children and the sizes of the cookies in ascending order
        g.sort()
        s.sort()
        
        # Initialize a pointer to keep track of the number of content children
        start = 0

        # Iterate over each cookie size in `s`
        for i in range(len(s)):
            # If all children are content, return the count
            if start == len(g):
                return start
            
            # If the largest cookie (s[-1]) is smaller than the smallest uncontent child (g[start]), stop
            if s[-1] < g[start]:
                break
            
            # If the current cookie size satisfies the current child’s greed factor
            if s[i] >= g[start]:
                # Move to the next child
                start += 1

        # Return the total number of content children
        return start
        
        
        