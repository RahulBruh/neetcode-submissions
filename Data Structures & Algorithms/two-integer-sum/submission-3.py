class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cuh = dict()

        for i, n in enumerate(nums):
            if target - n in cuh:
                return [min(i, cuh[target-n]), max(i, cuh[target-n])]
            cuh[n] = i
            
