class Solution {
    public int[] maxValue(int[] nums) {
        int n = nums.length;
        int[] ans = new int[n];
        ans[0] = nums[0];

        for (int right = 1; right < n; right++){
            ans[right] = Math.max(ans[right-1], nums[right]);
        }

        int minRight = nums[n-1];

        for (int idx = n-2; idx >= 0 ;idx--){

            if (minRight < ans[idx]){
                ans[idx] = Math.max(ans[idx], ans[idx+1]);
            }
            minRight = Math.min(minRight, nums[idx]);
        }

        return ans;

        
        
    }
}