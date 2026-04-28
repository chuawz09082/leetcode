class Solution {
    int[][] neighbours = {{0,1},{1,0},{0,-1},{-1,0}};
    int rows, cols;

    public boolean containsCycle(char[][] grid) {
        rows = grid.length;
        cols = grid[0].length;

        boolean[][] visited = new boolean[rows][cols];

        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                if (!visited[r][c]){
                    if (dfs(grid, visited, r, c, -1, -1)){
                        return true;
                    }
                }
            }
        }
        return false;
    }

    private boolean dfs(char[][] grid, boolean[][] visited,
                        int r, int c, int pr, int pc){

        visited[r][c] = true;

        for (int[] n : neighbours){
            int nr = r + n[0];
            int nc = c + n[1];

            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            if (grid[nr][nc] != grid[r][c]) continue;

            // skip parent
            if (nr == pr && nc == pc) continue;

            // cycle found
            if (visited[nr][nc]) return true;

            if (dfs(grid, visited, nr, nc, r, c)) return true;
        }

        return false;
    }
}