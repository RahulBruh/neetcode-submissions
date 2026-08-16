class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        numbers = {}

        output = []

        for i in nums:
            if i in numbers:
                numbers[i] += 1
            else:
                numbers[i] = 1


        for n in range(k):
            cuh = 0
            bruh = 0
            for i in numbers:
                if numbers[i] > cuh:
                    cuh = numbers[i]
                    bruh = i

            output.append(bruh)

            del numbers[output[n]]

        return output