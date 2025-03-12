#Q2
import random
import time
from queue import PriorityQueue
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

def update_edge_costs(graph):
    """Randomly updates edge costs to simulate dynamic changes."""
    for node in graph:
        for neighbor in graph[node]:
            if random.random()<0.2:  #20% chance of cost update
                graph[node][neighbor] = random.randint(1, 20)
    print("\nUpdated edge costs:", graph)

def adaptive_a_star(graph, start, goal):
    frontier = PriorityQueue()
    frontier.put((heuristic[start], start))
    g_costs = {start: 0}  
    came_from = {start: None} 
    while not frontier.empty():
        current_f, current_node = frontier.get()

        print(current_node, end=" ")
        if current_node == goal:
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node = came_from[current_node]
            path.reverse()
            print(f"\nGoal found with A*. Path: {path}")
            return

        update_edge_costs(graph)
        
        for neighbor, cost in graph[current_node].items():
            new_g_cost = g_costs[current_node] + cost 
            f_cost = new_g_cost + heuristic[neighbor]  

            if neighbor not in g_costs or new_g_cost < g_costs[neighbor]:
                g_costs[neighbor] = new_g_cost
                came_from[neighbor] = current_node
                frontier.put((f_cost, neighbor))
                
        time.sleep(1)  

    print("\nGoal not found")

print("\nFollowing is the Adaptive A* Search:")
adaptive_a_star(graph, 'A', 'G')