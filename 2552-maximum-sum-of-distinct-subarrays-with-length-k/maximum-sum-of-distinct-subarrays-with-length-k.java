class Solution {
    public long maximumSubarraySum(int[] nums, int k) {
        int n = nums.length;
        long maxTotal = Long.MIN_VALUE;
        long currentTotal = 0;
        HashMap<Integer, Integer> hashmap = new HashMap<>();

        for (int i = 0; i <= n - k;i ++){
            
            if (i == 0){
                for (int j = 0; j < k; j++){
                    hashmap.put(nums[j], hashmap.getOrDefault(nums[j],0)+1);
                    currentTotal += (long) nums[j];
                }
            } else {
                hashmap.put(nums[i+k-1], hashmap.getOrDefault(nums[i+k-1],0)+1);

                if (hashmap.get(nums[i-1]) > 1) hashmap.put(nums[i-1], hashmap.get(nums[i-1])-1);
                else hashmap.remove(nums[i-1]);
                currentTotal += (long) nums[i+k-1];
                currentTotal -= (long) nums[i-1];
          
            }

            if (hashmap.size() == k){
                maxTotal = Math.max(maxTotal, currentTotal);
            }

           

        }
        
        return maxTotal != Long.MIN_VALUE ? maxTotal : 0;
    }
}