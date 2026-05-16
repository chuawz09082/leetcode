class Solution {
    private int[][] neighbours = {{1,0},{-1,0},{0,1},{0,-1}};
    private int rows;
    private int cols;


    public void solve(char[][] board) {
        rows = board.length;
        cols = board[0].length;

        for (int i = 0; i < rows; i++){
            if (board[i][0] == 'O') dfs(i,0,board);
            if (board[i][cols-1] == 'O') dfs(i,cols-1,board);
        }

        for (int i = 0; i < cols; i++){
            if (board[0][i] == 'O') dfs(0,i,board);
            if (board[rows-1][i] == 'O') dfs(rows-1,i,board);
        }

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                if (board[i][j] == 'O') board[i][j] = 'X';
                if (board[i][j] == 'T') board[i][j] = 'O';
            }
        }
        
    }

    private void dfs(int row, int col, char[][] board){
        board[row][col] = 'T';

        for (int[] n: neighbours){
            int newrow = row+ n[0];
            int newcol = col + n[1];

            if (newrow < 0 || newrow >= rows || newcol < 0 || newcol >= cols ||
            board[newrow][newcol] != 'O') continue;

            dfs(newrow,newcol,board);
        }
            
      
    }
}