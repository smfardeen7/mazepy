# Maze Search Visualisation

![Source-derived architecture for Maze Search Visualisation](docs/images/project-overview.png)

**Implementation overview:** A Python coursework exercise in graph traversal. [Source map and scope](docs/PORTFOLIO.md).

The current score uses Euclidean displacement as g, not cumulative path cost. Standard A* shortest-path optimality is not established.

## Overview

This CS 580 coursework project uses a priority-queue search to find a route through a maze. It uses the `pyamaze` library to generate the maze and visualize the pathfinding process.

The agent starts at the bottom-right corner and aims to reach the goal at the top-left corner. The algorithm uses:

*   **g(n):** Euclidean distance from the start node to the current node `n`.
*   **h(n):** Manhattan distance from the current node `n` to the goal node.
*   **f(n):** `g(n) + h(n)` - the total estimated cost.

## Prerequisites

*   Python 3.x
*   `pyamaze` library

## Installation

1.  Clone the repository:
    ```bash
    git clone https://github.com/smfardeen7/mazepy.git
    cd mazepy
    ```

2.  Install the required dependency:
    ```bash
    pip install pyamaze
    ```
    *If the installation fails or `pyamaze` is not found, you may need to copy the `pyamaze.py` file into the same directory as the script.*

## Usage

Run the main script:

```bash
python h1_mshaik20.py
```

This will:
1.  Generate a 10x10 maze.
2.  Calculate a route using the current priority-queue search.
3.  Open a window showing the maze and the agent traversing the path.
4.  Display the path length.

## Author

mshaik20@gmu.edu
