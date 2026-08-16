class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        cuh = defaultdict(list)

        for w in strs:
            pattern = [0] * 26
            for l in w:
                pattern[ord('a') - ord(l)] += 1
            cuh[tuple(pattern)].append(w)
        output = []
        for v in cuh.values():
            bruh = []
            for w in v:
                bruh.append(w)
            output.append(bruh)
        return output
            
