class Solution:
    def assignBikes(self, workers: List[List[int]], bikes: List[List[int]]) -> List[int]:
        distdict = collections.defaultdict(list)
        result = [None]*len(workers)


        for i in range(len(workers)):
            for j in range(len(bikes)):
                manh = abs(bikes[j][0] - workers[i][0]) + abs(bikes[j][1] - workers[i][1])
                distdict[manh].append((i,j))

        distdict = dict(sorted(distdict.items(), key=lambda item: (item[0], sorted(item[1]))))

        for key in distdict.keys():
            values = distdict[key]
            for worker,bike in values:
                if result[worker] == None and bike not in result:
                    result[worker] = bike
        
        return result



        