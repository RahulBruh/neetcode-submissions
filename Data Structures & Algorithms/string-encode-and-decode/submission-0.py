class Solution:

    def encode(self, strs: List[str]) -> str:
        self.breaks = []
        
        for i in range(len(strs)):
            self.breaks.append(len(strs[i]))


        
        cuh = "".join(strs[i] for i in range(len(strs)))


        return cuh

    def decode(self, s: str) -> List[str]:
        decoded = []

        start = 0
        end = 0

        for i in range(len(self.breaks)):
            end += self.breaks[i]
            decoded.append(s[start: end])

            
            start = end


        return decoded