class Solution {
    public double[] calcEquation(List<List<String>> equations, double[] values, List<List<String>> queries) {
        Map<String, Map<String, Double>> graph = buildGraph(equations, values);
        int n = queries.size();
        double[] ans = new double[n];

        for (int idx = 0; idx < n;idx++){
            String u = queries.get(idx).get(0);
            String v = queries.get(idx).get(1);

            ans[idx] = getResult(u,v,graph, new HashSet<>(), 1.0);
        }


        return ans;
    }

    private double getResult(String u, String v, Map<String, Map<String, Double>> graph, Set<String> visited,  double val){
        visited.add(u);
        

        if (!graph.containsKey(u)) return -1.0;

        if (u.equals(v)) return val;
        
        for (String s: graph.get(u).keySet()){

                if (!visited.contains(s)){
                    double res = getResult(s,v,graph, visited, val*graph.get(u).get(s));
                    if (res != -1.0) return res;
                }
            }
        

        return -1.0;
    }

    private Map<String, Map<String, Double>> buildGraph(List<List<String>> equations, double[] values){
        Map<String, Map<String,Double>> graph = new HashMap<>();
        int n = equations.size();

        for (int idx = 0; idx < n;idx++){
            String u = equations.get(idx).get(0);
            String v = equations.get(idx).get(1);

            graph.computeIfAbsent(u, k -> new HashMap<>()).put(v, values[idx]);
            graph.computeIfAbsent(v, k -> new HashMap<>()).put(u, 1.0/values[idx]);
        }

        return graph;


    }
}