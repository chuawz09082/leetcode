class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        # Dictionary to store scores for each student
        # The key is the student's ID, and the value is a list of their top scores
        store_scores = collections.defaultdict(list)
        
        # Sort the items by student ID (ascending), then by score (descending)
        items_sort = sorted(items, key=lambda x: (x[0], -x[1]))
        
        # Iterate through the sorted list to collect the top 5 scores for each student
        while items_sort:
            current = items_sort.pop(0)  # Remove and return the first element from the list
            idx = current[0]  # Extract the student ID
            result = current[1]  # Extract the score
            
            # Append the score to the student's list if they have fewer than 5 scores
            if len(store_scores[idx]) < 5:
                store_scores[idx].append(result)
        
        # Prepare the final answer
        answer = []
        for key, value in store_scores.items():
            # Append each student's ID and the average of their top 5 scores
            answer.append([key, sum(value) // 5])
        
        return answer