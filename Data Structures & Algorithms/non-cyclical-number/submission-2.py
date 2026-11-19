class Solution:
    def isHappy(self, n: int) -> bool:
        explored = []
        current = n
        while current not in explored:
            # print(current)
            explored.append(current)
            current = self.cyclic_sum(current)
            if current == 1:
                return True
        return False

    def cyclic_sum(self, n: int) -> int:
        total = 0
        str_n = str(n)
        for i in range(len(str_n)):
            total += int(str_n[i])**2
        return total

        