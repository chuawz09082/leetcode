class Solution {
    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        Map<String, List<Set<String>>> graph = new HashMap<>();

        for (List<String> account: accounts){
            String name = account.get(0);

            graph.putIfAbsent(name, new ArrayList<>());

            List<Set<String>> listOfAccounts = graph.get(name);
            
            int i = 0;
            int size = listOfAccounts.size();

            Set<String> emailAccounts = new HashSet<>(account.subList(1, account.size()));

            while (i < size){
                Set<String> currentAccounts = listOfAccounts.get(i);
                Set<String> emailAccountstmp = new HashSet<>(emailAccounts);
                emailAccountstmp.retainAll(currentAccounts);

                if (!emailAccountstmp.isEmpty()){
                    
                    emailAccounts.addAll(currentAccounts);
                    listOfAccounts.remove(i);
                    size--;
                } else i++;
            }

            graph.get(name).add(emailAccounts);
        }


        List<List<String>> ans = new ArrayList<>();
        
        for (String name: graph.keySet()){
            List<Set<String>> emails = graph.get(name);

            for (Set<String> account: emails){
                List<String> list = new ArrayList<>(account);
                Collections.sort(list);
                list.addFirst(name);
                ans.add(list);
            }
        }

        return ans;
    }
}