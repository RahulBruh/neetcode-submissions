class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums)+1)]

        for n in nums:
            if n not in count:
                count[n] = 0
            count[n]+=1
        for n,c in count.items():
            freq[c].append(n)
        
        results=[]
        for n in range(len(freq)-1,0,-1):
            for num in freq[n]:
                results.append(num)
                if len(results)==k:
                    return results
