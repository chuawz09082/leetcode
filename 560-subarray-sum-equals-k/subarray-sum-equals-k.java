class Solution {
    public int subarraySum(int[] nums, int k) {
        int count = 0;
        int prefixSum = 0;
        int n = nums.length;
        HashMap<Integer, Integer> hashmap = new HashMap<>();
        hashmap.put(0,1);

        for (int idx = 0; idx < n; idx++){
            prefixSum += nums[idx];

            if (hashmap.containsKey(prefixSum - k)){
                count += hashmap.get(prefixSum - k);
            }

            hashmap.put(prefixSum, hashmap.getOrDefault(prefixSum, 0)+1);
            
           
        }


        return count;
        
    }
}