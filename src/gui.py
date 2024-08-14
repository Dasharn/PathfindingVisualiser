import pygame
from node import Node
import random

class Gui:

    def __init__(self, rows, width, screen, state):
        self.screen = screen
        self.screen_width = width
        self.rows = rows
        self.grid = self.make_grid()
        self.states = state

    

    def make_grid(self):
        node_width = self.screen_width // self.rows

        grid = [[Node(i, j, node_width, self.rows) for j in range(self.rows)] for i in range(self.rows)]

        return grid
    

    # Rest of the class code...

    """def generate_maze(self):
        grid = self.grid

        # Reset all nodes to be barriers
        for row in grid:
            for node in row:
                node.make_barrier()

        node_width = self.screen_width // self.rows

        # Select a random starting node
        start_node = grid[random.randint(0, self.rows-1)][random.randint(0, self.rows-1)]
        start_node.reset()

        # Add the starting node to the active set
        active_set = [start_node]

        while active_set:
            current_node = active_set.pop(random.randint(0, len(active_set)-1))

            # Check the neighbors of the current node
            neighbors = current_node.neighbours
            valid_neighbors = []

            for neighbor in neighbors:
                x, y = neighbor
                if 0 <= x < self.rows and 0 <= y < self.rows and grid[x][y].is_barrier():
                    valid_neighbors.append((x, y))

            if valid_neighbors:
                x, y = random.choice(valid_neighbors)
                next_node = grid[x][y]

                # Make the next node a passage
                next_node.reset()

                # Add the next node to the active set
                active_set.append(next_node)

                # Connect the current node and the next node
                if x > current_node.row:
                    grid[current_node.row + 1][current_node.col].reset()
                elif x < current_node.row:
                    grid[current_node.row - 1][current_node.col].reset()
                elif y > current_node.col:
                    grid[current_node.row][current_node.col + 1].reset()
                elif y < current_node.col:
                    grid[current_node.row][current_node.col - 1].reset()

        self.draw_grid()
"""


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
