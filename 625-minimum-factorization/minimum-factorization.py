class Solution:
    def smallestFactorization(self, num: int) -> int:
        if num < 10:
            return num
        
        factors = []
        start = 9
        remain = num

        while remain > 1:
            if remain%2 != 0 and remain%3 != 0 and remain%5 != 0 and remain%7 != 0:
                return 0
            while remain%start == 0:
                factors.append(start)
                remain = remain//start
            start -= 1

        output = 0
        for n in factors[::-1]:
            output = output*10 + n
            if output > 2147483647:
                return 0

    
        return output


        