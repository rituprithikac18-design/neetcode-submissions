class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = [c.lower() for c in s if c.isalnum()]
        l,r=0,len(s)-1
        while l < r:
            if s[l]==s[r]:
                pass
            else:
                return False
            r-=1
            l+=1
        return True
