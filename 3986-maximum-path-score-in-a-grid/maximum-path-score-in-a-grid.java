class Solution {
    public int maxPathScore(int[][] grid, int k) {
        
        int rows = grid.length;
        int cols = grid[0].length;
        int[][][] dp = new int[rows][cols][k+1];

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                Arrays.fill(dp[i][j], Integer.MIN_VALUE);
            }
        }

        dp[0][0][0] = 0;

        for (int i = 0; i < rows; i++){
            for (int j = 0; j < cols; j++){
                for (int c = 0; c <= k; c++){
                    if (dp[i][j][c] == Integer.MIN_VALUE) continue;

                    if (i+1 < rows){
                        int val = grid[i+1][j];
                        int cost = (val == 0 ? 0 : 1);
                        if (c + cost <= k){
                            dp[i+1][j][c + cost] = Math.max(dp[i+1][j][c + cost], dp[i][j][c] + val);
                        }
                    }

                    if (j+1 < cols){
                        int val = grid[i][j+1];
                        int cost = (val == 0 ? 0 : 1);
                        if (c + cost <= k){
                            dp[i][j+1][c + cost] = Math.max(dp[i][j+1][c + cost], dp[i][j][c] + val);
                        }
                    }
                }
            }
        }

        int ans = Integer.MIN_VALUE;

        for (int c = 0; c <= k; c++){
            ans = Math.max(ans, dp[rows-1][cols-1][c]);
        }

        return ans < 0 ? -1 : ans;

        
    }

    
}