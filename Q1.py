#Q1
from queue import PriorityQueue
class Node:
    def __init__(self, position, parent=None):
        self.position = position
        self.parent = parent
        self.g = 0
        self.h = 0
        self.f = 0

    def __lt__(self, other):
        return self.f < other.f

def heuristic(current_pos, goal):
    return abs(current_pos[0] - goal[0]) + abs(current_pos[1] - goal[1])

def best_first_search(maze, start, goal):
    rows, cols = len(maze), len(maze[0])
    start_node = Node(start)
    frontier = PriorityQueue()
    frontier.put(start_node)
    visited = set()
    while not frontier.empty():
        current_node = frontier.get()
        current_pos = current_node.position

        if current_pos == goal:
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]
        visited.add(current_pos)

        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_pos = (current_pos[0] + dx, current_pos[1] + dy)

            if 0 <= new_pos[0] < rows and 0 <= new_pos[1] < cols and maze[new_pos[0]][new_pos[1]] == 0 and new_pos not in visited:
                new_node = Node(new_pos, current_node)
                new_node.g = current_node.g + 1
                new_node.h = heuristic(new_pos, goal)
                new_node.f = new_node.h
                frontier.put(new_node)
                visited.add(new_pos)

    return None

def find_paths_for_all_goals(maze, start, goals):
    paths = {}
    current_start = start

    for goal in goals:
        path = best_first_search(maze, current_start, goal)
        if path:
            paths[goal] = path
            current_start = goal
        else:
            paths[goal] = None

    return paths

maze = [
    [0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 0, 1, 0]
]

start = (0, 0)
goals = [(4, 4),(1, 4),(2,2)]

paths = find_paths_for_all_goals(maze, start, goals)
for goal, path in paths.items():
    if path:
        print(f"Path to goal {goal}: {path}")
    else:
        print(f"No path found to goal {goal}")
