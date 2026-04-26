class Solution {
    public String countAndSay(int n) {
        return countRLE(n);
    }

    private String countRLE(int n){
        if (n == 1) return "1";

        String previous = countRLE(n-1);
        StringBuilder sb = new StringBuilder();

        int i = 0;
        int len = previous.length();

        while (i < len){
            char c = previous.charAt(i);
            int count = 1;

            while (i+1 < len && previous.charAt(i+1) == c){
                i++;
                count++;
            }

            sb.append(count);
            sb.append(c);
            i++;
        }


        return sb.toString();

        
    }
}