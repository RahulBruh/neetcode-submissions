class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        words = defaultdict(list)

        for word in strs:
            cur_array = [0]*26
            for l in word:
                cur_array[ord("a") - ord(l)] += 1
            words[tuple(cur_array)].append(word)
            
        output = []
        for v in words.values():
            output.append(v)
        return output
        
        