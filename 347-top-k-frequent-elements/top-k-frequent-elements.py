class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Create a dictionary to count the frequency of each number
        countdict = collections.defaultdict(int)

        # Iterate through the list and update the frequency count for each number
        for num in nums:
            countdict[num] += 1
        
        # Sort the dictionary by frequency in descending order
        # The key is the frequency (negative to ensure descending order)
        countdict = dict(sorted(countdict.items(), key=lambda x: -x[1]))

        # Initialize an empty list to store the result
        result = []

        # Iterate through the sorted dictionary and collect the top k frequent elements
        for key in countdict.keys():
            result.append(key)  # Add the current key to the result list
            if len(result) == k:  # Stop once we have k elements
                break
        
        # Return the list of the top k frequent elements
        return result
