class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = "aeiouAEIOU"
        s =list(s)
        
        i = 0
        j = len(s)-1
        
        while i < j :
            if s[i] not in vow :
                i = i+1
            elif s[j] not in vow :
                j = j-1
            else :
                s[i],s[j] = s[j],s[i]
                i = i+1
                j = j-1 
        return "".join(s)