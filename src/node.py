import pygame


class Node:
    
    def __init__(self, row, col, width, total_rows):
        self.states =  {
    "default":  "#FFFFFF",
    "start": "#D0E7FF",
    "end": "#1A34B8",
    "barrier": "#000000",
    "visited": "#87BFFF",
    "explore": "#3366FF",
    "shortest_path": "#8A2BE2",
    "lines": "#07080C"}

        self.row = row
        self.col = col
        # To get coordinate location of node. Grid coordinates (x, y) start at the top left.
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.color = self.states["default"]  # Default colour (of grid)
        self.neighbours = []

    # Methods to return state of node (True/False)
    def get_position(self):
        return self.row, self.col

    def check_start(self):
        return self.color == self.states["start"]

    def check_end(self):
        return self.color == self.states["end"]

    def can_explore(self):
        return self.color == self.states["explore"]

    def visited(self):
        return self.color == self.states["visited"]

    def is_barrier(self):
        return self.color == self.states["barrier"]

    # Assigning colours
    def reset(self):
        self.color = self.states["default"]

    def start_node(self):
        self.color = self.states["start"]

        print("start node color set")

    def end_node(self):
        self.color = self.states["end"]

    def to_explore(self):  # Node opened to signify that its neighbours are next to be evaluated
        self.color = self.states["explore"]
        print("to explore")

    def visited(self):  # Node already visited and explored
        self.color = self.states["visited"]
        print("alread visited")

    def make_barrier(self):
        self.color = self.states["barrier"]

    def shortest_path(self):
        self.color = self.states["shortest_path"]

    def draw(self, win):  # Height and width are equal for every node - difference is the position in x and y
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

    def check_neighbours(self, grid):
        print("checking neighbours")
        # Define the four possible directions: Down, Up, Right, Left
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        # Clear the neighbors list
        self.neighbours = []

        # Iterate over each direction
        for dr, dc in directions:
            # Calculate the new row and column values
            new_row = self.row + dr
            new_col = self.col + dc

            # Check if the new position is within the grid boundaries
            if 0 <= new_row < self.total_rows and 0 <= new_col < self.total_rows:
                # Retrieve the neighbor node from the grid
                neighbour_node = grid[new_row][new_col]

                # Check if the neighbor node is a barrier
                if not neighbour_node.is_barrier():
                    # Append the neighbor node to the neighbors list
                    self.neighbours.append(neighbour_node)