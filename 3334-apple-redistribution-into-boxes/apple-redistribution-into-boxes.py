class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        total_apples = sum(apple)
        countbox = 0
        start = 0
        while total_apples > 0:
            while capacity[start] > 0:
                total_apples -= 1
                capacity[start] -= 1
                if total_apples == 0:
                    return start + 1
            start += 1
        
        return start
            