class Solution {
    public int findCheapestPrice(int n, int[][] flights, int src, int dst, int k) {
        
        Map<Integer, Map<Integer, Integer>> flightmap = new HashMap<>();

        for (int[] flight: flights){
            flightmap.computeIfAbsent(flight[0], l-> new HashMap<>()).put(flight[1], flight[2]);
        }

        int stops = 0;
        int minPrice = Integer.MAX_VALUE;

        Queue<int[]> queue = new LinkedList<>();
        queue.offer(new int[]{src,0});

        int[] bestPrice = new int[n];
        Arrays.fill(bestPrice, Integer.MAX_VALUE);

        while (!queue.isEmpty() && stops <= k+1){
            int size = queue.size();

            for (int i = 0; i < size; i++){
                int[] item = queue.poll();

                bestPrice[item[0]] = Math.min(bestPrice[item[0]], item[1]);

                if (item[0] == dst){
                    minPrice = Math.min(minPrice, item[1]);
                    continue;
                }

                if (!flightmap.containsKey(item[0])) continue;

                Map<Integer, Integer> nextStops = flightmap.get(item[0]);

                for (int nextStop: nextStops.keySet()){
                    if (bestPrice[nextStop] <= item[1]+nextStops.get(nextStop)) continue;
                    queue.offer(new int[]{nextStop, item[1]+nextStops.get(nextStop)});

                }
            }

            stops ++;
        }


        return (minPrice != Integer.MAX_VALUE ? minPrice : -1);



    }
}
