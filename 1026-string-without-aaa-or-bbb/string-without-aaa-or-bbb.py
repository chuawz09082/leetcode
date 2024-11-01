class Solution:
    def strWithout3a3b(self, a: int, b: int) -> str:
        if a + b <= 3:
            s = ""
            s += "a"*a
            s += "b"*b
            return s

        lists = ["" for _ in range(a+b)]

        s = ""

        if b > a:
            chars = "b"
            charn = "a"
        else:
            chars = "a"
            charn = "b"

        totals = max(a,b)
        totaln = min(a,b)
        remains = totals
        remainn = totaln


        while remains > remainn and remainn > 0 and remains > 0:
            mins = min(2,remains)
            s += chars*mins
            remains -= mins

            minn = min(1,remainn)
            s += charn*minn
            remainn -= minn

        print(s)
        if remains > 0 or remainn > 0:
            if remainn == 0:
                s += chars*remains
                return s
            for i in range(a+b - len(s)):
                if len(s) > 0 and s[-1] == "b":
                    s += "a"
                else:
                    s += "b"

        
        return s



