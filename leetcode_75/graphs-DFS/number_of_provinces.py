from typing import List, Set

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        """
        Number of Provinces (also known as "Number of Connected Components in an Undirected Graph")

        We are given an adjacency matrix `isConnected` where isConnected[i][j] == 1 means
        city i and city j are directly connected. The task is to determine the number
        of connected components (provinces) in the undirected graph represented by this matrix.

        Approach:
        - Use depth-first search (DFS) to explore all nodes connected to a given node.
        - Maintain a set of visited nodes to avoid revisiting.
        - Iterate through each city; if it hasn't been visited, perform DFS starting from it
          and increment the province count.

        Example:
        --------
        Consider the matrix:
            [
                [1, 1, 0],
                [1, 1, 0],
                [0, 0, 1]
            ]

        - Start with city 0: it is connected to city 1. DFS will visit both 0 and 1.
          These two form one connected component.
        - City 2 is not connected to 0 or 1 (isConnected[2][0] == 0 and isConnected[2][1] == 0),
          so it forms its own component.
        Hence, the total number of provinces is 2.

        Time Complexity: O(n^2), where n is the number of cities, because we potentially inspect each cell in the matrix.
        Space Complexity: O(n) for the visited set and recursion stack.
        """
        n = len(isConnected)
        visited: Set[int] = set()

        def dfs(i: int) -> None:
            """
            Recursively visit all cities connected to city i.
            """
            visited.add(i)
            # Iterate over all possible neighboring cities
            for j in range(n):
                # If city j is connected to i and j has not been visited,
                # recursively visit j
                if isConnected[i][j] == 1 and j not in visited:
                    dfs(j)

        provinces = 0  # Count of connected components
        # Iterate through each city
        for city in range(n):
            # If we haven't visited this city, it's the start of a new province
            if city not in visited:
                dfs(city)  # Visit all cities in this province
                provinces += 1

        return provinces
