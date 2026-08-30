class Solution:
    # def lengthOfLongestSubstring(self, s: str) -> int:
    #     if not s:
    #         return 0

    #     best_seq = 1
    #     current = []
    #     for i in range(len(s)):
    #         if s[i] in current:
    #             if len(current) >= best_seq:
    #                 best_seq = len(current)
    #             current.clear()
    #         current.append(s[i])

    #     return max(best_seq, len(current))

    def lengthOfLongestSubstring(self, s: str) -> int:
        best = 0
        current = []
        for i in s:
            if i in current:
                index = (current.index(i)) + 1
                current = current[index:]
            current.append(i)
            if len(current) > best:
                best = len(current)

        return max(best, len(current))