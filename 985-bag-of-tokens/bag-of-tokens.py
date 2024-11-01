class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        left = 0
        right = len(tokens) - 1
        score = 0
        max_score = 0

        while left <= right:
            # If we have enough power, play the smallest token face-up to gain score
            if power >= tokens[left]:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            # If we don't have enough power but have score, play the largest token face-down to gain power
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            # If neither move is possible, break out of the loop
            else:
                break

        return max_score

        