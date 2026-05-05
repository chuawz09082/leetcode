class Solution {
    public String longestPalindrome(String s) {
        
        int n = s.length();
        int len = 1;
        String ans = s.substring(0,1);

        for (int l = 2; l <= n; l++){
            for (int start = 0; start <= n - l; start++){
                String subString = s.substring(start, start+l);
                if (isPalindromic(subString) == true){
                    ans = subString;
                    break;
                }
            }
        }

        return ans;
        
    }

    private boolean isPalindromic(String t){
        int len = t.length();

        for (int i = 0; i < len/2; i++){
            if (t.charAt(i) != t.charAt(len-1-i)) return false;
        }

        return true;
    }
}