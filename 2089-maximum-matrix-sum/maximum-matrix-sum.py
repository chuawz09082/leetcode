class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        total_sum = 0  # To store the sum of absolute values of all elements
        min_abs_num = float('inf')  # To keep track of the smallest absolute value in the matrix
        negative_count = 0  # To count the number of negative elements in the matrix

        # Iterate through each row and element in the matrix
        for row in matrix:
            for num in row:
                total_sum += abs(num)  # Add the absolute value of the current number to the total sum
                
                # Count negative numbers (including zero since zero doesn't affect the sum)
                if num < 0:
                    negative_count += 1
                
                # Update the minimum absolute value found so far
                min_abs_num = min(min_abs_num, abs(num))
        
        # If the number of negative numbers is even, all elements can be made positive
        if negative_count % 2 == 0:
            return total_sum  # Return the total sum of absolute values
        
        else:
            # If the number of negative numbers is odd, one number must remain negative.
            # Subtract twice the smallest absolute value to account for this.
            return total_sum - 2 * min_abs_num








        