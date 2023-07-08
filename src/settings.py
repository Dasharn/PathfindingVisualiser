class Settings:
    def __init__(self):
        self.states =  {
    "default":  "#FFFFFF",
    "start": "#D0E7FF",
    "end": "#1A34B8",
    "barrier": "#000000",
    "visited": "#87BFFF",
    "explore": "#3366FF",
    "shortest_path": "#8A2BE2",
    "lines": "#07080C"}
        self.screen_width = 750
        self.rows = 50
        
    def get_state_color(self, state):
        return self.states[state]
    
    def set_state_color(self, state):
        self.states[state] = state
    
    def get_states(self):
        return self.states

    def get_rows(self):
        return self.rows
    
    def set_rows(self, rows):
        self.rows = rows
    
    def get_screen_width(self):
        return self.screen_width
    
    def set_screen_width(self, width):
        self.screen_width = width
    
                
