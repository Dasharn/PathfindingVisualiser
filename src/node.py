import pygame

class Node:
    DIRECTIONS_FOUR = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    DIRECTIONS_EIGHT = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
    
    STATES = {
        "default":  "#FFFFFF",
        "start": "#D0E7FF", 
        "end": "#1A34B8",
        "barrier": "#000000",
        "visited": "#87BFFF",
        "explore": "#3366FF",
        "shortest_path": "#8A2BE2",
        "lines": "#07080C"
    }

    def __init__(self, row, col, width, total_rows):
        self.row = row
        self.col = col
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.color = self.STATES["default"]  # Initial node color
        self.neighbours = []
        self.directions = self.DIRECTIONS_FOUR

    def get_position(self):
        return self.row, self.col
    
    def get_directions(self):
        return self.directions
    
    def set_directions(self, directions):
        if directions == 8:
            self.directions = self.DIRECTIONS_EIGHT
        elif directions == 4:
            self.directions = self.DIRECTIONS_FOUR

    def set_color(self, color):
        self.color = color
        
    def get_color(self):
        return self.color

    # Node state checks
    def check_start(self):
        return self.color == self.STATES["start"]

    def check_end(self):
        return self.color == self.STATES["end"]

    def can_explore(self):
        return self.color == self.STATES["explore"]

    def is_barrier(self):
        return self.color == self.STATES["barrier"]

    # Node state setters
    def reset(self):
        self.set_color(self.STATES["default"])

    def start(self):
        self.set_color(self.STATES["start"])

    def end(self):
        self.set_color(self.STATES["end"])

    def to_explore(self):
        self.set_color(self.STATES["explore"])

    def visited(self):
        self.set_color(self.STATES["visited"])

    def make_barrier(self):
        self.set_color(self.STATES["barrier"])

    def shortest_path(self):
        self.set_color(self.STATES["shortest_path"])

    # Drawing the node
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.width))

    # Update the node's neighbors
    def check_neighbours(self, grid):
        self.neighbours = []
        for dr, dc in self.get_directions():
            new_row, new_col = self.row + dr, self.col + dc
            if 0 <= new_row < self.total_rows and 0 <= new_col < self.total_rows:
                neighbor_node = grid[new_row][new_col]
                if not neighbor_node.is_barrier():
                    self.neighbours.append(neighbor_node)

    

    
    
