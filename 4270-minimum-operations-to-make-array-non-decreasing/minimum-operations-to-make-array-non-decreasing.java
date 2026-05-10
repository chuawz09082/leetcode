class Solution {
    public long minOperations(int[] nums) {
        
        long count = 0L;
        for (int i = 0; i+1 < nums.length; i++){
            count += Math.max(0, nums[i] - nums[i+1]);
        }
        



        return count;
        
    }
}