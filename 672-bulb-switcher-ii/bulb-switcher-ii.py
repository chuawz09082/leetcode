class Solution:
    def flipLights(self, n: int, presses: int) -> int:
        # Define four combinations representing different button presses
        # comb1: toggles all lights
        # comb2: toggles even-indexed lights
        # comb3: toggles odd-indexed lights
        # comb4: toggles every third light
        comb1 = list(range(n))
        comb2 = list(range(0, n, 2))
        comb3 = list(range(1, n, 2))
        comb4 = list(range(0, n, 3))
        
        # Combine all combinations into a list for easy iteration
        comb = [comb1, comb2, comb3, comb4]

        # Initialize BFS queue with the initial state: all lights toggled (comb1)
        # and press count set to 0
        queue = deque([(comb1, 0)])
        
        # Set to store unique light configurations after specified presses
        result = set()
        
        # Set to track seen configurations with their respective press count
        seen = set()

        # BFS to explore all possible configurations within the press limit
        while queue:
            current, press = queue.popleft()

            # If the maximum number of presses is reached, add configuration to result
            if press == presses:
                result.add(tuple(sorted(current)))  # Sort to ensure unique configurations
                continue

            # Try all four possible button presses
            for i in range(4):
                # Toggle lights in `current` configuration using XOR with comb[i]
                new = tuple(set(current) ^ set(comb[i]))
                
                # Check if this new configuration and press count have been seen before
                if (new, press + 1) not in seen:
                    # Mark this configuration as seen
                    seen.add((tuple(sorted(new)), press + 1))
                    
                    # Append new configuration with incremented press count to the queue
                    queue.append((new, press + 1))
        
        # Return the number of unique configurations found
        return len(result)







    