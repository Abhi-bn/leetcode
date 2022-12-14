from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        l = []
        for i, num in enumerate(nums):
            if i == 0:
                l.append(num)
                continue
            l.append(l[i - 1] + num)
        return l
