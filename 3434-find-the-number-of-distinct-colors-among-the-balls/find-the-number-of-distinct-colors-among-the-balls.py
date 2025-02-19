class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        # Dictionary to keep track of the color of each ball (ball index -> color)
        ballcolor = {}

        # Dictionary to keep track of the count of each color (color -> count)
        numcolor = collections.defaultdict(int)

        # List to store the results after each query
        result = []

        # Variable to count the number of distinct colors present at any time
        colors = 0

        # Process each query in the list
        for idx, color in queries:
            # If the ball at index 'idx' is not yet assigned a color
            if idx not in ballcolor:
                # Assign the new color to the ball
                ballcolor[idx] = color

                # Increase the count of this color
                numcolor[color] += 1

                # If this is the first ball of this color, increase the distinct color count
                if numcolor[color] == 1:
                    colors += 1

                # Store the number of distinct colors in the result list
                result.append(colors)

            else:
                # Get the original color of the ball before changing
                oricolor = ballcolor[idx]

                # Get the count of balls with the original color
                oricolornumber = numcolor[oricolor]

                # If there was only one ball of this color, removing it reduces distinct colors
                if oricolornumber == 1:
                    colors -= 1

                # Decrease the count of the original color since the ball is changing color
                numcolor[oricolor] -= 1

                # If the new color does not exist in the collection, increase the distinct color count
                if numcolor[color] == 0:
                    colors += 1               

                # Increase the count of the new color
                numcolor[color] += 1

                # Update the color of the ball
                ballcolor[idx] = color

                # Store the number of distinct colors in the result list
                result.append(colors)

        # Return the list containing the number of distinct colors after each query
        return result
