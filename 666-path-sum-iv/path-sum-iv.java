class Solution {
    // Static variables to hold the final sum of path values and the list of paths
    static int finalsum;
    static List<List<Integer>> listnums;

    public int pathSum(int[] nums) {
        // Sort the array to process nodes from leaf to root
        Arrays.sort(nums);
        
        // Determine the maximum depth of the tree from the largest element
        int maxdepth = nums[nums.length - 1] / 100;
        
        // Initialize list of paths and final sum accumulator
        listnums = new ArrayList<>();
        finalsum = 0;

        // Traverse nodes from the last (deepest level) to the first (root level)
        for (int i = nums.length - 1; i > -1; i--) {
            int hundredsi = nums[i] / 100;      // The depth level of the current node
            int tensi = (nums[i] / 10) % 10;    // Position in the current level
            int onesi = nums[i] % 10;           // Value of the current node

            // If the node is at max depth (leaf node), start a new path
            if (hundredsi == maxdepth) {
                List<Integer> newlist = new ArrayList<>();
                newlist.add(nums[i]);
                listnums.add(newlist);          // Add new path with the leaf node
                finalsum += onesi;              // Add node value to final sum
                continue;
            }

            // Count how many paths this node connects to at the next level
            int count = 0;
            for (int j = 0; j < listnums.size(); j++) {
                // Determine the depth and position of the last node in listnums[j]
                int hundredsj = listnums.get(j).get(listnums.get(j).size() - 1) / 100;
                int tensj = (listnums.get(j).get(listnums.get(j).size() - 1) / 10) % 10;

                // Check if the current node is a parent to the last node in the current path
                if ((tensj == 2 * tensi || tensj == 2 * tensi - 1) && hundredsj == hundredsi + 1) {
                    // Add the current node to this path as a parent node
                    List<Integer> tmplist = listnums.get(j);
                    tmplist.add(nums[i]);
                    listnums.set(j, tmplist);  // Update the path with the new node
                    finalsum += onesi;         // Add the value of this node to the final sum
                    count++;
                }

                // Break out if we have added this node to all possible paths for its level
                if (count == Math.pow(2, maxdepth - hundredsi)) {
                    break;
                }
            }

            // If this node did not connect to any paths, start a new path with it
            if (count == 0) {
                List<Integer> newlist = new ArrayList<>();
                newlist.add(nums[i]);
                listnums.add(newlist);
                finalsum += onesi;
            }
        }

        // Return the total sum of all paths
        return finalsum;
    }
}