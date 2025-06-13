class Solution {
    public int lengthOfLastWord(String s) {
        String[] slist = s.split(" ");
        int n = slist.length;
        return slist[n-1].length();

        
    }
}