class Solution {
    public long findScore(int[] nums) {
        int n = nums.length;
        long score = 0L;
        boolean[] seen = new boolean[n];

        TreeMap<Integer, List<Integer>> treemap = new TreeMap<>();

        for (int idx = 0; idx < n; idx++){
            treemap.computeIfAbsent(nums[idx], k -> new ArrayList<>()).add(idx);
        }


        for (int key: treemap.keySet()){
            for (int idx: treemap.get(key)){
                if (seen[idx] == false){
                    score += (long) key;
                    seen[idx] = true;
                    if (idx > 0 && seen[idx-1] == false) seen[idx-1] = true;
                    if (idx < n-1  && seen[idx+1] == false) seen[idx+1] = true;
                }
            }
        }
        
       
        return score;
        
    }
}