import time
from queue import PriorityQueue
import heapq
import pygame
from collections import deque
from node import Node

width = 500

# Create the tkinter window
window = pygame.display.set_mode((width, width))
pygame.display.set_caption("Path-Finding Algorithm Visualiser   A*: Press 'a'  Dijkstra's: Press 'd'  Greedy: Press 'g' BFS: Press 'b'   Reset grid: Press 'r'")


# Colors
colors = {
    "white": "#FFFFFF",
    "orange": "#FFA500",
    "grey": "#A9A9A9",
    "black": "#000000",
    "blue": "#6495ED",
    "green": "#00FF00",
    "yellow": "#FFFF00"
}

# Node states
states = {
    "default":  "#FFFFFF",
    "start": "#FFA500",
    "end": "#A9A9A9",
    "barrier": "#000000",
    "visited": "#6495ED",
    "explore": "#00FF00",
    "shortest_path":  "#EE82EE"
}

class Node:
    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        # To get coordinate location of node. Grid coordinates (x, y) start at the top left.
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.color = states["default"]  # Default colour (of grid)
        self.neighbors = []

    # Methods to return state of node (True/False)
    def get_position(self):
        return self.row, self.col

    def check_start(self):
        return self.color == states["start"]

    def check_end(self):
        return self.color == states["end"]

    def can_explore(self):
        return self.color == states["explore"]

    def visited(self):
        return self.color == states["visited"]

    def is_barrier(self):
        return self.color == states["barrier"]

    # Assigning colours
    def reset(self):
        self.color = states["default"]

    def start_node(self):
        self.color = states["start"]

    def end_node(self):
        self.color = states["end"]

    def to_explore(self):  # Node opened to signify that its neighbours are next to be evaluated
        self.color = states["explore"]

    def already_visited(self):  # Node already visited and explored
        self.color = states["visited"]

    def make_barrier(self):
        self.color = states["barrier"]

    def shortest_path(self):
        self.color = states["shortest_path"]

    def draw(self, win):  # Height and width are equal for every node - difference is the position in x and y
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def check_neighbors(self, grid): 
        # Define the four possible directions: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        # Define the 8 possible directions
         # directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]

        # Clear the neighbors list
        self.neighbors = []

        # Iterate over each direction
        for dr, dc in directions:
            # Calculate the new row and column values
            new_row = self.row + dr
            new_col = self.col + dc

            # Check if the new position is within the grid boundaries
            if 0 <= new_row < self.total_rows and 0 <= new_col < self.total_rows:
                # Retrieve the neighbor node from the grid
                neighbor_node = grid[new_row][new_col]

                # Check if the neighbor node is a barrier
                if not neighbor_node.is_barrier():
                    # Append the neighbor node to the neighbors list
                    self.neighbors.append(neighbor_node)
    




def heuristic(present, target):
    # Unpack the coordinates of the present and target nodes
    (x1, y1), (x2, y2) = present, target

    # Calculate the distance in each dimension
    x_distance = abs(x1 - x2)
    y_distance = abs(y1 - y2)

    # Return the sum of the distances as the heuristic value
    return x_distance + y_distance

def find_shortest_path(before, present, draw):
    # Traverse the path from the end node to the start node
    while present in before:
        present = before[present]  # Update the present node to its predecessor
        present.shortest_path()  # Color the present node as YELLOW
        draw()  # Redraw the grid with the updated colors


def dijkstras(draw, grid, start, end):
    count = 0  # If 2 nodes mid-path give the same distance, node with lower count can be given priority

    # Priority queue to store nodes with their respective distances
    queue_set = []
    heapq.heappush(queue_set, (0, count, start))

    # Store the distances from the start node to each node in the grid
    distances = {node: float("inf") for row in grid for node in row}
    distances[start] = 0

    # Store the previous node in the shortest path
    prior = {}

    # Set to keep track of visited nodes
    visited = set()
    start_time = time.time()

    while queue_set:
        # Get the node with the minimum distance from the priority queue
        present = heapq.heappop(queue_set)[2]
        visited.add(present)

        if present == end:  # If end node reached
            find_shortest_path(prior, end, draw)
            end.end_node()
            start.start_node()
            return True

        for neighbor in present.neighbors:
            new_distance = distances[present] + 1  # Distance from start to neighbor is always 1

            if new_distance < distances[neighbor]:  # If a shorter path is found
                prior[neighbor] = present
                distances[neighbor] = new_distance
                if neighbor not in visited:
                    count += 1
                    heapq.heappush(queue_set, (distances[neighbor], count, neighbor))
                    neighbor.to_explore()

        draw()

        if present != start:
            present.already_visited()
    end_time = time.time()
    execution_time = end_time - start_time

    return False



def BFS(draw, grid, start, end):
    queue = deque([start])
    visited = set()
    visited.add(start)
    prior = {}  # Store the parent nodes
    
    start_time = time.time()
    while queue:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        node = queue.popleft()

        if node == end:
            find_shortest_path(prior, end, draw)
            end.end_node()
            start.start_node()
            return True

        for neighbor in node.neighbors:
            if neighbor not in visited:
                prior[neighbor] = node
                queue.append(neighbor)
                visited.add(neighbor)
                neighbor.to_explore()

        draw()

        if node != start:
            node.already_visited()
    
    end_time = time.time()
    execution_time = end_time - start_time

    return False


