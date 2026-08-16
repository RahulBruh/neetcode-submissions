class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bruh = set(nums)
        longest = 0

        for n in bruh:
            length = 1
            if n-1 not in bruh:
                while n + length in bruh:
                    length += 1
                longest = max(longest, length)
                
        return longest
