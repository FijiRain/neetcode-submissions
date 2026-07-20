class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        res = []

        # dict initialization
        count = dict()
        for i in set(nums):
            count[i] = 0

        # count occurences
        for i in nums:
            count[i] += 1

        rev_sorted_dic = sorted(count.items(), key=lambda k: k[1], reverse=True)
        for i in rev_sorted_dic:
            res.append(i[0])
            
        return res[:k]