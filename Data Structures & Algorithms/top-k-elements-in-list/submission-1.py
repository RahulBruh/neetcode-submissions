class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        count = defaultdict(int)
        freq = [[] for i in range(len(nums) + 1)]
        chuttey = []
        for n in nums:
            count[n] += 1
        for n, c in count.items():
            freq[c].append(n)
        for i in range(len(freq) - 1, -1, -1):
            for n in freq[i]:
                chuttey.append(n)
                if len(chuttey) == k:
                    return chuttey
