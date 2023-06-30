from PathfindingVisualiser.settings import Settings

class Node:
    def __init__(self, row, col, width, total_rows, states):
        self.row = row
        self.col = col
        # To get coordinate location of node. Grid coordinates (x, y) start at the top left.
        self.x = row * width
        self.y = col * width
        self.width = width
        self.total_rows = total_rows
        self.states = states
        self.color = self.states["default"]  # Default colour (of grid)
        self.neighbors = []

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

    def end_node(self):
        self.color = self.states["end"]

    def to_explore(self):  # Node opened to signify that its neighbours are next to be evaluated
        self.color = self.states["explore"]

    def already_visited(self):  # Node already visited and explored
        self.color = self.states["visited"]

    def make_barrier(self):
        self.color = self.states["barrier"]

    def shortest_path(self):
        self.color = self.states["shortest_path"]

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