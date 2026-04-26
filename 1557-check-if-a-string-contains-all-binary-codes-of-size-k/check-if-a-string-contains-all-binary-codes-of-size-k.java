class Solution {
    public boolean hasAllCodes(String s, int k) {
        int total = (int) Math.pow((double) 2,(double) k);

        int n = s.length();

        if (n - k + 1 < total) return false;

        HashSet<String> binaries = new HashSet<>();

        for (int i = 0; i <= n-k; i++){
            String subString = s.substring(i,i+k);
            binaries.add(subString);
        }

        return binaries.size() == total;
        
    }
}