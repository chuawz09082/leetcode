class Solution {
    boolean[][] visited;
    int rows;
    int cols;
    int[][] neighbours = {{1,0},{-1,0},{0,1},{0,-1}};
    
    public boolean exist(char[][] board, String word) {
        rows = board.length;
        cols = board[0].length;

        visited = new boolean[rows][cols];

        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                char c = board[row][col];
                if (c == word.charAt(0) && dfs(row, col, board, 1 ,word)) return true;
            }
        }

        return false;
        
    }

    private boolean dfs(int row, int col, char[][] board, int idx, String word){
        visited[row][col] = true;

        if (idx == word.length()) return true;

        char c = word.charAt(idx);

        for (int[] n: neighbours){
            int newrow = row + n[0];
            int newcol = col + n[1];
            if (newrow < 0 || newrow >= rows || newcol < 0 || newcol >= cols ||
            visited[newrow][newcol] || board[newrow][newcol] != c) continue;

            if (dfs(newrow, newcol, board, idx+1, word)) return true;
        }

        visited[row][col] = false;

        

        return false;
    }
}