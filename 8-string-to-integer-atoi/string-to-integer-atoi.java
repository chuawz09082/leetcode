class Solution {
    public int myAtoi(String s) {
        String sStrip = s.strip();
        int n = sStrip.length();

        if (n == 0) return 0;

        int sign = 1;
        int idx = 0;

        if (sStrip.charAt(0) == '-'){
            sign = -1;
            idx = 1;
        } else if (sStrip.charAt(0) == '+'){
            idx = 1;
        }


        long ans = 0;

        while (idx < n){
            if (ans > Integer.MAX_VALUE || sStrip.charAt(idx) - '0' < 0 || sStrip.charAt(idx) - '0' > 9) break;
            ans = ans*10 + (long) (sStrip.charAt(idx) - '0');
            idx++;
        }


        if (ans > Integer.MAX_VALUE){
            return (sign == 1 ? Integer.MAX_VALUE : Integer.MIN_VALUE);
        }

        return (int) (sign*ans);

        

        

    }
}