
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        priority_queue = []  # Min-heap to track (expiration, apples)
        apples_eaten = 0  # Total apples eaten
        day = 0  # Current day

        while day < len(apples) or priority_queue:
            if day < len(apples) and apples[day] > 0:
                expiration = day + days[day]
                heapq.heappush(priority_queue,(expiration, apples[day]))
            
            while priority_queue and (priority_queue[0][0] <= day or priority_queue[0][1] == 0):
                heapq.heappop(priority_queue)
            
            if priority_queue:
                expiration, apple_count = heapq.heappop(priority_queue)
                apples_eaten += 1
                apple_count -= 1
                if apple_count > 0:
                    heapq.heappush(priority_queue, (expiration, apple_count))

            day += 1
        return apples_eaten 
            
        

