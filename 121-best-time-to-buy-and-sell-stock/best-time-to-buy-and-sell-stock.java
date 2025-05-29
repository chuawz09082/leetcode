class Solution {
    public int maxProfit(int[] prices) {
        int minstock = Integer.MAX_VALUE;
        int profit = 0;

        for (int num: prices){
            minstock = Integer.min(minstock,num);
            profit = Integer.max(profit,num - minstock);
        }

        return profit;
    }
}