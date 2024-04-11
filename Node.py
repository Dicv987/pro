import copy

class Node:
    def __init__(self, rubik, heuristic_value=0,last_move=None, path=[] ,path_cost=0):
        self.rubik = copy.deepcopy(rubik)
        self.heuristic_value = heuristic_value
        self.path = path
        self.path_cost = path_cost
        self.last_move = last_move  # Stores the last move

    def __lt__(self, other):
        return self.heuristic_value < other.heuristic_value

    def __eq__(self, other):
        return self.rubik == other.rubik

    def __hash__(self):
        return hash(str(self.rubik))

    def __hashbfs__(self):
        return hash(tuple(map(tuple, self.rubik)))

    def add_move(self, move, clockwise):
        direction = 'CW' if clockwise else 'CCW'
        self.path.append(f"{move.__name__} ({direction})")
    