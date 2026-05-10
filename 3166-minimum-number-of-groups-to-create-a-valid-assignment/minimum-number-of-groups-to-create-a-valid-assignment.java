class Solution {
    public int minGroupsForValidAssignment(int[] balls) {
        HashMap<Integer, Integer> counter = new HashMap<>();

        for (int ball: balls){
            counter.put(ball, counter.getOrDefault(ball, 0)+1);
        }

        int min = Collections.min(counter.values());

        for (int size = min; size >= 1; size--){
            int numGroups = groupify(counter, size);
            if (numGroups > 0) return numGroups;
        }
        
        return balls.length;

        
    }

    private int groupify(Map<Integer, Integer> map, int size){
        int groups = 0;
        int next = size + 1;

        for(int value : map.values()) {
            int numGroups = value / next;
            int remaining = value % next;

            if(remaining == 0) {
                groups += numGroups;
            } else if(numGroups >= size - remaining) {
                groups += numGroups + 1;
            } 
            else {
                return 0;
            }
        }

        return groups;
    }
}