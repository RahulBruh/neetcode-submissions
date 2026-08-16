from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = defaultdict(int)

        bruh = defaultdict(int)

        for i in s:
            count[i] += 1

        for i in t:
            bruh[i] += 1
        
        if count == bruh:
            return True
        else:
            return False


