class Solution {
    public boolean canFinish(int numCourses, int[][] prerequisites) {
        int[] inDegree = new int[numCourses];

        HashMap<Integer, List<Integer>> graph = new HashMap<>();

        int total = 0;

        for (int[] p: prerequisites){
            graph.computeIfAbsent(p[1], k -> new ArrayList<>()).add(p[0]);
            inDegree[p[0]] ++;
        }

        ArrayDeque<Integer> queue = new ArrayDeque<>();

        for (int i = 0; i < numCourses; i++){
            if (inDegree[i] == 0) queue.add(i);
        }

        while (!queue.isEmpty()){
            int currentCourse = queue.poll();
            total++;

            if (!graph.containsKey(currentCourse)) continue;

            for (int nextCourse: graph.get(currentCourse)){
                inDegree[nextCourse] --;
                if (inDegree[nextCourse] == 0){
                    queue.add(nextCourse);
                }
            }
        }



        return total == numCourses;
        
    }
}