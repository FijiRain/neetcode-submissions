class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = []
        sublist = []
        for i in nums:
            if i == 1:
                sublist.append(i)
            else:
                res.append(sublist)
                # print(res)
                sublist = []
        if nums[-1] == 1:
            res.append(sublist)

        return max(len(i) for i in res)