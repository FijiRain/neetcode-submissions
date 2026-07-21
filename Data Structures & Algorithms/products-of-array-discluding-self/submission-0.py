class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        i = 0

        while i < len(nums):
            exception = i
            nb = 1
            for j in range(len(nums)):
                if j == exception:
                    continue
                nb *= nums[j]
            res.append(nb)
            i += 1

        return res