class Solution {
    public int[] getBiggestThree(int[][] grid) {
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int rows = grid.length;
        int cols = grid[0].length;

        for (int row = 0; row < rows; row++) {
            for (int col = 0; col < cols; col++) {
                int maxSide = Math.min(cols-1-col, col);
                maxSide = Math.min(maxSide, (rows-1-row)/2);

                offer(pq, grid[row][col]);

                for (int side = 1; side <= maxSide; side++) {
                    offer(pq, getRhombusSum(side, row, col, grid));
                }
            }
        }

        List<Integer> res = new ArrayList<>(pq);
        Collections.sort(res, Collections.reverseOrder());
        return res.stream().mapToInt(Integer::intValue).toArray();
    }

    private void offer(PriorityQueue<Integer> pq, int sum) {
        if (contains(pq, sum)) return;
        if (pq.size() < 3) pq.offer(sum);
        else if (pq.peek() < sum) {
            pq.poll();
            pq.offer(sum);
        }
    }

    private boolean contains(PriorityQueue<Integer> pq, int sum) {
        for (int val : pq) {
            if (val == sum) return true;
        }
        return false;
    }

    private int getRhombusSum(int side, int row, int col, int[][] grid) {
        int sum = grid[row][col];
        int count = 0;

        while (count < side) {
            sum += grid[row+count+1][col+count+1];
            sum += grid[row+count+1][col-count-1];
            count++;
        }

        count = 0;
        while (count < side-1) {
            sum += grid[row+side+count+1][col+side-count-1];
            sum += grid[row+side+count+1][col-side+count+1];
            count++;
        }

        sum += grid[row+2*side][col];
        return sum;
    }
}