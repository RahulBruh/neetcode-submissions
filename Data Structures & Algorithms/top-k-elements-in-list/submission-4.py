class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]

        

        for n in nums:
            count[n] += 1

        for b, v in count.items():
            freq[v].append(b)
            
        output = []
        for l in range(len(freq) -1, -1, -1):
            for n in freq[l]:
                output.append(n)
                if len(output) == k:  
                    return output
