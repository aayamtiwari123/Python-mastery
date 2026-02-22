from collections import deque


def BFS(graph, start):
    visited = set()  # use set to track visited nodes
    queue = deque([start])  # queue initialized with start node
    visited.add(start)  # mark start as visited

    while queue:
        node = queue.popleft()  # dequeue from the front
        print(node, end=" ")  # visit the node

        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append(neighbour)  # enqueue unvisited neighbor


graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

print("Breadth First Search (BFS):")
BFS(graph, 'A')
