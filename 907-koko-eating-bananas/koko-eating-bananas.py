class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def can_eat_bananas(speed):
            total_hours = 0
            for p in piles:
                total_hours += ceil(p/speed)
            
            if total_hours > h:
                return False
            return True

        piles.sort()
        left = 1
        right = piles[-1]

        while left < right:
            mid = (left+right)//2
            total_hours = 0
            for p in piles:
                total_hours += ceil(p/mid)

            if total_hours <= h:
                right = mid
            else:
                left = mid+1
        
        start = mid
        
        while not can_eat_bananas(start):
            start += 1
        return start



        
        


        
            

        