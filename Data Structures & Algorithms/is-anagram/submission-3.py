class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        t_count = defaultdict(int)

        for l in s:
            s_count[l] += 1
        for l in t:
            t_count[l] += 1
        
        return s_count == t_count