#process of refactoring

class Settings:
    def __init__(self):
        self.states = states = {
    "default":  "#FFFFFF",
    "start": "#FFA500",
    "end": "#A9A9A9",
    "barrier": "#000000",
    "visited": "#6495ED",
    "explore": "#00FF00",
    "shortest_path":  "#EE82EE"}
        
    def get_state(self, state):
        return self.states[state]
    def set_state(self, state):
        self.states[state] = state
