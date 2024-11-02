class Solution:
    def avoidFlood(self, rains: List[int]) -> List[int]:
        fulllake = {}  # Keeps track of the last day each lake was filled
        dry_days = []  # Min-heap to prioritize dry days for lakes with upcoming rain
        result = [-1] * len(rains)  # Initialize result with -1 for rain days

        for day,lake in enumerate(rains):
            if lake > 0:
                if lake in fulllake:
                    last_rain_day = fulllake[lake]
                    if not dry_days:
                        return []
                    found_dry_day = False
                    for i in range(len(dry_days)):
                        if dry_days[i] > last_rain_day:
                            result[dry_days[i]] = lake
                            dry_days.pop(i)
                            found_dry_day = True
                            break
                    if not found_dry_day:
                        return []
                    
                fulllake[lake] = day
            else:
                dry_days.append(day)

        if dry_days:
            for day in dry_days:
                result[day] = 1
        
        return result
                    

        


        