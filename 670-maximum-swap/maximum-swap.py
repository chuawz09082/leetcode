class Solution:
    def maximumSwap(self, num: int) -> int:
        lst = list(str(num))
        lstsort = sorted(lst,reverse = True)
        maxdgt = None

        for i in range(len(lst)):
            if lst[i] != lstsort[i]:
                maxdgt = int(lstsort[i])
                break

        if maxdgt == None:
            return num

        maxindex = []
        swap = None

        for i in range(len(lst)):
            if int(lst[i]) == maxdgt:
                maxindex.append(i)
            if swap == None and int(lst[i]) < maxdgt:
                swap = i

        maxswapidx = max(maxindex)
        print(maxswapidx,swap)

        newlst = lst[:swap]+lst[maxswapidx:maxswapidx+1]+lst[swap+1:maxswapidx]+lst[swap:swap+1]+lst[maxswapidx+1:]


        return int("".join(newlst))
        


        
        
        

        