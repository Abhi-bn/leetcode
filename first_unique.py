class Solution:
    def firstUniqChar(self, s: str) -> int:
        dups = []
        for i, a in enumerate(s):
            if a in dups:
                continue
            dup = False
            for j in range(i + 1, len(s)):
                if s[i] == s[j] and s[j] not in dups:
                    dup = True
                    break
            dups.append(a)
            if dup == False:
                return i
        return -1
