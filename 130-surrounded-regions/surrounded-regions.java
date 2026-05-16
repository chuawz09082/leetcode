class Solution {
    private int[][] neighbours = {{1,0},{-1,0},{0,1},{0,-1}};
    private int rows;
    private int cols;
    private List<List<Integer>> regionsO;
    private boolean[][] visited;

    public void solve(char[][] board) {
        rows = board.length;
        cols = board[0].length;
        
        visited = new boolean[rows][cols];

        for (int row = 1; row < rows-1; row++){
            for (int col = 1; col < cols-1; col++){
                if (board[row][col] == 'O' && !visited[row][col]){
                    regionsO = new ArrayList<>();
                    boolean toFlip = isIsland(row,col,board);
                    if (toFlip){
                        for (List<Integer> list: regionsO){
                            board[list.get(0)][list.get(1)] = 'X';
                        }
                    }
                }

          
            }
        }

        
        
    }

    private boolean isIsland(int row, int col, char[][] board){
        if (row == 0 || row == rows - 1 ||
            col == 0 || col == cols - 1) {
            return false;
        }

        visited[row][col] = true;
        regionsO.add(List.of(row, col));
        boolean ans = true;

        for (int[] n: neighbours){
            int newrow = row + n[0];
            int newcol = col + n[1];

            if (newrow < 0 || newrow >= rows || newcol < 0 || newcol >= cols || board[newrow][newcol] == 'X') continue;

            if (visited[newrow][newcol] == false ){
                ans = isIsland(newrow, newcol, board) && ans;
            }

            
        }


        return ans;
    }
}