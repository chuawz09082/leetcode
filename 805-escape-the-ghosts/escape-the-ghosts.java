class Solution {
    public boolean escapeGhosts(int[][] ghosts, int[] target) {
        int travelDist = Math.abs(target[0]) + Math.abs(target[1]);

        int ghostDist = Integer.MAX_VALUE;

        for (int[] ghost: ghosts){
            ghostDist = Math.min(ghostDist, Math.abs(ghost[0] - target[0]) + Math.abs(ghost[1] - target[1]));
        }



        return travelDist < ghostDist;
        
    }
}