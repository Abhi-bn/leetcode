class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) == 0:
            return True
        pos = 0
        index = 0
        while(True):
            if pos > len(s) - 1:
                break
            if index > len(t) - 1:
                break
            if s[pos] == t[index]:
                pos += 1

            index += 1

        return pos > len(s) - 1
