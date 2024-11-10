class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        neighbours = [(0,1),(0,-1),(1,0),(-1,0)]
        seen = set()
        rows = len(board)
        cols = len(board[0])

        def dfs(row: int, col: int) -> None:
            stack = [(row,col)]
            check = [(row,col)]
            island = True

            while check:
                row,col = check.pop()

                for n in neighbours:
                    if 0 <= row+n[0] < rows and 0 <= col+n[1] < cols:
                        if board[row+n[0]][col+n[1]] == "O" and (row+n[0],col+n[1]) not in seen:
                            seen.add(((row+n[0],col+n[1])))
                            stack.append((row+n[0],col+n[1]))
                            if 0 < row+n[0] < rows-1 and 0 < col+n[1] < cols-1:
                                check.append((row+n[0],col+n[1]))
                            else:
                                island = False
                        if (row+n[0],col+n[1]) in seen and ((row+n[0] == 0 or row+n[0] == rows-1) or (col+n[1] == 0 or col+n[1] == cols-1)):
                            island = False
            if island:
                for row,col in stack:
                    board[row][col] = "X"
    


        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O" and (i,j) not in seen:
                    seen.add((i,j))
                    if 0 < i < rows-1 and 0 < j < cols-1:
                        dfs(i,j)

        
