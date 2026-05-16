class Solution {
    public int reverse(int x) {
        int sign = (x < 0 ? -1 : 1);
        int posx = Math.abs(x);
        long reversex = 0L;

        while (posx > 0){
            
            reversex = reversex*10 + (long) posx%10;
            
            posx /= 10;
        }

        if (reversex > Integer.MAX_VALUE) return 0;

        return (int) (sign*reversex);
        
    }
}