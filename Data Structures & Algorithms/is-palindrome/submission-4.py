class Solution:
    def isPalindrome(self, s: str) -> bool:
        return "".join(filter(str.isalnum, s.lower())) == "".join(filter(str.isalnum, s.lower()))[::-1]   