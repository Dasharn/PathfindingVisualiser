import pygame


#process of refactoring
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

    def evaluate_neighbors(self, grid):
        # Define the four possible directions: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

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