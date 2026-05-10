class Solution {
    public int maxFrequency(int[] nums, int k) {
        int[] count = new int[51];
        int res = 0;

        for (int num: nums){
            count[num] = Math.max(count[num], count[k]) + 1;
            res = Math.max(res, count[num] - count[k]);
        }

        return count[k] + res;
        
    }
}