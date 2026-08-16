class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj = {
            i : [] for i in range(numCourses)
        }
        for cell in prerequisites:
            adj[cell[0]].append(cell[1])
        seen = set()

        def dfs(crs):
            if crs in seen:
                return False

            if adj[crs] == []:
                return True
            
            seen.add(crs)
            for course in adj[crs]:
                if dfs(course) == False:
                    return False
            seen.remove(crs)
            adj[crs] = []
            return True
            
        for crs in range(numCourses):
            if dfs(crs) == False:
                return False
        return True
