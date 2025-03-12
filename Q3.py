#Q3
graph={
    'A': {'B': 2, 'C': 1},
    'B': {'D': 4, 'E': 3},
    'C': {'F': 1, 'G': 5},
    'D': {'H': 2},
    'E': {},
    'F': {'I': 6},
    'G': {},
    'H': {},
    'I': {}
}

heuristic = {'A': 7, 'B': 6, 'C': 5, 'D': 4, 'E': 7, 'F': 3, 'G': 6, 'H': 2, 'I': 0}
time_windows = {'A': 10, 'B': 5, 'C': 7, 'D': 3, 'E': 8, 'F': 6, 'G': 9, 'H': 2, 'I': 1}
def greedy_bfs_delivery(graph, start, goal):
    frontier=[(start, heuristic[start], time_windows[start])] 
    visited=set()
    came_from={start: None}  

    while frontier:
        frontier.sort(key=lambda x: (x[1], x[2]))  
        current_node,_, _=frontier.pop(0)  

        if current_node in visited:
            continue

        print(current_node, end=" ") 
        visited.add(current_node)

        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nOptimized Delivery Route: {path}")
            return

        for neighbor in graph[current_node]:
            if neighbor not in visited:
                came_from[neighbor] = current_node
                frontier.append((neighbor, heuristic[neighbor], time_windows[neighbor]))

    print("\nNo feasible delivery route found.")
print("\nOptimized Delivery Route using GBFS with Time Windows:")
greedy_bfs_delivery(graph, 'A', 'I')
