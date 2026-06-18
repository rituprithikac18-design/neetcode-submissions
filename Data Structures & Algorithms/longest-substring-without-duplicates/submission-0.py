class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash={}
        n=len(s)
        l,r,maxlen=0,0,0
        for r in range(n):
            if s[r] in hash and hash[s[r]]>=l:
                    l=hash[s[r]]+1
            lenn=r-l+1
            maxlen=max(lenn,maxlen)
            hash[s[r]]=r
        return maxlen
