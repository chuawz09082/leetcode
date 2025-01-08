class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        """
        Calculates the maximum earnings a taxi driver can achieve by selecting non-overlapping rides optimally.

        @param n: int - The maximum endpoint of any ride (number of positions).
        @param rides: List[List[int]] - A list of rides where each ride is represented as [start, end, tip].
        @return: int - The maximum earnings achievable.
        """

        # Step 1: Sort rides by their ending position, and for rides with the same end position,
        # prioritize rides with larger effective profit (smaller start time and smaller tip).
        rides = sorted(rides, key=lambda x: (x[1], -x[1] + x[0] - x[2]))

        # Step 2: Initialize an array `earnings` to store the maximum earnings possible at each position.
        earnings = [0] * (n + 1)  # `earnings[i]` represents the max earnings possible up to position `i`.

        # Variable to track the last visited endpoint in `rides`.
        lastvisited = None

        # Step 3: Iterate over each ride.
        for starti, endi, tipi in rides:
            # Calculate the profit of the current ride (distance + tip).
            profiti = endi - starti + tipi

            # If this is the first ride processed:
            if not lastvisited:           
                # Set the earnings at the endpoint of this ride to its profit.
                earnings[endi] = profiti
                # Update the last visited endpoint.
                lastvisited = endi
            else:
                # Step 4: Find the closest valid position with maximum earnings before the current ride starts.
                basei = starti
                while basei > 0 and earnings[basei] == 0:
                    basei -= 1  # Move backward to find the last non-zero earnings.

                # Case 1: If the current ride does not overlap with the last processed ride:
                if starti >= lastvisited:                   
                    # Update earnings at the current ride's endpoint.
                    earnings[endi] = earnings[basei] + profiti
                    # Update the last visited endpoint.
                    lastvisited = endi
                else:
                    # Case 2: If the current ride overlaps:
                    # Check if taking this ride gives a better profit compared to the last visited ride.
                    if earnings[basei] + profiti > earnings[lastvisited]:                       
                        # Update earnings at the current ride's endpoint.
                        earnings[endi] = earnings[basei] + profiti
                        # Update the last visited endpoint.
                        lastvisited = endi
        # Return maximum of earnings
        return max(earnings)
            



        