class Solution {
    public boolean isAnagram(String s, String t) {
        int n1=s.length();
        int n2=t.length();
        if(n1!=n2){
            return false;
        }
        char[] str1=s.toCharArray();
        char[] str2=t.toCharArray();
        Arrays.sort(str1);
        Arrays.sort(str2);
        for(int i=0;i<n1;i++){
            if(str1[i]==str2[i]){
                continue;
            }
            else{
                return false;
            }
        }
        return true;
    }
}
