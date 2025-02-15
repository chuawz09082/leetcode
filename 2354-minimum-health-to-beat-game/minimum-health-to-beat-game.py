class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # Calculate the total damage if no armor is used
        totaldamage = sum(damage)

        # The armor can only absorb the largest single attack up to its maximum capacity.
        # If `armor` is greater than the highest damage attack, it only absorbs that highest attack.
        armor = min(armor, max(damage))

        # The minimum health required is:
        # - The total damage sustained
        # - Minus the absorbed damage from the strongest attack
        # - Plus 1 to ensure survival (i.e., health never reaches 0)
        return totaldamage - armor + 1
        