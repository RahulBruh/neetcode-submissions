class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        bruh = set(nums)
        longest = 0

        for n in bruh:
            if (n-1) not in bruh:
                length = 1
                while (n + length) in bruh:
                    length += 1
                longest = max(length, longest)
        return longest

