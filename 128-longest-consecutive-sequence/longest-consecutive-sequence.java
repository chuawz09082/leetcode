class Solution {
    public int longestConsecutive(int[] nums) {
        HashSet<Integer> num_set = new HashSet<Integer>();

        for (int num: nums) num_set.add(num);

        int longest_streak = 0;

        for (int num: num_set){
            if (!num_set.contains(num-1)){
                int current_streak = 1;
                int start = num;
                while (num_set.contains(start+1)){
                    start ++;
                    current_streak ++;
                }

                longest_streak = Math.max(longest_streak, current_streak);

            }
        }



        return longest_streak;
    }
}