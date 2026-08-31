class Solution:
    # Intuitive solution but not optimized
    # def search(self, nums: List[int], target: int) -> int:
    #     if target in nums:
    #         return nums.index(target)
    #     return -1

    # Legit way of doing binary search
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (r + l) // 2
            if nums[mid] == target:
                    return mid
            elif nums[mid] > target:
                r = mid - 1
            else:
                l = mid + 1 
        return -1