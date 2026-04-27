class Solution {
    public List<String> letterCombinations(String digits) {
        HashMap<Character, List<Character>> hashmap = new HashMap<>();
        hashmap.put('2', List.of('a', 'b', 'c'));
        hashmap.put('3', List.of('d', 'e', 'f'));
        hashmap.put('4', List.of('g', 'h', 'i'));
        hashmap.put('5', List.of('j', 'k', 'l'));
        hashmap.put('6', List.of('m', 'n', 'o'));
        hashmap.put('7', List.of('p', 'q', 'r', 's'));
        hashmap.put('8', List.of('t', 'u', 'v'));
        hashmap.put('9', List.of('w', 'x', 'y', 'z'));

        ArrayDeque<StringBuilder> queue = new ArrayDeque<>();

        for (Character c: hashmap.get(digits.charAt(0))){
            queue.addLast(new StringBuilder().append(c));

        }


        int idx = 1;
        int n = digits.length();
        

        while (idx < n){
            int size = queue.size();
            char chr = digits.charAt(idx);

            for (int i = 0; i < size; i++){
                StringBuilder sb = queue.poll();

                for (Character c: hashmap.get(chr)){
                    StringBuilder tmp = new StringBuilder(sb);
                    tmp.append(c);
                    queue.addLast(tmp);

                }
            }

            idx++;
        }

        List<String> answer = new ArrayList<>();

        for (StringBuilder sbuilder: queue){
            answer.add(sbuilder.toString());
        }

        return answer;
        
    }
}