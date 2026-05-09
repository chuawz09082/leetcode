class Solution {
    public int countSquares(int[][] matrix) {
        int count = 0;
        int rows= matrix.length;
        int cols = matrix[0].length;

        ArrayDeque<int[]> queue = new ArrayDeque<>();

        for (int r = 0; r < rows; r++){
            for (int c = 0; c < cols; c++){
                int ele = matrix[r][c];
                if (ele == 1){
                    count += 1;
                    if (r > 0 && c > 0){
                        queue.addLast(new int[]{r,c});
                    }
                }
            }
        }

        int len = 1;

        while (!queue.isEmpty()){
            int size = queue.size();

            for (int i = 0; i < size; i++){
                int[] current = queue.pollFirst();
                int r = current[0];
                int c = current[1];

                boolean add = true;

                for (int row = r; row >= r-len; row--){
                    if (matrix[row][c-len] == 0){
                        add = false;
                        break;
                    }
                }

                if (add == false) continue;

                for (int col = c; col >= c-len; col--){
                    if (matrix[r-len][col] == 0){
                        add = false;
                        break;
                    }
                }

                
                

                if (add == true){
                    count += 1;
                    if (r > len && c > len) queue.addLast(current);
                    
                }

            }


            len += 1;
        }


        return count;
        
    }
}