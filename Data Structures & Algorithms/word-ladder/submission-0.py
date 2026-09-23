class Solution:
    def one_letter_diff(self, w1: str, w2: str) -> bool:
        if len(w1) != len(w2):
            return False

        diff = 0
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                diff += 1
        return diff == 1

    def ladderLength(self, start: str, end: str, word_list: List[str]) -> int:
        if len(start) != len(end) or end not in word_list:
            return 0

        visited = {start}
        queue = [(start, 1)]
        while queue:
            next_queue = []
            for name, step in queue:
                if name == end:
                    return step
                for w in word_list:
                    if self.one_letter_diff(name, w) and w not in visited:
                        visited.add(w)
                        next_queue.append((w, step + 1))

            queue = next_queue

        return 0