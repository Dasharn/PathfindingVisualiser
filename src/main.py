import pygame
from collections import deque
from node import *
from algorithm import Algorithm 
from settings import Settings
from gui import Gui

class Visualiser:
    
    def __init__(self):
        self.algo = Algorithm()
        self.settings = Settings()
        self.width = self.settings.get_screen_width()
        self.rows = self.settings.get_rows()
        self.states = self.settings.get_states()

    # Create the tkinter screen
        self.screen = pygame.display.set_mode((self.width, self.width))
        pygame.display.set_caption("Path Finder A*: Press 'a'  Dijkstra's: Press 'd'  Greedy: Press 'g' BFS: Press 'b'  Reset grid: Press 'r'")
        self.gui = Gui(self.rows, self.width, self.screen, self.states)
        self.start = None
        self.end = None
        self.running = True
        self.grid = self.gui.make_grid()

        
    def play(self):
        while self.running:
            self.gui.draw_grid()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_a and self.start and self.end:
                        for row in self.grid:
                            for node in row:
                                node.check_neighbours(self.grid)
                        self.algo.A_Star(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)

                    elif event.key == pygame.K_d and self.start and self.end:
                        for row in self.grid:
                            for node in row:
                                node.check_neighbours(self.grid)
                        self.algo.dijkstras(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                    
                    elif event.key == pygame.K_b and self.start and self.end:
                        for row in self.grid:
                            for node in row:
                                node.check_neighbours(self.grid)
                        self.algo.BFS(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                    
                    elif event.key == pygame.K_g and self.start and self.end:
                        for row in self.grid:
                            for node in row:
                                node.check_neighbours(self.grid)
                        self.algo.greedy(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                
                    elif event.key == pygame.K_s and self.start and self.end:
                        for row in self.grid:
                            for node in row:
                                node.check_neighbours(self.grid)
                        self.algo.bidirectional_search(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)

                    elif event.key == pygame.K_r:
                        self.start = None
                        self.end = None
                        self.grid = self.gui.make_grid()

                if pygame.mouse.get_pressed()[0]:
                    position = pygame.mouse.get_pos()
                    row, col = self.gui.get_clicked_position(position)
                    node = self.grid[row][col]

                    if not self.start and node != self.end:
                        self.start = node
                        print("start_node called")
                        self.start.start_node()
                        
                    elif not self.end and node != self.start:
                        self.end = node
                        print("end node called")
                        self.end.end_node()
                    elif node != self.end and node != self.start:
                        node.make_barrier()

                elif pygame.mouse.get_pressed()[2]:
                    position = pygame.mouse.get_pos()
                    row, col = self.gui.get_clicked_position(position)
                    node = self.grid[row][col]
                    node.reset()
                    if node == self.start:
                        self.start = None
                    elif node == self.end:
                        self.end = None

        pygame.quit()

if __name__ == "__main__":
    visualiser = Visualiser()
    visualiser.play()
        