def A_Star(draw, grid, start, end):
    count = 0  # If 2 nodes mid-path give the same distance, node with lower count can be traversed.

    queue_set = []
    heapq.heappush(queue_set, (0, count, start))

    edge_total = {spot: float("inf") for row in grid for spot in row}
    edge_total[start] = 0

    total_distance = {spot: float("inf") for row in grid for spot in row}
    total_distance[start] = heuristic(start.get_position(), end.get_position())

    prior = {}
    in_queue = {start}

    start_time = time.time()

    while queue_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        present = heapq.heappop(queue_set)[2]
        in_queue.remove(present)

        if present == end:
            find_shortest_path(prior, end, draw)
            end.end_node()
            start.start_node()
            return True

        for neighbor in present.neighbors:
            new_edge_total = edge_total[present] + 1

            if new_edge_total < edge_total[neighbor]:
                prior[neighbor] = present
                edge_total[neighbor] = new_edge_total
                total_distance[neighbor] = new_edge_total + heuristic(neighbor.get_position(), end.get_position())
                if neighbor not in in_queue:
                    count += 1
                    heapq.heappush(queue_set, (total_distance[neighbor], count, neighbor))
                    in_queue.add(neighbor)
                    neighbor.to_explore()

        draw()

        if present != start:
            present.already_visited()
    
    end_time = time.time()
    execution_time = end_time - start_time

    return False
def greedy(draw, grid, start, end):
    open_set = [start]
    visited = set()
    visited.add(start)
    prior = {}  # Store the parent nodes

    start_time = time.time()
    while open_set:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        current = open_set.pop()
        
        if current == end:
            find_shortest_path(prior, end, draw)
            end.end_node()
            start.start_node()
            return True

        for neighbor in current.neighbors:
            if neighbor not in visited:
                prior[neighbor] = current
                open_set.append(neighbor)
                visited.add(neighbor)
                neighbor.to_explore()

        draw()

        if current != start:
            current.already_visited()
    
    end_time = time.time()
    execution_time = end_time - start_time

    return False


def make_grid(rows, win_width):
    node_width = win_width // rows

    # Use list comprehension to create the grid
    grid = [[Node(i, j, node_width, rows) for j in range(rows)] for i in range(rows)]

    return grid

def draw_grid_lines(win, rows, win_width):
    node_width = win_width // rows

    # Draw horizontal lines along rows
    for i in range(rows):
        y = i * node_width
        pygame.draw.line(win, states["end"], (0, y), (win_width, y))

    # Draw vertical lines along columns
    for j in range(rows):
        x = j * node_width
        pygame.draw.line(win, states["end"], (x, 0), (x, win_width))

def draw_grid(window, grid, rows, window_width):
    window.fill(states["default"])

    for row in grid:
        for node in row:
            node.draw(window)  # Uses node instances to draw nodes

    draw_grid_lines(window, rows, window_width)  # After window is filled, grid lines drawn
    pygame.display.update()

def get_clicked_position(position, rows, win_width):
    node_width = win_width // rows
    row, col = position[0] // node_width, position[1] // node_width
    return row, col

def main(win, win_width):
    rows = 50
    grid = make_grid(rows, win_width)
    start = None
    end = None

    running = True
    while running:
        draw_grid(win, grid, rows, win_width)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a and start and end:
                    for row in grid:
                        for node in row:
                            node.check_neighbors(grid)
                    A_Star(lambda: draw_grid(win, grid, rows, win_width), grid, start, end)

                elif event.key == pygame.K_d and start and end:
                    for row in grid:
                        for node in row:
                            node.check_neighbors(grid)
                    dijkstras(lambda: draw_grid(win, grid, rows, win_width), grid, start, end)
                
                elif event.key == pygame.K_b and start and end:
                    for row in grid:
                        for node in row:
                            node.check_neighbors(grid)
                    BFS(lambda: draw_grid(win, grid, rows, win_width), grid, start, end)
                
                elif event.key == pygame.K_g and start and end:
                    for row in grid:
                        for node in row:
                            node.check_neighbors(grid)
                    greedy(lambda: draw_grid(win, grid, rows, win_width), grid, start, end)

                elif event.key == pygame.K_r:
                    start = None
                    end = None
                    grid = make_grid(rows, win_width)

            if pygame.mouse.get_pressed()[0]:
                position = pygame.mouse.get_pos()
                row, col = get_clicked_position(position, rows, win_width)
                node = grid[row][col]

                if not start and node != end:
                    start = node
                    start.start_node()
                elif not end and node != start:
                    end = node
                    end.end_node()
                elif node != end and node != start:
                    node.make_barrier()

            elif pygame.mouse.get_pressed()[2]:
                position = pygame.mouse.get_pos()
                row, col = get_clicked_position(position, rows, win_width)
                node = grid[row][col]
                node.reset()
                if node == start:
                    start = None
                elif node == end:
                    end = None

    pygame.quit()


main(window, width)