class Solution {
    public boolean judgeCircle(String moves) {

        int[] steps = new int[2];

        for (char c: moves.toCharArray()){
            if (c == 'U'){
                steps[0] -= 1;
            } else if (c == 'D'){
                steps[0] += 1;
            } else if (c == 'L'){
                steps[1] -= 1;
            } else steps[1] += 1;
        }


        return (steps[0] == 0 && steps[1] == 0);
    }
}