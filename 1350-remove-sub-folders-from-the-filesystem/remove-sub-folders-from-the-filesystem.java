class Solution {
    public List<String> removeSubfolders(String[] folder) {
        Arrays.sort(folder);

        List<String> res = new ArrayList<>();

        for (String s: folder){
            if (res.isEmpty()){
                res.add(s);
                continue;
            }

            int len = res.size();
            String[] mainfolder = res.get(len-1).split("/");
            String[] subfolder = s.split("/");

            if (subfolder.length < mainfolder.length){
                res.add(s);
                continue;
            }

            boolean add = false;

            for (int idx = 0; idx < mainfolder.length; idx++){
                if (!mainfolder[idx].equals(subfolder[idx])){
                    add = true;
                    break;
                }
            }

            if (add == true){
                res.add(s);
            }


        }

        return res;
    }
}