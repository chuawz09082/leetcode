import bisect

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        # Check if the array has an odd length or if there's an odd count of zeros
        # In either case, it's impossible to reorder the array as required, so return False
        if len(arr) % 2 == 1 or arr.count(0) % 2 == 1:
            return False

        # Sort the array to handle negatives and positives separately
        arr.sort()

        # Find the index of the first non-negative number using bisect
        index = bisect.bisect_left(arr, 0)
        
        # Split the array into negatives (in reverse order) and non-negative numbers
        ngvarr = sorted(arr[:index], reverse=True)
        posarr = arr[index:]

        # If the number of negative elements is odd, it's impossible to pair them, so return False
        if len(ngvarr) % 2 == 1:
            return False

        # Initialize result arrays to track pairs (for both negative and positive arrays)
        ngvresult = [None] * len(arr)
        posresult = [None] * len(arr)

        # Process non-negative elements to form pairs
        startpos = 0
        while posarr:
            # Get the smallest remaining value in posarr
            minvalue = posarr.pop(0)
            posresult[startpos] = minvalue

            # Check if there's a double for the current value
            if 2 * minvalue in posarr:
                # Find the index of the double and add it to the result array
                nxtidx = posarr.index(2 * minvalue)
                posresult[startpos + 1] = posarr.pop(nxtidx)
            else:
                # If no double is found, return False
                return False
            # Move to the next position and re-sort posarr
            startpos += 2
            posarr.sort()

        # Process negative elements similarly, ensuring reverse pairing
        startpos = 0
        while ngvarr:
            # Get the largest remaining negative value
            maxvalue = ngvarr.pop(0)
            ngvresult[startpos] = maxvalue

            # Check if there's a double for the current negative value
            if 2 * maxvalue in ngvarr:
                # Find the index of the double and add it to the result array
                nxtidx = ngvarr.index(2 * maxvalue)
                ngvresult[startpos + 1] = ngvarr.pop(nxtidx)
            else:
                # If no double is found, return False
                return False
            # Move to the next position and re-sort ngvarr in descending order
            startpos += 2
            ngvarr.sort(reverse=True)

        # Check if all slots in result arrays are filled, meaning successful pairing
        if posresult.count(None) + ngvresult.count(None) == len(arr):
            return True
        return False





        