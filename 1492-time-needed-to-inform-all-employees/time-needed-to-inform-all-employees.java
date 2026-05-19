class Solution {
    public int numOfMinutes(int n, int headID, int[] manager, int[] informTime) {
        HashMap<Integer, List<Integer>> graph = new HashMap<>();

        for (int i = 0; i < n;i++){
            graph.computeIfAbsent(manager[i], k -> new ArrayList<>()).add(i);

        }

        return dfs(headID,graph, informTime);
        
    }

    private int dfs(int current, HashMap<Integer,List<Integer>> graph, int[] informTime){
        if (informTime[current] == 0) return 0;

        int TotalTime = 0;

        for (int next: graph.get(current)){
            TotalTime = Math.max(TotalTime, informTime[current] + dfs(next, graph, informTime));
        }


        return TotalTime;

    }


}