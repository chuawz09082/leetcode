class Solution:
    def minimumTime(self, jobs: List[int], workers: List[int]) -> int:
        """
        Calculate the minimum number of days required to complete all jobs 
        given the available workers with different work speeds.

        :param jobs: List of integers representing the amount of work required for each job.
        :param workers: List of integers representing the work capacity of each worker per day.
        :return: The minimum number of days required to complete all jobs.
        """
        
        # Step 1: Sort both the jobs and workers lists in ascending order.
        # Sorting ensures that we assign the weakest workers to the easiest jobs
        # and the strongest workers to the hardest jobs, minimizing overall time.
        jobs.sort()
        workers.sort()

        # Step 2: Calculate the number of days required for each worker to complete their assigned job.
        # We pair jobs[i] with workers[i], and compute the days required using ceil(jobs[i] / workers[i]).
        # Ceiling is used to round up since a job cannot be completed in a fractional day.
        days = [ceil(jobs[i] / workers[i]) for i in range(len(jobs))]

        # Step 3: Return the maximum number of days required among all workers.
        # The longest duration determines when all jobs will be completed.
        return max(days)
        