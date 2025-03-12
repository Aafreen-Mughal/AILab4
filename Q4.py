#Q4
import random
import time

graph={
    'A': {'B': 4, 'C': 3},
    'B': {'E': 12, 'F': 5},
    'C': {'D': 7, 'E': 10},
    'D': {'E': 2},
    'E': {'G': 5},
    'F': {'G': 16},
    'G': {},
}

heuristic={'A': 14, 'B': 12, 'C': 11, 'D': 6, 'E': 4, 'F': 11, 'G': 0}

def update_traffic():
    for node in graph:
        for neighbor in graph[node]:
            graph[node][neighbor] = max(1, graph[node][neighbor] + random.choice([-2, -1, 0, 1, 2]))

def a_star_real_time(graph, start, goal):
    frontier=[(start, heuristic[start])]  
    visited=set()
    g_costs={start: 0}  
    came_from={start: None}  

    while frontier:
        frontier.sort(key=lambda x: x[1])
        current_node, _=frontier.pop(0)

        if current_node in visited:
            continue

        print(f"Visiting: {current_node}")
        visited.add(current_node)

        if current_node==goal:
            path=[]
            while current_node is not None:
                path.append(current_node)
                current_node=came_from[current_node]
            path.reverse()
            print(f"\nFastest Route Found: {path}")
            return

        update_traffic()
        print(f"Updated Traffic: {graph}")

        for neighbor,cost in graph[current_node].items():
            new_g_cost=g_costs[current_node] + cost  
            f_cost=new_g_cost+heuristic[neighbor]  

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor]=new_g_cost
                came_from[neighbor]=current_node
                frontier.append((neighbor, f_cost))

        time.sleep(1)

    print("\nNo feasible route found.")

print("\nReal-Time A* Navigation with Traffic Updates:")
a_star_real_time(graph, 'A', 'G')
