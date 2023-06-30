class Settings:
    def __init__(self):
        self.width = 500

# Node states
        self.states = {
            "default": "#FFFFFF",
            "start": "#FFA500",
            "end":  "#A9A9A9",
            "barrier": "#000000",
            "visited": "#6495ED",
            "explore": "#00FF00",
            "shortest_path": "#FFFF00"
        }

    
    def set_state(self, state, colour):
        self.states[state] = colour
    
    def get_states(self):
        return self.states
    
        
