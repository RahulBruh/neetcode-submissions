class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            test_num = target - nums[i]
            
            if test_num in hashmap:
                return [hashmap[test_num], i]  # order doesn't really matter

            if nums[i] not in hashmap:
                hashmap[nums[i]] = i