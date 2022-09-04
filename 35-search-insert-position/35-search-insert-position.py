class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        elif target > nums[-1]:
            return len(nums)
        else:
            for i in range(len(nums)):
                if nums[i] < target:
                    pass
                else:
                    return i