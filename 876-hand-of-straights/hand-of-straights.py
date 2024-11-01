class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        # If hand size is not a multiple of groupSize, it's impossible to form groups
        if len(hand) % groupSize != 0:
            return False
        
        # Count the frequency of each card in the hand
        count = Counter(hand)
        
        # Sort the keys (unique cards) in ascending order
        unique_cards = sorted(count)
        
        # Try to form groups starting from each unique card
        for card in unique_cards:
            # If there are still some of this card left to place in groups
            if count[card] > 0:
                # Attempt to form a group starting from this card
                num_needed = count[card]  # How many groups we need starting from this card
                for i in range(groupSize):
                    # Check if the next consecutive card has enough to form the group
                    if count[card + i] < num_needed:
                        return False  # Not enough cards to complete this group
                    # Deduct the cards used to form the group
                    count[card + i] -= num_needed
        
        return True



        