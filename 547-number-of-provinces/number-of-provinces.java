class Solution {
    int[] parent;
    int n;

    public int findCircleNum(int[][] isConnected) {
        n = isConnected.length;
        parent = new int[n];
        int numberOfComponents = n;

        for (int i = 0; i < n; i++) parent[i] = i;

        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                if (isConnected[i][j] == 1 && find(i) != find(j)){
                    numberOfComponents --;
                    union_find(i,j);
                }
            }
        }

        return numberOfComponents;
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