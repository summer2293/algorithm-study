from typing import List

# 4th attempt, is this simply cycle detection?


class Solution:
    def DFS(self, taken, graph, start):
        print('DFS')
        print(start, 'start', taken, 'taken')
        # got to end of graph ,no cycle detected
        if start not in graph:
            return False
        # cycle detected, already visited
        if start in taken:
            print("CYLCLE DETECETD")
            return True
        for i in graph[start]:
            new_taken = taken
            new_taken.add(start)
            # print("dfs enterend, taken, i", taken, i)
            return self.DFS(new_taken, graph, i)

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if not prerequisites or not numCourses:
            return True
        graph = dict()
        courses = set()  # used to keep track of most "basic" courses
        advanced = set() # keep track of "advanced" courses
        # make graph
        for prerequisite in prerequisites:
            advanced.add(prerequisite[0])
            courses.add(prerequisite[1])
            if prerequisite[1] in graph:
                graph[prerequisite[1]].append(prerequisite[0])
            else:
                graph[prerequisite[1]] = [prerequisite[0]]


        courses -= advanced
        print(courses, 'courses')
        if not courses:
            return False
        # check cycle
        for course in courses:  # loop checking all introductory classes
            taken = set()
            taken.add(course)
            for i in graph[course]:  # see what classes can be taken after introductory class
                if self.DFS(taken, graph, i):
                    return False
            if len(taken) == numCourses:
                print("lenght")
                return True
        print("end")
        return True


answer = Solution()
# print(answer.canFinish(3,[[1, 0], [1, 2], [0, 1]]))  # expected false
# print(answer.canFinish(3,[[1, 0], [2, 0]]))  # expected true

# print(answer.canFinish(3,[[0, 2], [1, 2], [2, 0]]))  # expected false

# print(answer.canFinish(4,[[0, 1], [0, 2], [1, 3], [3, 0]]))  # expected false

# print(answer.canFinish(2, [[0, 1], [1, 0]]))  # expected false

print(answer.canFinish(4,[[0,1],[3,1],[1,3],[3,2]])) # expected false


# 3rd attempt, have two lists, one for pre -> course, one for course -> pre
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         if not prerequisites or not numCourses:
#             return True
#         need_to = [None] * numCourses
#         leads_to = [None] * numCourses
#         for direction in prerequisites:
#             need_to[direction[0]] = direction[1]
#             leads_to[direction[1]] = direction[0]
#             # check circular
#             if leads_to[direction[0]] == direction[1] and need_to[direction[0]] == direction[1]:
#                 return False
#             if leads_to[direction[1]] == direction[0] and need_to[direction[1]] == direction[0]:
#                 return False

#         # find the most 'basic' course
#         try:
#             idx = need_to.index(None)
#         except:
#             return False

#         completed = 1
#         chances = numCourses-1
#         while chances > 0:
#             chances-=1
#             try:
#                 idx = leads_to[idx]
#             except:
#                 return True
#             completed += 1
#         if idx == None or leads_to[idx] == None or completed == numCourses:
#                 return True
#         # print('last false')
#         return False


# 2nd attempt, turns out there are cases when # of prerequisites don't match numCourses and stuff like that
# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         poten_prerequisite = set()
#         if numCourses == 0:
#             return False
#         if not prerequisites:
#             return True

#         for i in prerequisites:
#             poten_prerequisite.add(i[1])
#         uf = [None] * numCourses
#         for prerequisite in prerequisites:
#             uf[prerequisite[1]] = prerequisite[0]
#             try:
#                 poten_prerequisite.remove(prerequisite[0])
#             except:
#                 if len(poten_prerequisite) == 0:
#                     print("len")
#                     return False
#         print(poten_prerequisite)
#         try:
#             idx = poten_prerequisite.pop()
#         except:
#             print('poten pop')
#             return False
#         completed = set()
#         completed.add(idx)
#         for _ in range(numCourses-1):
#             if uf[idx] == None:
#                 completed.add(uf[idx])
#                 continue
#             temp = uf[idx]
#             idx = temp
#             completed.add(temp)
#             if len(completed)== numCourses:
#                 print('len equasl')
#                 print(completed)
#                 return True

#         print(completed)
#         return len(completed) ==  numCourses


# strategy if mulitple prerequisites could point to same course:
# have a set of courses you can take with no prerequiiste
# do bfs on each couse in set
# and see if longest path is longer than numCourses

# class Solution:

#     def __init__(self):
#         self.course_taken = set() # set of all taken courses

#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         courses = [[] for i in range(numCourses)] # index denotes prequisites, USE -2 to denote ultimate course
#         beginner = set([i for i in range(numCourses)]) #set of courses with no requirements
#         for prerequisite in prerequisites:
#             courses[prerequisite[1]] = prerequisite[0]
#             beginner.remove(prerequisite[1])
#         for elementary in beginner:
#             stack = [] # stack for BFS
#             temp = numCourses
#             if self.BFS(temp, courses, elementary, stack):
#                 return True
#         return False

#     def BFS(self, numCourses, courses, elementary, stack):
#         if len(self.course_taken) >= numCourses:
#             return True
# return False
