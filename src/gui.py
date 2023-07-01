import pygame
from node import Node

class Gui:

    def __init__(self, rows, width, screen, state):
        self.screen = screen
        self.screen_width = width
        self.rows = rows
        self.grid = self.make_grid()
        self.states = state

    def make_grid(self):
        node_width = self.screen_width // self.rows

        # Use list comprehension to create the grid
        grid = [[Node(i, j, node_width, self.rows) for j in range(self.rows)] for i in range(self.rows)]

        self.grid = grid

        return grid

    def draw_grid_lines(self):
        node_width = self.screen_width // self.rows

        # Draw horizontal lines along rows
        for i in range(self.rows):
            y = i * node_width
            pygame.draw.line(self.screen, self.states["lines"], (0, y), (self.screen_width, y))

        # Draw vertical lines along columns
        for j in range(self.rows):
            x = j * node_width
            pygame.draw.line(self.screen, self.states["lines"], (x, 0), (x, self.screen_width))

    def draw_grid(self):
        grid = self.grid
        self.screen.fill(self.states["default"])

        for row in grid:
            for node in row:
                node.draw(self.screen)  # Uses node instances to draw nodes

        self.draw_grid_lines()  # After screendow is filled, grid lines drawn
        pygame.display.update()

    def get_clicked_position(self,position):
        node_width = self.screen_width // self.rows
        row, col = position[0] // node_width, position[1] // node_width
        return row, col