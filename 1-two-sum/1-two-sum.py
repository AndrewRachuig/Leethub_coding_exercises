class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            var1 = nums[i]
            next_list = nums[i+1:]
            for j in range(len(next_list)):
                if var1 + next_list[j] == target:
                    return [i, (i+j+1)]