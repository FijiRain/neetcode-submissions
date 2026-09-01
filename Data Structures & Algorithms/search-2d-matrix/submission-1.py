class Solution:
    # def search(self, m: List[int], target: int) -> int:
    #     l = 0
    #     r = len(m) - 1
    #     while l <= r:
    #         mid = (l + r) // 2
    #         if m[mid] == target:
    #             return m[mid]
    #         elif m[mid] > target:
    #             r = mid - 1
    #         else:
    #             l = mid + 1
    #     print(m[r])
    #     return m[r]


    # def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    #     start_line = 0
    #     end_line = len(matrix) - 1

    #     while start_line <= end_line:
    #         mid_line = (start_line + end_line) // 2
    #         clue = self.search(matrix[mid_line], target)
    #         if clue == target:
    #             return True
    #         elif clue > target:
    #             end_line = mid_line - 1
    #         else:
    #             start_line = mid_line + 1
    #     return False

    # intuitive version 
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in matrix:
            for j in i:
                if j == target:
                    return True
        return False

        