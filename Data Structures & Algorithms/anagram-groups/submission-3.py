class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        bruh = defaultdict(list)

        for word in strs:
            count = [0] * 26
            for letter in word:
                count[ord(letter) - 97] += 1
            
            bruh[tuple(count)].append(word)
        
        output = []
        for v in bruh.values():
            output.append(v)
        return output
            

