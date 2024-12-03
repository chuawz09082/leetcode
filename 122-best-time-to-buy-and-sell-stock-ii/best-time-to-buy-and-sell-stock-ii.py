class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be achieved from an unlimited number 
        of stock trades. You can buy and sell stocks on multiple days.

        Args:
        prices (List[int]): A list where prices[i] is the price of a given stock on day i.

        Returns:
        int: The maximum profit you can achieve by buying and selling stocks.
        """
        # Initialize total profit to 0
        profit = 0
        
        # Iterate through the prices starting from the second day
        for i in range(1, len(prices)):
            # If the current day's price is greater than the previous day's price
            # there is a profit opportunity, so add the difference to the total profit
            if prices[i] - prices[i-1] > 0:
                profit += prices[i] - prices[i-1]
        
        # Return the total accumulated profit
        return profit
        
        