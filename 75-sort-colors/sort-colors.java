class Solution {
    public void sortColors(int[] nums) {
        int n = nums.length;
        int end = n-1;

        while (end >= 0 && nums[end] == 2) end --;

        for (int i = 0; i < n; i++){
            if (nums[i] == 2 && end >= 0){
                swap(nums, i, end);
                while (end >= 0 && nums[end] == 2) end --;
            }

            if (i == end) break;
        }

        int start = 0;
        while (start < n && nums[start] == 0) start ++;

        for (int i = n-1; i >= 0; i--){
            if (nums[i] == 0 && start < n){
                swap(nums, i, start);
                while (start < n && nums[start] == 0) start ++;
            }

            if (i == start) break;
        }
        
    }

    private void swap(int[] nums, int i, int j){
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}