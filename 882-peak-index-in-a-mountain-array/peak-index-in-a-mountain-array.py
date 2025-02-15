class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left = 0  # Left boundary of the search space
        right = len(arr) - 1  # Right boundary of the search space

        while left < right:  # Continue binary search until left meets right
            mid = (left + right) // 2  # Find the middle index
            
            # Check if mid is the peak
            if arr[mid] > arr[mid + 1] and arr[mid] > arr[mid - 1]:  
                return mid  # Peak found, return index
            
            # If mid is increasing, move left boundary to mid+1
            elif arr[mid] > arr[mid - 1]:  
                left = mid + 1  
                
            # If mid is decreasing, move right boundary to mid
            else:  
                right = mid  

        return mid  # Return the peak index after the binary search loop
        