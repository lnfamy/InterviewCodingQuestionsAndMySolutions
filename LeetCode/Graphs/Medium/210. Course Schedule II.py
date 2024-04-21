"""
https://leetcode.com/problems/course-schedule-ii/description/
"""
from typing import List


class Solution:
    """
    approach:
        1. we create a graph to represent the prerequisite relationships between
            the courses.
        2. we use a dictionary where each key represents a course, and its
            corresponding value is the list of prerequisite courses required
            to take that course

    """

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build dictionary to represent prerequisites
        pre = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            pre[course].append(prereq)

        res = []
        visited, cycle = set(), set()

        # create a dfs function to traverse the graph
        def dfs(course):
            # if course is part of a cycle, we cannot take all courses no matter what
            if course in cycle:
                return False
            # if course has already been visited but isn't part of a cycle, it's ok
            if course in visited:
                return True

            # now add course to cycle check
            cycle.add(course)
            # recursively explore the prerequisites
            # if we find a cycle in this check, return False
            for prereq in pre[course]:
                if dfs(prereq) == False:
                    return False

            # now that we've concluded this check, we can remove this course from
            # the cycle set.
            cycle.remove(course)
            # add this course to visited set and result list
            visited.add(course)
            res.append(course)
            return True

        # now, outside of the dfs function - we iterate through each course
        # and call for the dfs traversal for each one
        for course in range(numCourses):
            # if any given course gives us an error, return an empty list
            if dfs(course) == False:
                return []

        return res
