from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bruh = defaultdict(list)
        chuttey = []

        for w in strs:
            count = [0] * 26

            for c in w:
                count[ord(c) - ord("a")] += 1
            
            bruh[tuple(count)].append(w)
        
        for value in bruh.values():
            chuttey.append(value)

        return chuttey