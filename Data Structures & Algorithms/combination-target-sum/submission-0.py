class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        output = []
        def backtrack(cur, i, total):
            if total == target:
                output.append(cur.copy())
                return
            if i == len(nums) or total > target:
                return
            
            cur.append(nums[i])
            backtrack(cur, i, total + nums[i])
            cur.pop()
            backtrack(cur, i + 1, total)

        backtrack([], 0, 0)
        return output