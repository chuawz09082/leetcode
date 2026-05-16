class Solution {
    private int[][] neighbours = {{1,0},{-1,0},{0,1},{0,-1}};

    public void wallsAndGates(int[][] rooms) {
        int rows = rooms.length;
        int cols = rooms[0].length;

        Queue<int[]> queue = new LinkedList<>();

        for (int row = 0; row < rows; row++){
            for (int col = 0; col < cols; col++){
                if (rooms[row][col] == 0) queue.offer(new int[]{row, col});
            }
        }

        
        int steps = 0;


        while (!queue.isEmpty()){
            int size = queue.size();

            for (int i = 0; i < size; i++){
                int[] current = queue.poll();
                rooms[current[0]][current[1]] = Math.min(rooms[current[0]][current[1]], steps);

                for (int[] n: neighbours){
                    int newrow = current[0] + n[0];
                    int newcol = current[1] + n[1];

                    if (newrow < 0 || newrow >= rows || newcol < 0 || newcol >= cols || rooms[newrow][newcol] != Integer.MAX_VALUE) continue;
                    queue.offer(new int[]{newrow, newcol});
                }
            }


            steps++;
        }
        
    }
}