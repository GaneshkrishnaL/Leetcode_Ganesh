class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # 5cities from  - 0-4 , 4 edges, poinint either direction b/w cities 
        # need to point all to city zero and return min no of edges changed.


        # need to create a dictionary to keep track of neighbors of each city 
        # also need a visited set to keep track of visited cities in our search

        neighbors=defaultdict(list)
        connection=set()

        for start,end in connections:
            neighbors[start].append(end)
            neighbors[end].append(start)
            connection.add((start,end))

        visited=set()
        reverse=0
        curr=[0]
        visited.add(0)

        while curr:
            updated=[]

            for i in curr:
                nei=neighbors[i]
                for n in nei:
                    if n not in visited:
                        visited.add(n)
                        if (n,i) not in connection:
                            reverse+=1
                        updated.append(n)
                curr=updated
        return reverse
