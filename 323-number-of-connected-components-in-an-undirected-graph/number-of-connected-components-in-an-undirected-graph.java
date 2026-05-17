class Solution {
    private int[] parent;


    public int countComponents(int n, int[][] edges) {
        parent = new int[n];

        for (int i = 0; i < n; i++) parent[i] = i;

        int numOfComponents = n;

        for (int[] edge: edges){
            int i = edge[0];
            int j = edge[1];
            if (find(i) != find(j)){
                union_find(i,j);
                numOfComponents -= 1;
            }
        }

        return numOfComponents;
    }

    private int find(int x){
        if (x != parent[x]) parent[x] = find(parent[x]);
        return parent[x];
    }

    private void union_find(int x, int y){
        int parentx = find(x);
        int parenty = find(y);

        if (parentx == parenty) return;
        else if (parentx < parenty) parent[parenty] = parentx;
        else parent[parentx] = parenty;
    }
}