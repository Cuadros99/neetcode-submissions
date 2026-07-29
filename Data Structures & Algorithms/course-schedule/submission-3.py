class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_map = defaultdict(list)
        output = True

        for course, pre_requisite in prerequisites:
            courses_map[course].append(pre_requisite)

        def dfs(course, visited):
            nonlocal output

            if not output:
                return
            if course not in courses_map:
                return
            for pre_course in courses_map[course]:
                if pre_course in visited:
                    print(visited)
                    print(pre_course)
                    output = False
                    return
                visited.add(pre_course)
                dfs(pre_course, visited)
                visited.remove(pre_course)

        for course in courses_map:
            if not output:
                break
            dfs(course, {course})

        return output





#        1
#        [] -> true
#
#        2
#        [0,1] -> true
#
#        2
#        [[0,1],[1,0]] -> false