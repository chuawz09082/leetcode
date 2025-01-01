class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        """
        Calculates the maximum average pass ratio after distributing extra students
        among the given classes.

        @param classes: List of classes, where each class is represented as [passed, total].
        @param extraStudents: The number of additional students available for distribution.
        @return: The maximum average pass ratio achievable.
        """

        # Define a helper function to calculate the gain in pass ratio
        # when an extra student is added to the class.
        def calculate_gain(p: int, total: int) -> float:
            """
            Calculate the improvement in pass ratio when one student is added.

            @param p: The number of students who passed in the class.
            @param total: The total number of students in the class.
            @return: The gain in pass ratio (negative value for max-heap).
            """
            return -p / total + (p + 1) / (total + 1)  # Negative for max-heap simulation

        # Priority queue (max-heap using negative gain values) to store classes by potential gain.
        heap = []

        # Populate the heap with the initial pass ratios and their gains for each class.
        for p, total in classes:
            heappush(heap, (-calculate_gain(p, total), p, total))  # Push negative gain, passed, total

        # Distribute the extra students.
        while extraStudents:
            # Pop the class with the highest potential gain.
            _, p, total = heappop(heap)

            # Add one student to the class and recalculate the gain.
            heappush(heap, (-calculate_gain(p + 1, total + 1), p + 1, total + 1))

            # Decrement the count of extra students.
            extraStudents -= 1

        # Calculate the final average pass ratio.
        average = 0  # Variable to store the cumulative pass ratio
        while heap:
            # Pop each class and accumulate the pass ratio.
            _, p, total = heappop(heap)
            average += p / total

        # Return the average pass ratio across all classes.
        return average / len(classes)
