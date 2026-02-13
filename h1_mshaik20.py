"""
CS 580 - H1: A* Search for Maze Solving
======================================
Implements A* pathfinding algorithm to solve a maze using pyamaze.
- g(n): Euclidean distance from start node to current node n
- h(n): Manhattan distance from current node n to goal node
- f(n): g(n) + h(n) - total estimated cost

Start: bottom-right corner | Goal: top-left corner

Author: mshaik20@gmu.edu

Setup: pip install pyamaze
If installation fails, copy pyamaze.py to the same folder as this file.
"""

import math
from queue import PriorityQueue
from pyamaze import maze, agent, textLabel


def euclidean_distance(cell1: tuple, cell2: tuple) -> float:
    """
    Calculate g(n): Euclidean distance between two cells.
    Used as the actual cost from start to current node.
    Formula: sqrt((x1-x2)² + (y1-y2)²)
    
    Args:
        cell1: (row, col) of first cell
        cell2: (row, col) of second cell
    
    Returns:
        Euclidean distance as a float
    """
    r1, c1 = cell1
    r2, c2 = cell2
    return math.sqrt((r1 - r2) ** 2 + (c1 - c2) ** 2)


def manhattan_distance(cell1: tuple, cell2: tuple) -> float:
    """
    Calculate h(n): Manhattan distance between two cells.
    Used as the heuristic estimate from current node to goal.
    Formula: |x1-x2| + |y1-y2|
    
    Args:
        cell1: (row, col) of current cell
        cell2: (row, col) of goal cell
    
    Returns:
        Manhattan distance as a float
    """
    r1, c1 = cell1
    r2, c2 = cell2
    return abs(r1 - r2) + abs(c1 - c2)


def get_neighbors(maze_map: dict, cell: tuple) -> list:
    """
    Get all walkable neighbor cells from the current cell.
    Uses maze_map to check which walls are open (value 1 = can move).
    
    Args:
        maze_map: Dictionary mapping cells to their wall info {'N','S','E','W': 0|1}
        cell: (row, col) of current cell
    
    Returns:
        List of (row, col) tuples for accessible neighbors
    """
    row, col = cell
    neighbors = []
    walls = maze_map[cell]
    
    # North: row-1 (wall open means we can move to the cell above)
    if walls['N'] == 1:
        neighbors.append((row - 1, col))
    # South: row+1
    if walls['S'] == 1:
        neighbors.append((row + 1, col))
    # East: col+1
    if walls['E'] == 1:
        neighbors.append((row, col + 1))
    # West: col-1
    if walls['W'] == 1:
        neighbors.append((row, col - 1))
    
    return neighbors


def astar(maze_obj) -> dict:
    """
    A* search algorithm to find optimal path from start to goal.
    
    Uses priority queue ordered by f(n) = g(n) + h(n).
    Tiebreaker: when f(n) values are equal, we use an incrementing counter
    to prefer nodes that were added earlier (FIFO order).
    
    Args:
        maze_obj: The pyamaze maze object with maze_map attribute
    
    Returns:
        Dictionary mapping each cell to the next cell in the path (for tracePath),
        or empty dict if no path exists
    """
    # Define start (bottom-right) and goal (top-left) per assignment
    start = (maze_obj.rows, maze_obj.cols)
    goal = (1, 1)
    
    # Priority queue: (f(n), tiebreaker, node)
    # Tiebreaker ensures consistent ordering when f-values are equal
    open_set = PriorityQueue()
    tiebreaker = 0
    open_set.put((0, tiebreaker, start))
    tiebreaker += 1
    
    # Track where we came from to reconstruct the path
    parent = {start: None}
    # Track visited nodes to avoid revisiting
    visited = set()
    
    while not open_set.empty():
        # Get node with minimum f(n)
        _, _, current = open_set.get()
        
        # Skip if already expanded
        if current in visited:
            continue
        visited.add(current)
        
        # Goal reached - reconstruct and return path
        if current == goal:
            # Build path as dict: cell -> next_cell (format for tracePath)
            path = {}
            node = goal
            while parent[node] is not None:
                path[parent[node]] = node
                node = parent[node]
            return path
        
        # Expand neighbors
        for neighbor in get_neighbors(maze_obj.maze_map, current):
            if neighbor in visited:
                continue
            
            # g(n): Euclidean distance from start to neighbor
            g = euclidean_distance(start, neighbor)
            # h(n): Manhattan distance from neighbor to goal
            h = manhattan_distance(neighbor, goal)
            # f(n) = g(n) + h(n)
            f = g + h
            
            # Add to open set with tiebreaker for consistent ordering
            open_set.put((f, tiebreaker, neighbor))
            tiebreaker += 1
            
            # Update parent if this is first time we see this node
            if neighbor not in parent:
                parent[neighbor] = current
    
    # No path found
    return {}


def main():
    """
    Create maze, run A* search, and visualize the solution.
    """
    # Maze dimensions (rows and cols must be variables per assignment)
    # Valid range: [2, 100] - using 10x10 for testing
    rows = 10
    cols = 10
    
    # Create and generate the maze
    m = maze(rows, cols)
    m.CreateMaze()
    
    # Run A* to find the path
    path = astar(m)
    
    # Create agent and trace the path
    a = agent(m, footprints=True)
    m.tracePath({a: path})
    
    # Display path length (number of steps + 1 for the goal cell)
    path_length = len(path) + 1
    textLabel(m, 'Path Length', path_length)
    
    m.run()


if __name__ == '__main__':
    main()
