class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        seenislands = set()
        seenpoints = set()
        idxes = deque()

        rows = len(grid)
        cols = len(grid[0])
        neighbour = [(0,1),(1,0),(-1,0),(0,-1)]

        def findmin(elements):   
            min_element = min(elements, key=lambda x: (x[0], x[1]))   
            return min_element
        
        def findneighbours(x,y):
            island = set()
            island.add((x,y))
            queue = deque([(x,y)])

            while queue:
                x0,y0 = queue.popleft()
                for dx,dy in neighbour:
                    if (x0+dx,y0+dy) in seenpoints:
                        continue
                    if 0 <= x0+dx < rows and 0 <= y0+dy < cols:
                        seenpoints.add((x0+dx,y0+dy))
                        if grid[x0+dx][y0+dy] == 1:
                            island.add((x0+dx,y0+dy))
                            queue.append((x0+dx,y0+dy))

            return list(island)

        def subtract_tuple_from_list(lst, subtrahend):
            return [(x - subtrahend[0], y - subtrahend[1]) for x, y in lst]

        for r in range(rows):
            for c in range(cols):
                idxes.append((r,c))

        while idxes:
            i,j = idxes.popleft()
            if (i,j) in seenpoints:
                continue
            seenpoints.add((i,j))
            if grid[i][j] == 1:
                listisland = findneighbours(i,j)
                mintuple = findmin(listisland)
                
                listisland  = subtract_tuple_from_list(listisland, mintuple)
                seenislands.add(frozenset(listisland))

        return len(seenislands)







