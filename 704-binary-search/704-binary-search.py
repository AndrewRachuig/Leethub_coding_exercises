class Solution:
    def search(self, nums: List[int], target: int) -> int:
        position = 0
        if target > nums[-1]:
            return -1
        elif target < nums[0]:
            return -1
        else:
            while nums[0] < target:
                nums.remove(nums[0])
                position += 1
            
            while nums[-1] > target:
                nums.remove(nums[-1])
                if len(nums) == 0:
                    return -1

        return position
