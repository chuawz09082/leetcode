class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Create a copy of nums1 to avoid modifying the input list
        copynums = nums1.copy()
        
        # Calculate the total length of the combined arrays
        length = len(nums1) + len(nums2)

        # Handle the case where nums1 is empty
        if not nums1:
            # If nums1 is empty, use nums2 as the combined array
            copynums = nums2.copy()
            nums2 = []
        
        # Merge nums2 into copynums using binary search
        while nums2 and len(copynums) < length:
            low = 0
            high = len(copynums) - 1
            
            # Remove the first element of nums2
            current = nums2.pop(0)
            
            # Case 1: If current is greater than or equal to the largest element in copynums
            if current >= copynums[high]:
                # Append current and the remaining elements of nums2 to copynums
                copynums += [current] + nums2
                continue
            
            # Case 2: If current is less than or equal to the smallest element in copynums
            elif current <= copynums[low]:
                # Prepend current to copynums
                copynums = [current] + copynums
                continue

            # Case 3: Use binary search to find the correct position for current
            while low <= high:
                mid = (low + high) // 2

                # If current fits between copynums[mid] and copynums[mid + 1]
                if copynums[mid] <= current <= copynums[mid + 1]:
                    # Insert current into the correct position
                    copynums.insert(mid + 1, current)
                    break
                # If current is greater than copynums[mid], search the right half
                elif current > copynums[mid]:
                    low = mid + 1
                # If current is less than copynums[mid], search the left half
                else:
                    high = mid - 1

        # Determine the median of the combined array
        if length % 2 == 1:
            # Odd length: return the middle element
            return copynums[length // 2]
        else:
            # Even length: return the average of the two middle elements
            return (copynums[length // 2] + copynums[length // 2 - 1]) / 2


            