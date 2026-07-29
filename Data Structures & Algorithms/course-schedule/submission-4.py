class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_map = defaultdict(list)
        visited = set()

        for course, pre_requisite in prerequisites:
            courses_map[course].append(pre_requisite)

        def dfs(course):
            if course not in courses_map:
                return True
            if course in visited:
                return False
            visited.add(course)
            outputs = []
            for pre_course in courses_map[course]:
                outputs.append(dfs(pre_course))

            if all(outputs):
                del(courses_map[course])
                return True
            else:
                return False

        for course in list(courses_map.keys()):
            if not dfs(course):
                return False

        return True
                 





#        1
#        [] -> true
#
#        2
#        [0,1] -> true
#
#        2
#        [[0,1],[1,0]] -> false