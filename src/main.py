import pygame
from collections import deque
from node import *
from algorithm import Algorithm 
from settings import Settings
from gui import Gui

class Visualiser:
    # Initializer for the Visualiser class
    def __init__(self):
        # Initialize the Algorithm, Settings, and Gui objects
        self.algo = Algorithm()
        self.settings = Settings()
        # Get the screen width and number of rows from the settings
        self.width = self.settings.get_screen_width()
        self.rows = self.settings.get_rows()
        # Get the states from the settings
        self.states = self.settings.get_states()

        # Create the pygame screen with the given width and height
        self.screen = pygame.display.set_mode((self.width, self.width))
        # Set the caption for the pygame window
        pygame.display.set_caption("Path Finder A*: Press 'a' BFS: Press 'b'  Dijkstra's: Press 'd'  Greedy: Press 'g'   Reset grid: Press 'r'")
        # Initialize the Gui object with the rows, width, screen, and states
        self.gui = Gui(self.rows, self.width, self.screen, self.states)
        # Initialize the start and end nodes as None
        self.start = None
        self.end = None
        # Set running to True
        self.running = True
        # Create the grid
        self.grid = self.gui.make_grid()

    # The main loop for the visualiser
    def play(self):
        # Keep running until running is set to False
        while self.running:
            # Draw the grid on each iteration
            self.gui.draw_grid()

            # Handle all the events
            for event in pygame.event.get():
                # If the event is QUIT, set running to False
                if event.type == pygame.QUIT:
                    self.running = False
                # Handle the key events
                

                self.handle_key_event(event)
                #
                self.handle_mouse_event(event)

        # Quit pygame when the loop is done
        pygame.quit()

    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if self.start and self.end:
                self.update_neighbours()
                self.run_algorithm(event.key)
            elif event.key == pygame.K_r:
                self.reset_and_recreate_grid()

    def update_neighbours(self):
        for row in self.grid:
            for node in row:
                node.check_neighbours(self.grid)

    def run_algorithm(self, key):
        algorithms = {
            pygame.K_a: self.algo.A_Star,
            pygame.K_d: self.algo.dijkstras,
            pygame.K_b: self.algo.bfs,
            pygame.K_g: self.algo.greedy,
            pygame.K_s: self.algo.bidirectional_search,
            pygame.K_f: self.algo.dead_end_filling
        }

        algorithm = algorithms.get(key)
        if algorithm:
            algorithm(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)

    def reset_and_recreate_grid(self):
        self.start = None
        self.end = None
        self.grid = self.gui.make_grid()

    

    def handle_mouse_event(self, event):
        left_button_pressed = pygame.mouse.get_pressed()[0]
        right_button_pressed = pygame.mouse.get_pressed()[2]

        position = pygame.mouse.get_pos()
        row, col = self.gui.get_clicked_position(position)
        node = self.grid[row][col]

        if left_button_pressed:
            self.handle_left_button(node)
        elif right_button_pressed:
            self.handle_right_button(node)

    def handle_left_button(self, node):
        if not self.start and node != self.end:
            self.set_start_node(node)
        elif not self.end and node != self.start:
            self.set_end_node(node)
        elif node != self.end and node != self.start:
            node.make_barrier()

    def handle_right_button(self, node):
        node.reset()
        if node == self.start:
            self.start = None
        elif node == self.end:
            self.end = None

    def set_start_node(self, node):
        self.start = node
        print("Start Set")
        self.start.start()

    def set_end_node(self, node):
        self.end = node
        print("End Set")
        self.end.end()



       

if __name__ == "__main__":
    visualiser = Visualiser()
    visualiser.play()
        
