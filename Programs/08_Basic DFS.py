def DFS(graph,start,visited=None):
    if visited is None:
        visited=set()
    
    print(start,end=" ")
    visited.add(start)
    
    for neighbour in graph[start]:
        if neighbour not in visited:
            DFS(graph,neighbour,visited)
    

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

# Run DFS starting from node 'A'
print("Depth First Search (Recursive):")
DFS(graph, 'A')
