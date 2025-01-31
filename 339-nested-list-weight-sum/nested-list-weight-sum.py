# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        Computes the sum of all integers in the nested list, weighted by their depth.
        
        :param nestedList: A list of NestedInteger objects, which can be either an integer or a nested list.
        :return: The weighted sum of all integers in the list, where each integer is multiplied by its depth.
        """
        
        def helper(lst, depth):
            """
            Recursively calculates the weighted sum of integers in the nested list.
            
            :param lst: A NestedInteger object that could be an integer or a nested list.
            :param depth: The current depth level in the nested structure.
            :return: The sum of all integers in 'lst', each multiplied by its corresponding depth.
            """
            # Base case: If the element is an integer, return its value multiplied by its depth
            if lst.isInteger():
                return lst.getInteger() * depth
            
            # Recursive case: If it's a nested list, retrieve the list and process each element
            nxtlist = lst.getList()
            
            # Apply recursion to each element in the list, increasing the depth
            return sum([helper(nxtlist[i], depth + 1) for i in range(len(nxtlist))])

        # Start recursion for each element in the top-level list, starting at depth 1
        return sum([helper(nestedList[i], 1) for i in range(len(nestedList))])

        