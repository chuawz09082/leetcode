class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        moneydict = collections.defaultdict(int)
        
        for val in bills:
            if val == 5:
                moneydict[5] += 1
            elif val == 10:
                if moneydict[5] == 0:
                    return False
                moneydict[5] -= 1
                moneydict[10] += 1
            else:
                if moneydict[10] >= 1 and moneydict[5] >= 1:
                    moneydict[5] -= 1
                    moneydict[10] -= 1
                    moneydict[20] += 1
                elif moneydict[5] >= 3:
                    moneydict[5] -= 3
                    moneydict[20] += 1
                else:
                    return False
        
        return True

        