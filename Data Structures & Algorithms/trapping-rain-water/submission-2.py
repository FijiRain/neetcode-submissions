class Solution:
    def area(self, f_wall: int, n_wall: int, heights: list[int]) -> int:
        res = 0
        diff = min(heights[f_wall], heights[n_wall])
        for i in range(f_wall + 1, n_wall):
            # Pour faire la borne superieure
            res += diff - heights[i]
        return res
        

    def find_first_wall(self, height: list[int], start: int) -> int:
        first_w = -1

        for i in range(start, len(height) - 1):
            if height[i+1] < height[i]:
                first_w = i
                break
        return first_w

    def next_wall(self, height: list[int], start: int) -> int:
        if start == -1:
            return -1
        next_w = -1
        # +1 parce que on ne veut pas prendre start dans l'intervalle 
        local_height = -1
        local_index = -1
        for i in range(start + 1, len(height)):
            if height[i] > local_height:
                local_height = height[i]
                local_index = i
            if local_height >= height[start]:
                return local_index
        return local_index 

    def trap(self, height: List[int]) -> int:
        current = 0
        filled = 0
        while current < len(height):
            f_wall = self.find_first_wall(height, current)
            n_wall = self.next_wall(height, f_wall)
            # Error case
            if f_wall == -1:
                break
            filled += self.area(f_wall, n_wall, height)
            current = n_wall
        return filled
