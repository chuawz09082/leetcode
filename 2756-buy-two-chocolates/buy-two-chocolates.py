class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        # Sort the prices list to start buying the cheapest chocolates first
        prices.sort()
        
        # Initialize count to keep track of how many chocolates have been bought
        count = 0
        # Initialize left with the total money available
        left = money

        # Iterate through the sorted prices list
        for price in prices:
            # If we have already bought 2 chocolates, return the remaining money
            if count == 2:
                return left
            # If the current price is more than the money left, return the original money
            # since we cannot buy more chocolates
            if price > left:
                return money
            
            # Deduct the price of the current chocolate from the remaining money
            left -= price
            # Increment the count as we have bought one chocolate
            count += 1
        
        # Return the remaining money after buying up to 2 chocolates
        return left
        