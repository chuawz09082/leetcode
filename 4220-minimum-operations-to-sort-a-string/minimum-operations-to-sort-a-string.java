class Solution {
    public int minOperations(String s) {
        int n = s.length();
        boolean allasc = true;
        int min = Integer.MAX_VALUE;
        int max = Integer.MIN_VALUE;
        
        for (int idx = 0; idx < n-1; idx++){
            
            if ((int) s.charAt(idx) > (int) s.charAt(idx+1)) allasc = false;

            if (idx > 0){
                min = Math.min(min, (int) s.charAt(idx));
                max = Math.max(max, (int) s.charAt(idx));
            }
            
        }

        if (allasc == true) return 0;

        if (n == 2 && allasc == false) return -1;


        int first = (int) s.charAt(0);
        int last = (int) s.charAt(n-1);

        if (first <= last && (min >= first || max <= last)) return 1;
 

        return (first > max && last < min ? 3 : 2);
    }
}