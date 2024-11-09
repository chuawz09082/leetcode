import bisect

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        if len(arr)%2 == 1:
            return False

        arr.sort()
        index = bisect.bisect_left(arr, 0)
        
        ngvarr = sorted(arr[:index],reverse = True)
        posarr = arr[index:]

        ngvresult = [None]*len(arr)
        posresult = [None]*len(arr)

        startpos = 0
        while posarr:
            minvalue = posarr.pop(0)
            posresult[startpos] = minvalue
            if 2*minvalue in posarr:
                nxtidx = posarr.index(2*minvalue)
                posresult[startpos+1] = posarr.pop(nxtidx)
            else:
                return False
            startpos += 2
            posarr.sort()

        startpos = 0
        while ngvarr:
            maxvalue = ngvarr.pop(0)
            ngvresult[startpos] = maxvalue

            if 2*maxvalue in ngvarr:
                nxtidx = ngvarr.index(2*maxvalue)
                ngvresult[startpos+1] = ngvarr.pop(nxtidx)
            else:
                return False
            startpos += 2
            ngvarr.sort(reverse = True)

        if posresult.count(None)+ngvresult.count(None) == len(arr):
            return True
        return False





        