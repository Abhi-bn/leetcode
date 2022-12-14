class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        info1 = {}
        for i, c in enumerate(s):
            if c in info1 and info1[c] != t[i]:
                return False
            info1[c] = t[i]
        info2 = {}
        for i, c in enumerate(t):
            if c in info2 and info2[c] != s[i]:
                return False
            info2[c] = s[i]

        return True


# "badc" "baba"
Solution().isIsomorphic("foo", "bar")
