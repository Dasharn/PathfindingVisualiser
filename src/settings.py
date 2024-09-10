class Settings:
    DEFAULT_STATES = {
        "default":  "#FFFFFF",
        "start": "#D0E7FF",
        "end": "#1A34B8",
        "barrier": "#000000",
        "visited": "#87BFFF",
        "explore": "#3366FF",
        "shortest_path": "#8A2BE2",
        "lines": "#07080C"
    }

    def __init__(self, screen_width=750, rows=50):
        self.screen_width = screen_width
        self.rows = rows
        self.STATES = self.DEFAULT_STATES.copy()  # Ensure we don't modify the class-level dict

    def get_state_color(self, state):
        return self.STATES.get(state, "#FFFFFF")  # Return default color if state not found
    
    def set_state_color(self, state, color):
        self.STATES[state] = color  # Set the color for a given state
    
    def get_states(self):
        return self.STATES

    def get_rows(self):
        return self.rows
    
    def set_rows(self, rows):
        self.rows = rows
    
    def get_screen_width(self):
        return self.screen_width
    
    def set_screen_width(self, width):
        self.screen_width = width

                
