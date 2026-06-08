from typing import List
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)

        # [course, pre] 表示 pre -> course
        for course, pre in prerequisites:
            graph[pre].append(course)

        # 0 = unvisited
        # 1 = visiting，正在目前 DFS 路徑中
        # 2 = visited，已確認安全
        state = [0] * numCourses

        def dfs(course: int) -> bool:
            # 如果又遇到目前路徑上的節點，代表有 cycle
            if state[course] == 1:
                return False

            # 如果之前已經確認安全，直接重用結果
            if state[course] == 2:
                return True

            # 開始探索這門課的後續課程
            state[course] = 1

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            # 所有後續路徑都安全，這門課也安全
            state[course] = 2
            return True

        # 圖可能不是連通的，所以每門課都要當起點檢查一次
        for course in range(numCourses):
            if not dfs(course):
                return False

        return True