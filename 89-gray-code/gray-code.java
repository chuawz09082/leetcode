class Solution {
    public List<Integer> grayCode(int n) {
        List<Integer> result = new ArrayList<>();

        int sequenceLength = 1 << n;

        for (int i = 0; i < sequenceLength; i++){
            int num = i ^ (i >> 1);
            result.add(num);
        }
        
        return result;
    }
}