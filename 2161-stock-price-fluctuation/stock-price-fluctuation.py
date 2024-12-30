class StockPrice:

    def __init__(self):
        """
        Initialize the StockPrice class.
        - `self.stock` stores the price at each timestamp.
        - `self.current_timestamp` keeps track of the latest timestamp.
        - `self.min_heap` is a min-heap to efficiently find the minimum price.
        - `self.max_heap` is a max-heap to efficiently find the maximum price.
        """
        self.stock = {}
        self.current_timestamp = 0
        self.min_heap = []
        self.max_heap = []

    def update(self, timestamp: int, price: int) -> None:
        """
        Updates the price of the stock at the given timestamp.
        If the timestamp already exists, it overwrites the price.
        
        - Updates the `self.stock` dictionary with the given timestamp and price.
        - Updates the `self.current_timestamp` to the latest timestamp seen so far.
        - Pushes the new price and timestamp into both min-heap and max-heap.

        Time complexity: O(log n) for pushing into each heap.
        """
        # Update the price at the given timestamp
        self.stock[timestamp] = price
        
        # Update the latest timestamp
        self.current_timestamp = max(self.current_timestamp, timestamp)
        
        # Push the price and timestamp into the heaps
        heappush(self.min_heap, (price, timestamp))
        heappush(self.max_heap, (-price, timestamp))

    def current(self) -> int:
        """
        Returns the current price of the stock at the latest timestamp.

        Time complexity: O(1).
        """
        return self.stock[self.current_timestamp]

    def maximum(self) -> int:
        """
        Returns the maximum price of the stock.

        - Pops elements from the max-heap until the top of the heap represents a valid price (matches the price in `self.stock` for the corresponding timestamp).
        - Pushes the valid top element back into the heap after verification.

        Time complexity: O(log n) for heap operations.
        """
        # Get the top element of the max-heap
        maxprice, maxtime = heappop(self.max_heap)

        # Remove invalid entries (outdated prices)
        while -maxprice != self.stock[maxtime]:
            maxprice, maxtime = heappop(self.max_heap)
        
        # Push the valid entry back into the max-heap
        heappush(self.max_heap, (maxprice, maxtime))
        
        # Return the maximum price (convert back from negative)
        return -maxprice

    def minimum(self) -> int:
        """
        Returns the minimum price of the stock.

        - Pops elements from the min-heap until the top of the heap represents a valid price (matches the price in `self.stock` for the corresponding timestamp).
        - Pushes the valid top element back into the heap after verification.

        Time complexity: O(log n) for heap operations.
        """
        # Get the top element of the min-heap
        minprice, mintime = heappop(self.min_heap)

        # Remove invalid entries (outdated prices)
        while minprice != self.stock[mintime]:
            minprice, mintime = heappop(self.min_heap)
        
        # Push the valid entry back into the min-heap
        heappush(self.min_heap, (minprice, mintime))
        
        # Return the minimum price
        return minprice


# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()