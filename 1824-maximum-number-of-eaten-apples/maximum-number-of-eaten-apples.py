
class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        priority_queue = []  # Min-heap to track (expiration, apples)
        apples_eaten = 0  # Total apples eaten
        day = 0  # Current day

        while day < len(apples) or priority_queue:
            # Add new apples that become available on the current day
            if day < len(apples) and apples[day] > 0:
                expiration = day + days[day]
                heapq.heappush(priority_queue, (expiration, apples[day]))
            
            # Remove expired apples or apples with zero quantity
            while priority_queue and (priority_queue[0][0] <= day or priority_queue[0][1] == 0):
                heapq.heappop(priority_queue)
            
            # Eat an apple if available
            if priority_queue:
                expiration, apple_count = heapq.heappop(priority_queue)
                apples_eaten += 1  # Eat one apple
                if apple_count > 1:
                    # Put back the remaining apples with updated count
                    heapq.heappush(priority_queue, (expiration, apple_count - 1))
            
            day += 1  # Move to the next day

        return apples_eaten
            
            
        

