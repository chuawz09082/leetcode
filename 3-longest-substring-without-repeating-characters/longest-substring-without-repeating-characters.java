class Solution {
    public int lengthOfLongestSubstring(String s) {

        HashSet<Character> seen = new HashSet<>();
        int len = 0;
        int n = s.length();
        int left = 0;

        for (int right = 0; right < n; right++){
            char c = s.charAt(right);

            while (seen.contains(c)){
                seen.remove(s.charAt(left));
                left ++;
            }

            len = Math.max(len, right - left+1);
            seen.add(c);

        }



        return len;
        
    }
}