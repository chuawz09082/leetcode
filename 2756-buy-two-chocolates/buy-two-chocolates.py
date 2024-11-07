class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        prices.sort()
        count = 0
        left = money
        for price in prices:
            if count == 2:
                return left
            if price > left:
                return money
            left -= price
            count += 1
        
        return left
        