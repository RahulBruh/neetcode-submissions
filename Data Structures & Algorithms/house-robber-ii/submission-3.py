class Solution:
    def rob(self, nums: List[int]) -> int:
        
        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        temp1 = temp2 = 0
        for n in nums:
            cur = max(temp1 + n, temp2)

            temp1 = temp2

            temp2 = cur
        return temp2