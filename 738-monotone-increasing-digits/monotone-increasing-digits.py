class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        lst = list(str(n))
        
        while lst:
            if len(lst) == 1:
                return int("".join(lst))

            for i in range(len(lst)-1,0,-1):
                if int(lst[i]) < int(lst[i-1]):
                    pos = i
                    break
                if i == 1:
                    return int("".join(lst))

            zeros = ['0' for _ in range(len(lst)-pos)]
            lst = lst[:pos]+zeros
            lst = list(str(int("".join(lst))-1))

        return int("".join(lst))

