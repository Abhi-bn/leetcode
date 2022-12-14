from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        sol = []
        for i in range(1, numRows + 1):
            row = []
            for each in range(i):
                if each == 0 or each == i - 1:
                    row.append(1)
                    continue
                row.append(sol[i-2][each - 1] + sol[i-2][each])
            sol.append(row)
        return sol

Solution().generate(10)