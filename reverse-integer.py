class Solution:
    def reverse(self, x: int) -> int:
        val = str(x)
        neg = False
        store = 0
        if val[0] == '-':
            neg = True
            val = val[1:]
        for a in range(len(val) - 1, -1, -1):
            store += int(val[a]) * (10 ** a)
        if neg:
            store *= -1
        return store


print(Solution().reverse(-40))
