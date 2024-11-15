class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize a list to track whether each course has prerequisites.
        # False indicates the course has no prerequisites.
        prereq = [False for _ in range(numCourses)]
        
        # Create dictionaries to manage dependencies:
        # - `nxtcourse`: Maps a course to the list of courses dependent on it.
        # - `prevcourse`: Maps a course to the list of courses it depends on.
        nxtcourse = collections.defaultdict(list)
        prevcourse = collections.defaultdict(list)

        # Populate `prereq`, `nxtcourse`, and `prevcourse` based on the prerequisites list.
        for nxt, prev in prerequisites:
            # Mark that `nxt` has prerequisites.
            prereq[nxt] = True
            # Add `nxt` to the list of dependent courses for `prev`.
            nxtcourse[prev].append(nxt)
            # Add `prev` to the list of prerequisites for `nxt`.
            prevcourse[nxt].append(prev)
        
        # Identify courses with no prerequisites; these can be taken initially.
        currentcourses = [idx for idx, ele in enumerate(prereq) if not ele]
        
        # List to store the order of courses.
        sequence = []
        # Set to keep track of courses that have already been processed.
        seen = set()

        # Process courses using a BFS-like approach.
        while currentcourses and len(seen) < numCourses:
            nxtcourses = []  # List to store courses for the next level of processing.
            for course in currentcourses:              
                # If the course is not already in the sequence and all its prerequisites have been processed:
                if course not in sequence and all(prereq_course in seen for prereq_course in prevcourse[course]):
                    # Add the course to the sequence.
                    sequence.append(course)
                    # Add its dependent courses to the next level.
                    nxtcourses += nxtcourse[course]
                    # Mark the course as seen.
                    seen.add(course)  
            
            # Move to the next level of processing.
            currentcourses = nxtcourses
        
        # If all courses are included in the sequence, return the sequence.
        # Otherwise, return an empty list to indicate a cycle in the prerequisites.
        return sequence if len(sequence) == numCourses else []
