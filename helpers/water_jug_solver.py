class WaterJugSolver:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def solver(self):
        visited_states = set()
        actions = []
        
        def dfs(current_x, current_y):
            if (current_x, current_y) in visited_states:
                return False
            
            visited_states.add((current_x, current_y))
            
            if (current_x == self.z and current_y == 0) or (current_y == self.z and current_x == 0):
                return True
            
            possible_actions = [
                ("Fill X", self.x, current_y),
                ("Fill Y", current_x, self.y),
                ("Empty X", 0, current_y),
                ("Empty Y", current_x, 0),
                ("Transfer X to Y", max(0, current_x + current_y - self.y), min(current_x + current_y, self.y)),
                ("Transfer Y to X", min(current_x + current_y, self.x), max(0, current_x + current_y - self.x))
            ]
            
            for action_name, action_x, action_y in possible_actions:
                actions.append({"action": action_name, "x": action_x, "y": action_y})
                if dfs(action_x, action_y):
                    return True
                actions.pop()
            
            return False
        
        if dfs(0, 0):
            return actions
        else:
            return None