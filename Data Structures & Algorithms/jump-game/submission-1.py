class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums)-1
        for i in range(len(nums)-1, -1, -1):
            # is this index reachable
            # if so this is your new testing point
            if i + nums[i] >= goal:
                goal = i

        return goal == 0
            