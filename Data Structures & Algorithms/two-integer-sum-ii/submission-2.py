class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sum_nb = float("inf")
        start = 0
        end = len(numbers) - 1
        while sum_nb != target:
            sum_nb = numbers[start] + numbers[end]
            if end == 0:
                end = len(numbers)
                start += 1
            if sum_nb != target:
                end -= 1

        return [start + 1, end + 1]