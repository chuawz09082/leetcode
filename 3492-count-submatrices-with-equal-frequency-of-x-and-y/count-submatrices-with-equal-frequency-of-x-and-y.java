class Solution {
    public int numberOfSubmatrices(char[][] grid) {
        int rows = grid.length;
        int cols = grid[0].length;
        Map<Character, Integer> map = Map.of('X', 1, 'Y', -1, '.', 0);

        int[][] dp = new int[rows][cols];

        boolean[][] seenX = new boolean[rows][cols];

        int count = 0;

        for (int row = 0; row < rows; row++){
            char c = grid[row][0];
            if (row == 0){
                dp[row][0] = map.get(c);
                if (c == 'X')seenX[row][0] = true;
            } else {
                dp[row][0] = dp[row-1][0] +map.get(c);
                if (seenX[row-1][0] == true || c == 'X')seenX[row][0] = true;
            }

            if (seenX[row][0] == true && dp[row][0] == 0) count += 1;
        }

        for (int col = 1; col < cols; col++){
            char c = grid[0][col];
            
            dp[0][col] = dp[0][col-1] +map.get(c);
            if (seenX[0][col-1] == true || c == 'X')seenX[0][col] = true;
            

            if (seenX[0][col] == true && dp[0][col] == 0) count += 1;
        }

        for (int row = 1; row < rows; row++){
            for (int col = 1; col < cols; col++){
                char c = grid[row][col];
                dp[row][col] = dp[row-1][col] + dp[row][col-1] - dp[row-1][col-1] + map.get(c);
                if (seenX[row][col-1] == true || seenX[row-1][col] == true  || c == 'X')seenX[row][col] = true;

                if (seenX[row][col] == true && dp[row][col] == 0) count += 1;
            }
        }



        return count;
    }
}