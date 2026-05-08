class Solution {
    public List<String> subdomainVisits(String[] cpdomains) {
        
        HashMap<String, Integer> hashmap = new HashMap<>();

        for (String s: cpdomains){
            String[] splitSCount = s.split(" ");
            int count = Integer.valueOf(splitSCount[0]);

            String[] domains = splitSCount[1].split("\\.");
           

            for (int idx = 0; idx < domains.length; idx ++){
                String current = String.join(".", Arrays.copyOfRange(domains, idx, domains.length));
                hashmap.put(current, hashmap.getOrDefault(current,0)+count);
            }
        }

        List<String> res = new ArrayList<>();

        for (String domain: hashmap.keySet()){
            StringBuilder sb = new StringBuilder();
            sb.append(hashmap.get(domain).toString()+ " "+domain);
            res.add(sb.toString());
        }
        return res;
    }
}