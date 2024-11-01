class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if not trust:
            if n == 1:
                return n
            return -1

        trust_dict = collections.defaultdict(list)
        judge_dict  = collections.defaultdict(list)

        for i,j in trust:
            trust_dict[i].append(j)
            judge_dict[j].append(i)
        
        maxlenjudge = max([len(value) for value in judge_dict.values()])
        keyjudge = [key for key,value in judge_dict.items() if len(value) == maxlenjudge][0]

        if keyjudge in trust_dict.keys() or maxlenjudge < n-1:
            return -1
        return keyjudge
        