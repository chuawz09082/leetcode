class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Find the k closest points to the origin (0, 0) using the Euclidean distance.
        
        Args:
        points (List[List[int]]): List of points on a 2D plane, where each point is represented as [x, y].
        k (int): Number of closest points to find.
        
        Returns:
        List[List[int]]: The k points closest to the origin.
        """
        
        def euclidean(point1: List[int], point2: List[int]) -> float:
            """
            Calculate the Euclidean distance between two points.
            
            Args:
            point1 (List[int]): Coordinates of the first point [x1, y1].
            point2 (List[int]): Coordinates of the second point [x2, y2].
            
            Returns:
            float: The Euclidean distance between the two points.
            """
            # Apply the formula for Euclidean distance: sqrt((x2 - x1)^2 + (y2 - y1)^2)
            return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)

        # Sort the points based on their Euclidean distance from the origin (0, 0)
        points = sorted(points, key=lambda x: euclidean(x, [0, 0]))

        # Return the first k points, which are the closest to the origin
        return points[:k]
        