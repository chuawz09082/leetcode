from datetime import datetime

class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        # Convert the first date string into a datetime object
        date1 = datetime.strptime(date1, "%Y-%m-%d")
        
        # Convert the second date string into a datetime object
        date2 = datetime.strptime(date2, "%Y-%m-%d")
        
        # Calculate the difference between the two datetime objects
        # The result is a timedelta object
        difference = date2 - date1
        
        # Return the absolute value of the difference in days
        # This ensures a positive result regardless of the date order
        return abs(difference.days)