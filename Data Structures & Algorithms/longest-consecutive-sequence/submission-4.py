class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        s_nums = set(nums)
        best_seq = 0
        for i in s_nums:
            if i - 1 not in s_nums:
                seq = 1
                start = i
                while start + 1 in s_nums:
                    start += 1
                    seq += 1
                if seq > best_seq:
                    best_seq = seq

        return best_seq