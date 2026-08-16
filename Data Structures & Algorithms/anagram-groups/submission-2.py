from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        chuttey = defaultdict(list)
        output = []
        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord(c) - ord("a")] += 1
            
            chuttey[tuple(count)].append(w)
        
        for value in chuttey.values():
            output.append(value)
        return output