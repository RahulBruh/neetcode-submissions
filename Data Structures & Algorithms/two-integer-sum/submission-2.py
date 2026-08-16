class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        chuttey = {}
        for i in range(len(nums)):
            if target - nums[i] in chuttey:
                return [min(i, chuttey[target - nums[i]]), max(i, chuttey[target - nums[i]])]
            else:
                chuttey[nums[i]] = i
                

