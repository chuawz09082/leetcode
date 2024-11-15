class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # Initialize a list to track whether a course has prerequisites.
        # False means the course has no prerequisites and can be taken immediately.
        prereq = [False for _ in range(numCourses)]
        
        # Create dictionaries to track course dependencies:
        # - `nxtcourse`: Maps each course to the list of courses dependent on it.
        # - `prevcourse`: Maps each course to the list of its prerequisite courses.
        nxtcourse = collections.defaultdict(list)
        prevcourse = collections.defaultdict(list)

        # Populate `prereq`, `nxtcourse`, and `prevcourse` based on the prerequisites.
        for nxt, prev in prerequisites:
            # Mark that the course `nxt` has prerequisites.
            prereq[nxt] = True
            # Add `nxt` to the list of dependent courses for `prev`.
            nxtcourse[prev].append(nxt)
            # Add `prev` to the list of prerequisites for `nxt`.
            prevcourse[nxt].append(prev)
        
        # Identify courses that have no prerequisites (independent courses).
        # These can be taken initially.
        currentcourses = [idx for idx, ele in enumerate(prereq) if not ele]
        
        # List to store the course order in the correct sequence.
        sequence = []
        seen = set()

        while currentcourses and len(seen) < numCourses:
            nxtcourses = []  
            for course in currentcourses:              
                if course not in sequence and all(prereq_course in seen for prereq_course in prevcourse[course]):
                    sequence.append(course)
                    nxtcourses += nxtcourse[course]
                    seen.add(course)  
            
            currentcourses = nxtcourses
        
        return sequence if len(sequence) == numCourses else []
