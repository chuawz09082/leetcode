class Solution {
    private int[] parent;
    public int earliestAcq(int[][] logs, int n) {

        Arrays.sort(logs, (a,b) -> a[0] - b[0]);

        parent = new int[n];

        for (int i = 0; i < n; i++) parent[i] = i;

        int numOfDisconnected = n;

        for (int[] log: logs){
            int x = log[1];
            int y = log[2];

            if (find(x) != find(y)){
                numOfDisconnected --;
                union_find(x,y);
            }


            if (numOfDisconnected == 1) return log[0];

            
        }


        return -1;
        
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