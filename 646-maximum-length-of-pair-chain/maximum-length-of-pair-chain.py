class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Sort pairs based on the first element, and then by the second element
        # This helps to process the pairs in a sequential order
        pairs = sorted(pairs, key=lambda x: (x[0], x[1]))
        
        # Initialize a list to hold chains of pairs and track the maximum length
        lst = []
        length = len(pairs)
        maxlength = 0

        # Iterate over each pair in the sorted list
        for i in range(length):
            pair = pairs[i]
            
            # If the list of chains is empty, start a new chain with the current pair
            if not lst:
                lst.append([pair])
                maxlength = 1  # Set the initial maximum chain length to 1
                continue  # Move to the next pair

            added = False  # Track whether the current pair was added to an existing chain

            # Iterate over existing chains in lst
            for j in range(len(lst)):
                tmp = lst[j]  # Temporary reference to the current chain
                
                # Check if the current pair can be appended to the current chain
                if tmp[-1][1] < pair[0]:
                    tmp.append(pair)  # Append the pair to the chain
                    added = True
                
                # If the current pair’s second element is smaller, replace the last pair
                # This keeps the chain ending as small as possible for potential additions
                elif tmp[-1][1] > pair[1]:
                    tmp.pop()  # Remove the last pair in the chain
                    tmp.append(pair)  # Add the current pair to minimize the end value
                    added = True
                
                # Update the maximum chain length if the current chain length is the longest
                if len(tmp) > maxlength:
                    maxlength = len(tmp)
            
            # If the current pair could not be added to any chain, start a new chain
            if not added:
                lst.append([pair])
        
        # Return the length of the longest chain found
        return maxlength


