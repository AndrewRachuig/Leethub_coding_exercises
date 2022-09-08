class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        import math

        max_sum, current_sum = -math.inf,  0

        for element in nums:

            if current_sum < 0:
                current_sum = element
            else:
                current_sum = current_sum + element

            max_sum = max(max_sum, current_sum)

        return max_sum