class Solution {
    public int[][] minAbsDiff(int[][] grid, int k) {
        int rows = grid.length;
        int cols = grid[0].length;

        int[][] res = new int[rows - k+1][cols-k+1];

        for (int i = 0; i <= rows - k; i++){
            for (int j = 0; j <= cols-k;j++){
                List<Integer> kgrid = new ArrayList<>();

                for (int x = i; x < i+k; x++){
                    for (int y = j; y < j + k; y++) {
                        kgrid.add(grid[x][y]);
                    }
                }

                int kmin = Integer.MAX_VALUE;
                Collections.sort(kgrid);
                for (int t = 1; t < kgrid.size(); t++) {
                    if (kgrid.get(t).equals(kgrid.get(t - 1))) {
                        continue;
                    }
                    kmin = Math.min(kmin, kgrid.get(t) - kgrid.get(t - 1));
                }
                if (kmin != Integer.MAX_VALUE) {
                    res[i][j] = kmin;
                }
            }
        }

        return res;
    }
}