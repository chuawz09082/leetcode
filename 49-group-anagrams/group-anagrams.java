class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        HashMap<String, List<String>> hashmap = new HashMap<>();

        for (String s: strs){
            char[] chars = s.toCharArray();
            Arrays.sort(chars);
            String sorted = new String(chars);

            hashmap.computeIfAbsent(sorted, k -> new ArrayList<>()).add(s);
        }

        List<List<String>> res = new ArrayList<>();

        for (List<String> values: hashmap.values()){
            res.add(values);
        }

        return res;
    }
}