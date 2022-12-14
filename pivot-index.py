class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        su = sum(nums)
        ls = 0
        for i, num in enumerate(nums):
            if ls == (su-ls-num):
                return i
            ls += num
        return -1
