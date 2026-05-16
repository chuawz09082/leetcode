class Solution {
    public int numSubarraysWithSum(int[] nums, int goal) {
        int totalCount = 0;
        int currentSum = 0;

        HashMap<Integer, Integer> freq = new HashMap<>();
        freq.put(0,1);

        for (int num: nums){
            currentSum += num;

            if (freq.containsKey(currentSum - goal)){
                totalCount += freq.get(currentSum - goal);
            }

            freq.put(currentSum, freq.getOrDefault(currentSum, 0) + 1);


        }

        return totalCount;

        
        
    }
}