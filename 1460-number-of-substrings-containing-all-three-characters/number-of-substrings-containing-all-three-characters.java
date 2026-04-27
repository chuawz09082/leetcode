class Solution {
    public int numberOfSubstrings(String s) {
        int n = s.length();
        int count = 0;
        int end = 0;

        HashMap<Character, Integer> hashmap = new HashMap<>();

        for (int i = 0; i < n; i++) {

            // expand window
            while (end < n && hashmap.size() < 3) {
                hashmap.put(s.charAt(end),
                        hashmap.getOrDefault(s.charAt(end), 0) + 1);
                end++;
            }

            // count valid substrings
            if (hashmap.size() == 3) {
                count += n - end + 1;
            }

            // shrink window from left
            char leftChar = s.charAt(i);
            hashmap.put(leftChar, hashmap.get(leftChar) - 1);
            if (hashmap.get(leftChar) == 0) {
                hashmap.remove(leftChar);
            }
        }

        return count;
    }
}