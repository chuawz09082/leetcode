class Solution {

    public int orangesRotting(int[][] grid) {
        
        ArrayDeque<int[]> queue = new ArrayDeque<>();
        int rows = grid.length;
        int cols = grid[0].length;
        int[][] neighbours = {{0,1},{0,-1},{1,0},{-1,0}};
        int count = 0;
        

        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){

                if (grid[row][col] == 2){
                    int[] orange = new int[2];
                    orange[0] = row;
                    orange[1] = col;
                    queue.addLast(orange);
                } else if (grid[row][col] == 1) count += 1;
            }
        }

        if (count == 0) return 0;

        
        int time = -1;


        while (!queue.isEmpty()){
            int size = queue.size();
            

            for (int idx = 0 ;idx < size; idx ++){
                 int[] current = queue.pollFirst();

                 int r = current[0];
                 int c = current[1];

                 for (int[] n : neighbours){
                    int nr = r + n[0];
                    int nc = c + n[1];

                    if (nr < 0 || nr >= rows || nc < 0 || nc >= cols || grid[nr][nc] != 1 ) continue;

                    grid[nr][nc] = 2;
                    count -= 1;
                    queue.addLast(new int[]{nr,nc});
                 }
            }

            time += 1;
        }


        return (count == 0 ? time : -1);
    }
}