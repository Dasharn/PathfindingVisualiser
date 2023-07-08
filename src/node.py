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
        self.distance = 0
        
        self.four_directions =  [(1, 0), (-1, 0), (0, 1), (0, -1)]
        self.eight_directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.directions = self.four_directions
        #d* light algorithm attributes

        self.cost = 0
        self.rhs = 0
        self.parent = None

    # Methods to return state of node (True/False)

    def get_position(self):
        return self.row, self.col
    
    def get_directions(self):
        return self.directions
    
    def set_directions(self, directions):
        if directions == 8:
            self.directions =  self.eight_directions
        elif directions == 4:
            self.directions = self.four_directions
    
    def set_color(self, color):
        self.color = color
        
    def get_color(self, color):
        return self.color

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
        self.set_color(self.states["default"])
        #self.color = self.states["default"]

    def start(self):
        self.set_color(self.states["start"])
        #self.color = self.states["start"]


    def end(self):
        self.set_color(self.states["end"])
        #self.color = self.states["end"]

    def to_explore(self):  # Node opened to signify that its neighbours are next to be evaluated
        self.set_color(self.states["explore"])
        #self.color = self.states["explore"]
        

    def visited(self):  # Node already visited and explored
        self.set_color(self.states["visited"])
        #self.color = self.states["visited"]
        

    def make_barrier(self):
        self.set_color(self.states["barrier"])
        #self.color = self.states["barrier"]

    def shortest_path(self):
        self.set_color(self.states["shortest_path"])
        #self.color = self.states["shortest_path"]

    def draw(self, screen):  # Height and width are equal for every node - difference is the position in x and y
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    def check_neighbours(self, grid):
        
        # Define the four possible directions: Down, Up, Right, Left
        

        # Clear the neighbors list
        self.neighbours = []

        # Iterate over each direction
        for dr, dc in self.get_directions():
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
    

    
    
