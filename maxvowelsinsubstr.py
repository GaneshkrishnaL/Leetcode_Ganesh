class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels={'a','e','i','o','u'}
        curr=0
        for i in range(k):
            if s[i] in vowels:
                curr+=1
        maxx=curr
        for i in range(k,len(s)):
            if s[i] in vowels:
                curr+=1
            if s[i-k] in vowels:
                curr-=1
            maxx=max(curr,maxx)

        return maxx