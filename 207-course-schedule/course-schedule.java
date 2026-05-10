class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] indegree = new int[numCourses];
        List<List<Integer>> adj = new ArrayList<>();

        for (int idx = 0; idx < numCourses; idx++){
            adj.add(new ArrayList<>());
        }

        for (int[] prerequisite: prerequisites){
            adj.get(prerequisite[1]).add(prerequisite[0]);
            indegree[prerequisite[0]]++;
        }

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < numCourses; i++){
            if (indegree[i] == 0) queue.offer(i);
        }

        int nodesVisited = 0;
        while (!queue.isEmpty()){
            int current = queue.poll();
            nodesVisited += 1;

            for (int nextCourse: adj.get(current)){
                indegree[nextCourse]--;
                if (indegree[nextCourse] == 0) queue.offer(nextCourse);
            }
        }

        return nodesVisited == numCourses;
    }
}