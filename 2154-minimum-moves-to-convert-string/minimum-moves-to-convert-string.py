class Solution:
    def minimumMoves(self, s: str) -> int:
        start = 0
        moves = 0
        s_list = list(s)

        while start < len(s_list)-2:
            while start < len(s_list)-2 and s_list[start] != "X":
                start += 1
                print(start,s_list[start])
                
            if "X" in s_list[start:start+3]:
                moves += 1
                for i in range(3):
                    if start+i < len(s_list):
                        s_list[start+i] = "0"
            if start >= len(s)-3:
                return moves
            start += min(3,len(s)-3-start)

            



        