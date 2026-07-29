class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_map = defaultdict(list)
        visited = set()
        taken_courses = set()
        order = []
        
        for course, pre_course in prerequisites:
            courses_map[course].append(pre_course)


        def dfs(course):
            if course in taken_courses:
                return True
            
            if course in visited:
                return False
            
            visited.add(course)
            
            for pre_course in courses_map[course]:
                if not dfs(pre_course):
                    return False
            taken_courses.add(course)
            order.append(course)
            visited.remove(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []

        return order

            
            