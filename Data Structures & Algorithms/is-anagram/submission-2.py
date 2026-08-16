class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_count = defaultdict(int)
        for i in s:
            s_count[i] += 1
        t_count = defaultdict(int)
        for i in t:
            t_count[i] += 1
        
        return s_count == t_count