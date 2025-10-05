import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    previous = {node: None for node in graph}

    distances[start] = 0
    heap = [(0, start)]

    while heap:
        current_distance, current_node = heapq.heappop(heap)

        for node, weight in graph[current_node]:
            distance = current_distance + weight
            if distance < distances[node]:
                distances[node] = distance
                previous[node] = current_node
                heapq.heappush(heap, (distance, node))

    return previous, distances


def get_path(previous, end):
    path = []
    node = end
    while node is not None:
        path.append(node)
        node = previous[node]
    path.reverse()
    return path


graph = {
    "A": [("B", 4), ("C", 2)],
    "B": [("C", 5), ("D", 10)],
    "C": [("D", 3)],
    "D": []
}

start_node = "A"
previous, distances = dijkstra(graph, start_node)

# Print shortest distances
print("Shortest distances from", start_node)
for node, dist in distances.items():
    print(f"{start_node} -> {node} = {dist}")

# Print actual shortest paths
print("\nShortest paths from", start_node)
for node in graph:
    path = get_path(previous, node)
    print(f"{start_node} -> {node}: {path}")
