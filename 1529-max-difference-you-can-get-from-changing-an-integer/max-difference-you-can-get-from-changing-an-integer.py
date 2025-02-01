class Solution:
    def maxDiff(self, num: int) -> int:
        start = 0
        stringnum = str(num)  # Convert the number to a string for easy digit manipulation
        n = len(stringnum) - 1  # Get the index of the last digit

        # Find the first digit that is not '9' to maximize the number by replacing it with '9'
        while start < len(stringnum) and stringnum[start] == '9':
            start += 1
        
        # If all digits are '9', the number remains unchanged. Otherwise, replace the first non-9 digit with '9'
        a_num = int(str(num).replace(str(num)[min(start, n)], '9'))
        
        # Reset start to find the optimal digit for minimizing the number
        start = 0
        
        # Case 1: If the first digit is not '1', replace it with '1' to minimize the number
        if stringnum[start] != '1':
            b_num = int(str(num).replace(str(num)[0], '1'))
        else:
            # Case 2: If the first digit is '1', find the first digit that is not '0' or '1'
            start += 1
            while start < len(stringnum) and (stringnum[start] == '0' or stringnum[start] == '1'):
                start += 1
            
            # If all remaining digits are '0' or '1', no further minimization is possible
            if start == n + 1:
                b_num = num
            else:
                # Replace the first non-0, non-1 digit with '0' to minimize the number
                b_num = int(str(num).replace(str(num)[start], '0'))

        # Return the difference between the maximized and minimized numbers
        return a_num - b_num
        