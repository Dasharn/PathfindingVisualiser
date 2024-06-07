class Settings:
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

    def __init__(self, screen_width=750, rows=50):
        self.STATES = self.STATES
        self.screen_width = screen_width
        self.rows = rows
        
    def get_state_color(self, state):
        return self.STATES[state]
    
    def set_state_color(self, state):
        self.STATES[state] = state
    
    def get_STATES(self):
        return self.STATES

    def get_rows(self):
        return self.rows
    
    def set_rows(self, rows):
        self.rows = rows
    
    def get_screen_width(self):
        return self.screen_width
    
    def set_screen_width(self, width):
        self.screen_width = width
    
                
