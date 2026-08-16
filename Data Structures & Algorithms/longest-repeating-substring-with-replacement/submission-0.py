class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        output = 1
        l = r = 0
        for c in s:
            count[c] += 1
            r += 1
            if len(count) > 1 and (r - l) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            output = max(output, (r - l))
        return output
            
            
        
        
        
