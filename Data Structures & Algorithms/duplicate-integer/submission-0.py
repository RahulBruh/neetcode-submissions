class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        """
        :type nums: List[int]
        :rtype: bool
        """
        seen = set()
        for x in nums:
            if x in seen:
                return True
            else:
                seen.add(x)
        return False