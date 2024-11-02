class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fulllake = {}  # Keeps track of the last day each lake was filled
        dry_days = []  # Min-heap to prioritize dry days for lakes with upcoming rain
        result = [-1] * len(rains)  # Initialize result with -1 for rain days
        
        for day, lake in enumerate(rains):
            if lake > 0:  # It's a rain day for a specific lake
                if lake in fulllake:
                    # If lake is already full and will rain again, we must dry it first
                    last_rain_day = fulllake[lake]
                    if not dry_days:
                        return []  # No dry day available to prevent flood
                    
                    # Find the earliest dry day that is after the last rain for this lake
                    found_dry_day = False
                    for i in range(len(dry_days)):
                        dry_day = dry_days[i]
                        if dry_day > last_rain_day:
                            result[dry_day] = lake  # Use the dry day to dry this lake
                            dry_days.pop(i)  # Remove used dry day from heap
                            found_dry_day = True
                            break
                    
                    if not found_dry_day:
                        return []  # No dry day available to prevent flood
                    
                # Update last rain day for this lake
                fulllake[lake] = day
            
            else:  # It's a dry day
                heapq.heappush(dry_days, day)
        
        # Set remaining dry days to any arbitrary value (doesn't matter for the result)
        for dry_day in dry_days:
            result[dry_day] = 1  # Use '1' as arbitrary lake since it has no effect
        
        return result
                    

        


        