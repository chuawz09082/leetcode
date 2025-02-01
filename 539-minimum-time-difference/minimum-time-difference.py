class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # Convert time "HH:MM" to total minutes since midnight
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))  # Split the string by ":" and convert to integers
            return hours * 60 + minutes  # Convert hours to minutes and add to minutes

# Convert all time points to minutes and sort them
        minutes_list = sorted([time_to_minutes(time) for time in timePoints])

        # Initialize the minimum difference to a very large number (infinity)
        diff = float('inf')

        # Iterate through the sorted list to find the smallest difference between consecutive time points
        for i in range(1, len(minutes_list)):
            # Calculate the difference between consecutive time points
            current_diff = minutes_list[i] - minutes_list[i - 1]
            
            # Update the minimum difference if the current difference is smaller
            diff = min(diff, current_diff)

        # Handle the wrap-around case (difference between the last and first time across midnight)
        wrap_around_diff = (minutes_list[0] + 24 * 60) - minutes_list[-1]

        # Update the minimum difference if the wrap-around difference is smaller
        diff = min(diff, wrap_around_diff)

        # Return the minimum difference
        return diff

