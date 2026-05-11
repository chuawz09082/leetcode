class Solution {
    public String largestPalindromic(String num) {
        TreeMap<Integer, Integer> map = new TreeMap<>(Collections.reverseOrder());

        for (char c: num.toCharArray()){
            int n = Character.getNumericValue(c);
            map.put(n, map.getOrDefault(n,0)+1);
        }

        int maxSingleDigit = -1;

        for (int key: new ArrayList<>(map.keySet())){
            int count = map.get(key);

            if (count%2 == 1) maxSingleDigit = Math.max(maxSingleDigit, key);

            if (count == 1){ 
                map.remove(key);
            }
            else {
                map.put(key, count/2);
            }

        }

        StringBuilder sb = new StringBuilder();

        for (int key: map.keySet()){
            if (sb.length() == 0 && key == 0) continue;
            sb.append(String.valueOf(key).repeat(map.get(key)));
        }

        StringBuilder reversesb = new StringBuilder(sb).reverse();

        if (maxSingleDigit > -1) sb.append(String.valueOf(maxSingleDigit));

        sb.append(reversesb);

        return (sb.length() > 0 ? sb.toString() : "0");


    }
}