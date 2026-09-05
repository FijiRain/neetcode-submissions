class Solution:
    # def is_zero(self, a:int, b: int, c: int) -> bool:
    #     return a + b + c == 0

    # def threeSum(self, nums: List[int]) -> List[List[int]]:
    #     triplets = []

    #     start = 0
    #     end = len(nums) - 1

    #     for _ in nums[1:end]:
    #         for j in nums[1:end]:
    #             # print(f"{nums[start]}     {j}     {nums[end]}")
    #             if self.is_zero(nums[start], j, nums[end]):
    #                 output = sorted([nums[start], j, nums[end]])
    #                 # print(f"Output = {output}")
    #                 if output not in triplets:
    #                     triplets.append(output)
    #         end -= 1

    #     return triplets

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        triplets = []

        for i in range(len(nums)):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                sum = nums[i] + nums[l] + nums[r]
                if sum == 0:
                    output = [nums[i], nums[l], nums[r]]
                    if output not in triplets:
                        triplets.append(output)
                if sum > 0:
                    r -= 1
                if sum <= 0:
                    l += 1

        return triplets
        