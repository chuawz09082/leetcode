class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert the number to a list of its digits as strings
        lst = list(str(num))
        
        # Create a sorted version of the list in descending order to determine the maximum possible arrangement
        lstsort = sorted(lst, reverse=True)
        
        # Initialize maxdgt to None, which will store the first digit that should be swapped
        maxdgt = None
        
        # Find the first digit that is out of place by comparing `lst` and `lstsort`
        for i in range(len(lst)):
            # Identify the first index where the current digit does not match the sorted list's digit
            if lst[i] != lstsort[i]:
                maxdgt = int(lstsort[i])  # This is the maximum digit that we want to bring to this position
                break

        # If the digits are already in their maximum arrangement, return the original number
        if maxdgt is None:
            return num

        # List to track all indices of the maximum digit `maxdgt` in the original list
        maxindex = []
        
        # Variable to store the first index where a swap should happen to maximize the number
        swap = None
        
        # Iterate through the list again to locate possible swap indices
        for i in range(len(lst)):
            # Collect all indices of `maxdgt` in the list
            if int(lst[i]) == maxdgt:
                maxindex.append(i)
            # Identify the first position where the current digit is smaller than `maxdgt` (potential swap position)
            if swap is None and int(lst[i]) < maxdgt:
                swap = i

        # Get the last occurrence of the maximum digit for optimal swapping
        maxswapidx = max(maxindex)

        # Form the new list by swapping `swap` and `maxswapidx` positions to achieve the maximum number
        newlst = (
            lst[:swap] +  # Digits before the swap index
            lst[maxswapidx:maxswapidx+1] +  # Insert the maximum digit at the swap position
            lst[swap+1:maxswapidx] +  # Digits between `swap` and `maxswapidx`
            lst[swap:swap+1] +  # Insert the original digit at the maximum digit's position
            lst[maxswapidx+1:]  # Digits after the maxswap index
        )

        # Convert the list of characters back to an integer and return the result
        return int("".join(newlst))
        


        
        
        

        