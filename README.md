# Path-Finding Algorithm Visualizer

This is a path-finding algorithm visualizer implemented in Python using the Pygame library. It allows you to visualize four different path-finding algorithms: A*, Dijkstra's algorithm, Breadth-First Search (BFS), and Greedy algorithm.

## Getting Started

1. Install Python if you haven't already. You can download Python from the official website: [Python Downloads](https://www.python.org/downloads/)

2. Install Pygame library by running the following command:


3. Clone or download the repository.

4. Run the `main.py` file to start the application.

## Instructions

- Use the mouse to interact with the grid:
- Left-click to place the start node, end node, and barriers.
- Right-click to remove a node or barrier.
- Use the keyboard to select and run the algorithms:
- Press 'a' to run A* algorithm.
- Press 'd' to run Dijkstra's algorithm.
- Press 'b' to run Breadth-First Search (BFS).
- Press 'g' to run Greedy algorithm.
- Press 'r' to reset the grid.

## Algorithms

- A* Algorithm: Finds the shortest path by considering both the distance from the start node and the heuristic (estimated) distance to the goal.
- Dijkstra's Algorithm: Finds the shortest path by considering only the distance from the start node.
- BFS (Breadth-First Search): Finds the shortest path by exploring nodes in breadth-first order.
- Greedy Algorithm: Finds the path by always choosing the neighbor node that appears to be closest to the goal.

## License

This project is licensed under the [MIT License](LICENSE).

