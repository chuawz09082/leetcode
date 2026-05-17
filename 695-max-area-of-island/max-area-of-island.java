class Solution {
    private boolean[][] visited;
    private int rows;
    private int cols;
    private int[][] neighbours = {{1,0},{-1,0},{0,1},{0,-1}};

    public int maxAreaOfIsland(int[][] grid) {

        rows = grid.length;
        cols = grid[0].length;

        visited = new boolean[rows][cols];

        int maxArea= 0 ;

        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                if (grid[row][col] == 1 && !visited[row][col]){
                    maxArea = Math.max(maxArea, dfs(row, col, grid));
                }
            }
        }

        return maxArea;
        
    }


    private int dfs(int row, int col, int[][] grid){
        int area = 1;
        visited[row][col] = true;

        for (int[] n: neighbours){
            int newrow = row + n[0];
            int newcol = col + n[1];

            if (newrow < 0 || newrow >= rows || newcol < 0 || newcol >= cols || visited[newrow][newcol] || grid[newrow][newcol] == 0) continue;
            area += dfs(newrow, newcol, grid);
        }


        return area;
    }
}