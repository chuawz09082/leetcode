class Solution {
    public int unhappyFriends(int n, int[][] preferences, int[][] pairs) {
        int[] map = new int[n];

        for (int[] pair: pairs){
            map[pair[0]] = pair[1];
            map[pair[1]] = pair[0];
        }

        int res = 0;

        Map<Integer, Integer>[] prefer = new Map[n];

        for (int i = 0; i < n; i++){
            for (int j = 0; j < n-1; j++){
                if (prefer[i] == null) prefer[i] = new HashMap<>();
                prefer[i].put(preferences[i][j], j);
            }
        }

        for (int i = 0; i < n; i++){
            for (int j : preferences[i]){
                if (prefer[j].get(i) < prefer[j].get(map[j])
                && prefer[i].get(j) < prefer[i].get(map[i])){
                    res ++;
                    break;
                }
            }
        }



        return res;
        
    }
}