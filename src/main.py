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
        pygame.display.set_caption("Path Finder A*: Press 'a' BFS: Press 'b'  Dijkstra's: Press 'd'  Greedy: Press 'g'   Reset grid: Press 'r'")
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
                self.handle_key_event(event)
                self.handle_mouse_event(event)

        
        pygame.quit()

    def handle_key_event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a or event.key == pygame.K_d or event.key == pygame.K_b or event.key == pygame.K_g or event.key == pygame.K_s or event.key == pygame.K_f:
                if self.start and self.end:
                    for row in self.grid:
                        for node in row:
                            node.check_neighbours(self.grid)

                    if event.key == pygame.K_a:
                        self.algo.A_Star(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                    elif event.key == pygame.K_d:
                        self.algo.dijkstras(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                    elif event.key == pygame.K_b:
                        self.algo.bfs(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                    elif event.key == pygame.K_g:
                        self.algo.greedy(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                    elif event.key == pygame.K_s:
                        self.algo.bidirectional_search(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                    elif event.key == pygame.K_f:
                        print("press f")
                        self.algo.dead_end_filling(lambda: self.gui.draw_grid(), self.grid, self.start, self.end)
                   
            elif event.key == pygame.K_r:
                self.start = None
                self.end = None
                self.grid = self.gui.make_grid()

    def handle_mouse_event(self, event):
        if pygame.mouse.get_pressed()[0]:
            position = pygame.mouse.get_pos()
            row, col = self.gui.get_clicked_position(position)
            node = self.grid[row][col]

            if not self.start and node != self.end:
                self.start = node
                print("start_node called")
                self.start.start()
            elif not self.end and node != self.start:
                self.end = node
                print("end node called")
                self.end.end()
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

        
              


       

if __name__ == "__main__":
    visualiser = Visualiser()
    visualiser.play()
        