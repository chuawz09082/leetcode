class Solution {
    int[][] neighbours = {{0,1},{0,-1},{1,0},{-1,0}};
    boolean[][] visited;

    public int[] findPeakGrid(int[][] mat) {
        int rows = mat.length;
        int cols = mat[0].length;
        visited = new boolean[rows][cols];

        return  dfs(0,0,rows,cols,mat);
        
    }

    private int[] dfs(int row, int col, int rows, int cols, int[][] mat){
        visited[row][col] = true;
        int[] ans = {row,col};

        for (int[] n: neighbours){
            int nrow = row+n[0];
            int ncol = col+n[1];

            if (nrow >= 0 && nrow < rows && ncol >= 0 && ncol < cols && visited[nrow][ncol] == false && mat[nrow][ncol] > mat[row][col]){
                ans = dfs(nrow,ncol,rows,cols,mat);
                return ans;
            }
        }


        return ans;
    }
}