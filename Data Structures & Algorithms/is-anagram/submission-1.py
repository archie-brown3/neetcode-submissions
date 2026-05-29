class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # initialise two dictionaries 
        charS, charT = {}, {}
        if len(s) != len(t):
            return False

        for i in range(len(s)):
            # s[i] = key
            charS[s[i]] = 1 + charS.get(s[i], 0)
            charT[t[i]] = 1 + charT.get(t[i], 0)

        print(charS)
        print(charT)

        return charS == charT