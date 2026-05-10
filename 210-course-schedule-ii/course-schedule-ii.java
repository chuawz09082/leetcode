class Solution {
    public int[] findOrder(int numCourses, int[][] prerequisites) {
        int[] orderingCourses = new int[numCourses];
        int[] inDegree = new int[numCourses];

        List<List<Integer>> adjacentList = new ArrayList<>();

        for (int i = 0; i < numCourses; i++){
            adjacentList.add(new ArrayList<>());
        }

        for (int[] prerequisite: prerequisites){
            adjacentList.get(prerequisite[1]).add(prerequisite[0]);
            inDegree[prerequisite[0]] ++;
        }

        Queue<Integer> queue = new LinkedList<>();

        for (int i = 0; i < numCourses; i++){
            if (inDegree[i] == 0) queue.add(i);
        }

        int numOfNodes = 0;
        int[] coursesSequence = new int[numCourses];

        while (!queue.isEmpty()){
            int currentNode = queue.poll();
            coursesSequence[numOfNodes] = currentNode;
            numOfNodes ++;

            for (int nextCourse: adjacentList.get(currentNode)){
                inDegree[nextCourse] --;
                if (inDegree[nextCourse] == 0) queue.add(nextCourse);
            }
        }


        return (numOfNodes == numCourses ? coursesSequence : new int[0]);


    }
}