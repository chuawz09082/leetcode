class Solution {
    public int[][] merge(int[][] intervals) {
        Arrays.sort(intervals, (a,b) -> a[0] != b[0] ? a[0] - b[0] : a[1] - b[1]);

        List<List<Integer>> mergeList = new ArrayList<>();

        for (int[] list: intervals){
            int start = list[0];
            int end = list[1];

            if (mergeList.isEmpty() || start > mergeList.getLast().get(1)){
                mergeList.add(new ArrayList<>(Arrays.asList(start, end)));
            } else {
                List<Integer> last = mergeList.getLast();
                last.set(1, Math.max(last.get(1),end));
            }
        }

        int[][] result = new int[mergeList.size()][2];

        for (int i = 0; i < mergeList.size(); i++) {
            result[i][0] = mergeList.get(i).get(0);
            result[i][1] = mergeList.get(i).get(1);
        }

        return result;


    }
}