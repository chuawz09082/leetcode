class Solution {

    public List<Integer> findMinHeightTrees(int n, int[][] edges) {
        if (n == 1) return new ArrayList<>(List.of(0));

        List<Set<Integer>> adjacentList = new ArrayList<>();

        for (int idx = 0; idx < n; idx++) adjacentList.add(new HashSet<>());

        for (int[] edge: edges){
            adjacentList.get(edge[0]).add(edge[1]);
            adjacentList.get(edge[1]).add(edge[0]);
        }

        List<Integer> leaves = new ArrayList<>();

        for (int idx = 0; idx < n; idx++) {
            if (adjacentList.get(idx).size() == 1) leaves.add(idx);
        }

        while (n > 2){
            n -= leaves.size();
            List<Integer> newLeaves = new ArrayList<>();

            for (int leaf: leaves){
                int nextLeaf = adjacentList.get(leaf).iterator().next();
                adjacentList.get(nextLeaf).remove(leaf);
                if (adjacentList.get(nextLeaf).size() == 1) newLeaves.add(nextLeaf);
            }

            leaves = newLeaves;
        }


        return leaves;


    }

}