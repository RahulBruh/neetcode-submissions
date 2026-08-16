class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        chuttey = {}
        for i in s:
            if i in chuttey:
                chuttey[i] += 1 #add's everything to hashmap and number of times of apperance
            else:
                chuttey[i] = 1
        for x in t:
            if x in chuttey:
                chuttey[x] -= 1
                if chuttey[x] < 0:
                    return False
            else:
                return False
        for n in chuttey:
            if chuttey[n] > 0:
                return False
        return True
